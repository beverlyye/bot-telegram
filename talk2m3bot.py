import threading
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

bot_lock = threading.Lock()

TOKEN: Final = '6581449693:AAEIpCBITfHLgqgDTTH8mr71ucD3gCzaGpU'
BOT_USERNAME: Final = '@talk2m3bot'

app = Application.builder().token(TOKEN).build()

async def run_bot():
    async with bot_lock:
        print(f"Bot is running with token: {TOKEN}")


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
   
    keywords = {
        'sad': "I feel sorry for you. but just so u know, for anything bad you faced, there is always the good impact that can makes you a better person ",
        'happy': "I'm glad to hear that! wow! im also super hyped knowing you are having a good day, it felt really nice knowing you smile to the whole world :D",
        'thank': "youre welcome! do text me if you want to tell another story",
        'upset': "I know you must felt so upset. Cheer up dear! sometimes you need to let it g, than the next day when you woke up, everythings gonna be an amazing day, you did great today, im so proud",
        'funny': "HAHAHA, glad it makes your mood fly high up!",
        'tired': 'Sometimes all we need is a good and effective rest! just close your eyes, take a deep breath and relax your mind'
    }

    for keyword, response in keywords.items():
        if keyword in processed:
            return response

    return "pardon? i cant understand what you wrote, sorry"

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

    with bot_lock:
        run_bot()

    #commands

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help' , help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('upset', upset_command))
    app.add_handler(CommandHandler('happy', happy_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, take_message))

    #errors
    app.add_error_handler(error)

    #polls the bot
    print('Polling..')
    app.run_polling(poll_interval=3)

