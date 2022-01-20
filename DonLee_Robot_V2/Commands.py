# (c) [Muhammed] @YOUR_NARUTO_1
# (s) @new_movies_group_2021 , @new_all_movies_club, @NETFLIXINDIA2022
# Copyright permission under MIT License
# All rights reserved by YOUR_NARUTO_1
# License -> https://github.com/NORUTO-SUPPORT-MAD-YT/DonLee-Robot-V2

import random
from pyrogram import filters, Client as DonLee_Robot_V2
from DonLee_Robot_V2.Config_Vars.Vars import Config
from DonLee_Robot_V2 import Text, Import, Database, LOGGER

db = Database()

@DonLee_Robot_V2.on_message(filters.command(["start", "alive"]) & filters.private)
async def start(bot: DonLee_Robot_V2, msg: Import.Msg):
    START_BUTTON = [[  
          Import.Button("💠 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗍𝗌 💠", url=f"http://t.me/{Config.BOT_USERNAME}?startgroup=true")
          ],[
          Import.Button("⚠️ 𝖧𝖾𝗅𝗉", callback_data="help"),
          Import.Button("𝖠𝖻𝗈𝗎𝗍 🤠", callback_data="about")
          ]]
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id)
    try:
        file_uid = msg.command[1]
    except IndexError:
        file_uid = False
             
    if file_uid:
        try:
            user = await bot.get_chat_member(Config.FORCE_CHANNEL, msg.chat.id)
            if user.status == "kicked out":
               await msg.reply_text("😔 𝖲𝗈𝗋𝗋𝗒 𝖣𝗎𝖽𝖾, 𝖸𝗈𝗎 𝖺𝗋𝖾 ⚠️🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎⚠️")
               return
        except Import.User:
            userbot = await bot.get_me()
            await msg.reply_text(
                text=Config.FORCE_SUB_TEXT.format(msg.from_user.mention),
                reply_markup=Import.Markup([
                    [ Import.Button(text="🔔 𝖩𝗈𝗂𝗇", url=f"https://t.me/{Config.FORCE_CHANNEL}"),
                      Import.Button(text="Try Again 🔃", url=f"https://t.me/{Config.BOT_USERNAME}?start={file_uid}")]       
              ])
            )
            return

        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return

        if Config.CAPTION_BOLD_OR_MONO == "bold":
            caption = ("<b>" + file_name + "</b>")
        else:
            caption = ("<code>" + file_name + "</code>")
        try:
            await msg.reply_cached_media(
                file_id,
                quote=True,
                caption = f"""{caption}\n\n{Config.CUSTOM_CAPTION}""",
                parse_mode="html",
                reply_markup=db.Donlee_bt
            )

        except Exception as e:
            await msg.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    button = [[
     Import.Button('💠 Add Me To Your Groups 💠', url='http://t.me/donlee_robot?startgroup=true')
    ]]
    await msg.reply_photo(
    photo=random.choice(Config.PHOTO),
    caption=Text.START_TEXT.format(msg.from_user.mention, Config.DEV_ID),
    reply_markup=Import.Markup(START_BUTTON))


@DonLee_Robot_V2.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot: DonLee_Robot_V2, msg: Import.Msg):
        button = [[
          Import.Button("💡𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝚁𝚁", callback_data="autofilter"),
          Import.Button("📍𝙼𝙰𝙽𝚄𝙰𝙻 𝙵𝙸𝙻𝚃𝙴𝚁", callback_data="filter"),
          Import.Button("⚒️𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂", callback_data="connection")
          ],[
          Import.Button("⚙️𝙱𝙰𝙽", callback_data="ban"),
          Import.Button("📡𝙼𝚄𝚃𝙴", callback_data="mute"),
          Import.Button("🔗𝙿𝚄𝚁𝙶", callback_data="purge")
          ],[
          Import.Button("🛡️𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙿𝙷", callback_data="telegraph"),
          Import.Button("🧹𝚃𝚃𝚂", callback_data="tts"),
          Import.Button("🗿𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳", callback_data="sticker")
          ],[
          Import.Button("🇮🇳𝙲𝙾𝙽𝚃𝚁𝚈", callback_data="country"),
          Import.Button("🙄𝙼𝙴𝙼𝙴", callback_data="meme")
          ],[
          Import.Button("🤧𝙲𝙾𝚅𝙸𝙳", callback_data="covid"),
          Import.Button("🎾𝚁𝙴𝙿𝙾𝚁𝚃", callback_data="report"),
          Import.Button("🎗️𝚆𝙴𝙻𝙲𝙾𝙼𝙴", callback_data="welcome")
          ],[
          Import.Button("🏠𝙷𝙾𝙼𝙴", callback_data="home"),
          Import.Button("🔰𝚂𝚃𝙰𝚃𝚂", callback_data="status"),
          Import.Button("𝙰𝙱𝙾𝚄𝚃🤠", callback_data="about")
          ]]
        await bot.send_photo(
            chat_id=msg.chat.id,
            photo=random.choice(Config.PHOTO),
            caption=Text.HELP_TEXT,
            reply_markup=Import.Markup(button),
            parse_mode="html", 
            reply_to_message_id=msg.message_id
        )



@DonLee_Robot_V2.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot: DonLee_Robot_V2, msg: Import.Msg):
        button = [[
          Import.Button("👨‍💻𝖣𝖾𝗉𝗅𝗈𝗒", url='https://youtube.com/channel/UCEK86p-F18gR-zd9LwLH4Gw'),
          Import.Button("𝖲𝗈𝗎𝗋𝖼𝖾📦", callback_data="source")
          ],[
          Import.Button("⚠️𝖧𝖾𝗅𝗉", callback_data="help"),
          Import.Button("🏠𝖧𝗈𝗆𝖾", callback_data="home"),
          Import.Button("𝖢𝗅𝗈𝗌𝖾🗑️", callback_data="close")
          ]]                     
        await bot.send_photo(
            chat_id=msg.chat.id,
            photo=random.choice(Config.PHOTO),
            caption=Text.ABOUT_TEXT.format(Config.BOT_USERNAME, Config.DEV_ID, Config.DEV_NAME, Config.BOT_USERNAME),
            reply_markup=Import.Markup(button),
            parse_mode="html", 
            reply_to_message_id=msg.message_id
        )


@DonLee_Robot_V2.on_message(filters.command(["sub", "subscribe"]) & filters.private, group=1)
async def sub(bot: DonLee_Robot_V2, msg: Import.Msg):
        button = [[     
          Import.Button("🖥️𝖵𝗂𝖽𝖾𝗈", url="https://youtube.com/channel/UCEK86p-F18gR-zd9LwLH4Gw"),
          Import.Button("𝖲𝗎𝗉𝗉𝗈𝗋𝗍🤝", url="https://youtube.com/channel/UCEK86p-F18gR-zd9LwLH4Gw")
          ],[
          Import.Button("📢𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/new_all_movies_club"),
          Import.Button("𝙶𝚁𝚄𝙾𝙿", url="https://t.me/new_movies_group_2021")
          ],[
          Import.Button("📦𝖦𝗂𝗍𝗁𝗎𝖻", url="https://github.com/NORUTO-SUPPORT-MAD-YT/DonLee-Robot-V2"),
          Import.Button("𝖨𝗇𝗌𝗍𝖺😁", url="https://www.instagram.com/athif_kollayil_")
          ],[
          Import.Button("𝖢𝗅𝗈𝗌𝖾🗑️", callback_data="close")
          ]]                     
        await bot.send_photo(
            chat_id=msg.chat.id,
            photo=random.choice(Config.PHOTO),
            caption=Text.SUB_TEXT.format(Config.BOT_USERNAME, Config.DEV_ID, Config.DEV_NAME, Config.BOT_USERNAME),
            reply_markup=Import.Markup(button),
            parse_mode="html", 
            reply_to_message_id=msg.message_id
        )

@DonLee_Robot_V2.on_message(filters.private & filters.command("report"))
async def admin(bot, msg):
    button = [[  
       Import.Button("𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾➡️", url="https://t.me/YOUR_NARUTO_1")
       ]]
    await msg.reply_text(
        text="𝖢𝗈𝗇𝗍𝖾𝖼𝗍 𝖡𝗎𝗍𝗍𝗈𝗇 𝖡𝖾𝗅𝗅𝗈𝗐",
        reply_markup=Import.Markup(button)
    )
