from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6581449693:AAEIpCBITfHLgqgDTTH8mr71ucD3gCzaGpU'
BOT_USERNAME: Final = '@talk2m3bot'


async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('Hi! if you are using this bot, it means that you have a story to share with? please continue love <3')


async def help_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a listener bot! please type anything to get my response')


async def custom_command (update: Update, context: ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text ('This is a custom command!')


def take_response(text: str) -> str:
   processed: str = text.lower()
   
   if 'hi' in processed:
        return 'hey there!'
   
   if 'im having a bad day' in processed:
       return 'how come? tell me'
   
   if 'im having a good day' in processed:
       return 'glad to hear that! what makes you happy?'
   
   return 'pardon? i  cant understand what you wrote, thankyou'


async def take_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_tipe: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_tipe}: "{text}"')

    if message_tipe == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, ' ').strip()
            response: str = take_response(new_text)
        else:
            return
    else:
        response: str = take_response(text)

        print('Bot:', response)
        await update.message.reply_text(response)



