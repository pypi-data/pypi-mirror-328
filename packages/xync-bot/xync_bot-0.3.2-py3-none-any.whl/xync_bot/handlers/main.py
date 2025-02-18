import logging
from os import path

from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import CommandStart, CommandObject, IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (
    User as TgUser,
    ChatMemberUpdated,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    ChatJoinRequest,
    WebAppInfo,
    FSInputFile,
)
from aiogram.utils.deep_linking import create_start_link
from aiogram.utils.web_app import WebAppUser
from tg_auth import Lang
from xync_schema.models import User, UserStatus, Order, Msg, Forum

from xync_bot.shared import NavCallbackData

main = Router()


class RrCallbackData(CallbackData, prefix="reg_res"):  # registration response
    to: int
    res: bool


home_btns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Invite", callback_data=NavCallbackData(to="ref_link").pack()),
            InlineKeyboardButton(text="Get VPN", callback_data=NavCallbackData(to="get_vpn").pack()),
        ]
    ]
)


@main.message(CommandStart(deep_link=True, deep_link_encoded=True))
async def start_handler(msg: Message, command: CommandObject):
    me: TgUser = msg.from_user
    ref_id: int = command.args.isnumeric() and int(command.args)
    user = await User.get_or_none(id=me.id, status__gte=UserStatus.RESTRICTED)
    rm = None
    if user:
        rs, rm = f"{me.full_name}, you have registered already😉", home_btns
    elif not (ref := await User.get_or_none(id=ref_id)):
        rs = f"No registered user #{ref_id}😬"
    else:  # new user created
        user, cr = await user_upsert(me)
        await user.update_from_dict({"ref": ref}).save()
        approve_btns = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Отклонить", callback_data=RrCallbackData(to=user.id, res=False).pack()),
                    InlineKeyboardButton(text="Одобрить", callback_data=RrCallbackData(to=user.id, res=True).pack()),
                ]
            ]
        )
        await msg.bot.send_message(
            ref.id, f"{me.full_name} просит что б Вы взяли за него/ее ответственность", reply_markup=approve_btns
        )
        return await msg.answer(f"Please wait for @{ref.username} approving...")
    return await msg.answer(rs, reply_markup=rm)


@main.callback_query(RrCallbackData.filter())
async def phrases_input_request(cb: CallbackQuery, callback_data: RrCallbackData) -> None:
    protege = await User[callback_data.to]
    if callback_data.res:
        # protege.status = UserStatus.RESTRICTED
        await protege.save()
        rs = f"{cb.from_user.full_name}, теперь Вы несете ответветвенность за {protege.username}"
    else:
        rs = f'Вы отклонили запрос юзера "{protege.username}" на Вашу протекцию'
    res = {True: "одобрил", False: "отклонил"}
    txt = f"{cb.from_user.full_name} {res[callback_data.res]} вашу регистрацию"
    txt, rm = (f"Поздравляем! {txt}💥", home_btns) if callback_data.res else (f"К сожалению {txt}😢", None)
    await cb.bot.send_message(protege.id, txt, reply_markup=rm)
    await cb.answer("👌🏼")
    await cb.message.edit_text(rs)


@main.message(CommandStart(deep_link=True))  # attempt to reg by fake link
async def fraud_handler(msg: Message):
    logging.info(f"Start: {msg.from_user.id}. Msg: {msg}")
    # todo: alert to admins! Fraud attempt!
    await msg.answer("🤔")


@main.message(CommandStart())
async def start_no_ref_handler(msg: Message):
    me = msg.from_user
    user, cr = await user_upsert(me)
    rr = "сначала вы должны найти поручителя, и перейти по его реферальной ссылке.\nhttps://telegra.ph/XyncNet-02-13"
    if cr:  # has ref and created now
        await msg.answer(f"Здравствуйте {me.full_name}, что бы использовать возможности нашей сети, {rr}")
    elif not user.ref_id:
        await msg.answer(rr.capitalize())
    else:
        await msg.answer(f"{me.full_name}, не балуйтесь, вы и так уже активный участник👌🏼", reply_markup=home_btns)


@main.callback_query(NavCallbackData.filter(F.to == "ref_link"))
async def ref_link_handler(cbq: CallbackQuery):
    me = cbq.from_user
    if not (u := await User.get_or_none(id=me.id, status__gt=UserStatus.RESTRICTED).prefetch_related("ref")):
        return await cbq.answer(f"{me.full_name}, сначала сами получите одобрение поручителя😉")
    link = await create_start_link(cbq.bot, str(u.id), encode=True)
    logging.info(f"Start: {me.id}. Msg: {cbq}")
    await cbq.message.answer(
        f"Your referrer is {u.ref_id and u.ref.username}"
        f"\nThis is your invite link: {link}"
        f"\nGive it to your protege, and approve his request"
    )
    await cbq.answer("Wait for your protege request..")


async def user_upsert(u: TgUser | WebAppUser, status: UserStatus = None) -> (User, bool):
    pic = (
        (gpp := await u.get_profile_photos(0, 1)).photos and gpp.photos[0][-1].file_unique_id
        if type(u) is TgUser
        else (u.photo_url[0] if u.photo_url else None)
    )
    udf = {
        "username": u.username,
        "first_name": u.first_name,
        "last_name": u.last_name,
        "status": UserStatus.MEMBER,
        "lang": u.language_code and Lang[u.language_code],
        "pic": pic,
    }
    if status:
        udf.update({"status": status})
    return await User.update_or_create(udf, id=u.id)


@main.my_chat_member()
async def user_set_status(my_chat_member: ChatMemberUpdated):
    u: TgUser = my_chat_member.from_user
    new_status = UserStatus[my_chat_member.new_chat_member.status.upper()]
    await user_upsert(u, status=new_status)


@main.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def on_user_leave(member: ChatMemberUpdated):
    forum = await Forum[member.chat.id]
    if not forum.joined:
        resp = (
            f"{member.from_user.username or member.from_user.full_name}#{member.from_user.id} "
            f"already leaved from {member.chat.title}#{member.chat.id}"
        )
        logging.error(resp)
    else:
        forum.joined = False
        await forum.save()
        resp = "Bye!"
    return await member.bot.send_message(member.new_chat_member.user.id, resp)


@main.chat_join_request()
async def on_join_request(req: ChatJoinRequest):
    forum = await Forum[req.chat.id]
    if forum.user_id != req.from_user.id:
        resp = f"{req.chat.title} is chat for user#{forum.user_id}"
        logging.error(resp)
        forum.joined = not await req.decline()
    else:
        resp = "Welcome!"
        forum.joined = await req.approve()
        cp = (await req.bot.get_chat(req.chat.id)).photo
        if not cp:
            pth = path.join(path.dirname(path.abspath(__file__)), "xicon.png")
            await req.chat.set_photo(FSInputFile(pth))
    await forum.save()
    return await req.bot.send_message(req.user_chat_id, resp)


@main.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(member: ChatMemberUpdated):
    forum = await Forum[member.chat.id]
    rm = None
    if forum.user_id != member.from_user.id:
        if member.from_user.id in (6806432376, forum.created_by):
            return
        resp = f"{member.chat.title} is chat for user#{forum.user_id}"
        logging.error(resp)
        await member.bot.ban_chat_member(member.chat.id, member.from_user.id)
    else:
        resp = "Welcome to XyncNetwork"
        rm = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Go!", web_app=WebAppInfo(url="https://t.me/XyncNetBot/test"))]]
        )
    return await member.bot.send_message(member.new_chat_member.user.id, resp, reply_markup=rm)


@main.message(F.is_topic_message)
async def order_msg(msg: Message):
    sender = await User[msg.from_user.id]
    cid = msg.chat.shifted_id
    assert sender.forum == cid, "sender is not client"
    if order := await Order.get_or_none(taker__user_id=sender.id, taker_topic=msg.message_thread_id):
        is_taker = True
    elif order := await Order.get_or_none(ad__agent__user_id=sender.id, maker_topic=msg.message_thread_id):
        is_taker = False
    else:
        return await msg.answer("No such order")
        # raise Exception("No such order")
    receiver: User = await (order.ad.agent.user if is_taker else order.taker.user)
    rcv_topic = order.taker_topic if is_taker else order.maker_topic
    await Msg.create(tgid=msg.message_id, txt=msg.text, order_id=order.id, receiver=receiver)
    return await msg.send_copy(receiver.forum, message_thread_id=rcv_topic)


@main.message(
    F.content_type.not_in(
        {
            # ContentType.NEW_CHAT_MEMBERS,
            ContentType.FORUM_TOPIC_CLOSED,
            ContentType.GENERAL_FORUM_TOPIC_HIDDEN,
            # ContentType.LEFT_CHAT_MEMBER,
            ContentType.SUPERGROUP_CHAT_CREATED,
            ContentType.NEW_CHAT_PHOTO,
            # ContentType.FORUM_TOPIC_CREATED,
            # ContentType.FORUM_TOPIC_EDITED,
            # ContentType.FORUM_TOPIC_CLOSED,
        }
    )
)
async def del_cbq(msg: Message):
    await msg.delete()
