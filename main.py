from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6581449693:AAEIpCBITfHLgqgDTTH8mr71ucD3gCzaGpU'
BOT_USERNAME: Final = '@talk2m3bot'


#commands 

async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('Hi! if you are using this bot, it means that you have a story to share with? please continue to select the command;)')


async def help_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a listener bot! please type anything to get my response')


async def custom_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('This is a custom command!')

async def upset_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('what makes u sad? tell me')

async def happy_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('glad to know! so what makes u happy?')


#responses #buat handle respon dr bot

def take_response(text: str) -> str:
   processed: str = text.lower()
   
   if 'hi' in processed:
        return 'hey there! what can i help you with? please select the command to tell story ;)'
   
   if 'im really sad, because' in processed:
       return 'how come? but just so u know, for anything bad you faced, there is always the good impact that can makes you a better person'
   
   if 'im really happy, because...' in processed:
       return 'glad to hear that! im also super hyped knowing you are having a good day, it felt really nice knowing you smile to the whole world :D'
   
   if 'thankyou' in processed:
       return 'youre welcome! do text me if you want to tell another story'
   
   return 'pardon? i  cant understand what you wrote, sorry'

#messages #handle pesan yg akn di sendback ke user(priv/group)

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


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(TOKEN).build()

     