__MODULE__ = "ʀᴇᴀᴄᴛɪᴏɴ"
__HELP__ = """
<blockquote>Bantuan Untuk Reaction

perintah : <code>{0}react</code> [chat_id/@username] [emoji/random]
    memberikan reaction emoji ke semua pesan
   
perintah : <code>{0}stopreact</code>
    membatalkan proses reaction</blockquote>
"""

import asyncio
import random
from PyroUbot import *
from pyrogram.errors import FloodWait

reaction_progress = []

RANDOM_EMOJIS = [
    "😀", "😂", "😍", "😎", "😢", "😡", "👍",
    "👎", "🙏", "👏", "❤️", "🗿", "😭", "🔥",
]

@PY.UBOT("react")
@PY.TOP_CMD
async def react_command(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 3:
        return await message.reply(f"<blockquote><b>{ggl} Format salah!\nGunakan: .react [chat_id/@username] [emoji/random]</b></blockquote>")

    chat_id = message.command[1]
    emoji = message.command[2]

    if emoji.lower() == "random":
        emoji = random.choice(RANDOM_EMOJIS)

    reaction_progress.append(client.me.id)
    sukses = 0
    gagal = 0

    proses = await message.reply(f"<b>{prs} Memulai reaction ke {chat_id} dengan emoji: {emoji}</b>")

    try:
        async for msg in client.get_chat_history(chat_id):
            if client.me.id not in reaction_progress:
                break
            await asyncio.sleep(0.5)
            try:
                await client.send_reaction(
                    chat_id=msg.chat.id,
                    message_id=msg.id,
                    emoji=emoji
                )
                sukses += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception:
                gagal += 1
    except Exception as e:
        return await proses.edit(f"<b>{ggl} ERROR:</b> <code>{str(e)}</code>")
    finally:
        if client.me.id in reaction_progress:
            reaction_progress.remove(client.me.id)

    await proses.edit(
        f"<b>{sks} Reaction selesai!</b>\n"
        f"Chat: <code>{chat_id}</code>\n"
        f"Emoji: <code>{emoji}</code>\n"
        f"Sukses: <code>{sukses}</code>\n"
        f"Gagal: <code>{gagal}</code>"
    )


@PY.UBOT("stopreact")
@PY.TOP_CMD
async def stopreact_command(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)

    if client.me.id in reaction_progress:
        reaction_progress.remove(client.me.id)
        await message.reply(f"<blockquote><b>{sks} Berhasil membatalkan proses reaction</b></blockquote>")
    else:
        await message.reply(f"<blockquote><b>{ggl} Tidak ada proses reaction yang sedang berjalan</b></blockquote>")
