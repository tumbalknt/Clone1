import base64

from pyrogram import filters
from pyrogram import Client
from pyrogram import Client as gez
from pyrogram.types import Message

from geez.modules.help import add_command_help


@gez.on_message(filters.command("encod", ".") & filters.me)
async def encod(client: Client, message: Message):
    match = message.pattern_match.group(1)
    if not match and message.is_reply:
        gt = await message.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or message.is_reply):
        return await message.edit("`Give me Something to Encode..`")
    byt = match.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await message.edit(f"**=>> Encoded Text :** `{match}`\n\n**=>> OUTPUT :**\n`{atc}`")


@gez.on_message(filters.command("decod", ".") & filters.me)
async def encod(client: Client, message: Message):
    match = message.pattern_match.group(1)
    if not match and message.is_reply:
        gt = await message.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or message.is_reply):
        return await message.edit("`Give me Something to Decode..`")
    byt = match.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await message.edit(
            f"**=>> Decoded Text :** `{match}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await message.edit("**ERROR :** " + str(p))


add_command_help(
    "Base64",
    [
        ["encod", "Encode base64."],
        ["decod", "Decode bade64."],
    ],
)
