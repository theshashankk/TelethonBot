from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def startvro(event):
  but = [[Button.url('Creator 💜', "t.me/Albertt_xD")]]
  but += [[Button.inline('Utils', data="utttils")]]
  but += [[Button.url('Gay', f"tg://user?id={event.sender.id}")]]
  if event.is_private:
    return await event.reply(f'**Hey** **[{event.sender.first_name}](tg://user?id={event.sender.id})!**\n**Btw I only Work for @Albertt_xD 💜**', buttons=but)
  if event.sender_id in OWNER_ID:
    await event.reply(f"**Hey Master How are you 😉😉**")
  else:
    await shashank.reply("**Hemlo gay**")
