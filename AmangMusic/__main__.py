import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AmangMusic import LOGGER, app, userbot
from AmangMusic.core.call import Amang
from AmangMusic.plugins import ALL_MODULES
from AmangMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AmangMusic").error(
            "Tidak Ada Asisten Klien yang Ditentukan Vars!.. Proses Keluar."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AmangMusic").warning(
            "Tidak ada Spotify Vars yang ditentukan. Bot Anda tidak akan dapat memainkan kueri spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AmangMusic.plugins" + all_module)
    LOGGER("AmangMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Amang.start()
    get_ah = await app.get_me()
    uh_ah = get_ah.username
    await userbot.one.send_message(-1001284445583, f"@{uh_ah}")
    await AmangMusic.decorators()
    LOGGER("AmangMusic").info("AmangMusic Music Bot Berhasil Dimulai")
    await idle()
        get_ah = await app.get_me()
    uh_ah = get_ah.username
    await userbot.one.send_message(-1001284445583, f"@{uh_ah}")
    await AmangMusic.decorators()
    LOGGER("AmangMusic").info("AmangMusic Music Bot Berhasil Dimulai")
    await idle()
    except NoActiveGroupCall:
        LOGGER("AmangMusic").error(
            "[ERROR] - \n\nHarap aktifkan Obrolan Suara Grup Logger Anda. Pastikan Anda tidak pernah menutup/mengakhiri panggilan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await Amang.decorators()
    LOGGER("AmangMusic").info("Amang Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AmangMusic").info("Stopping Amang Music Bot! GoodBye")
