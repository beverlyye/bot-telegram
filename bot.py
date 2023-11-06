from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, contextTypes

TOKEN: Final = '6581449693:AAEIpCBITfHLgqgDTTH8mr71ucD3gCzaGpU'
BOT_USERNAME: Final = '@talk2m3bot'

async def start_command (update: Update, context: contextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('Hi! if you are using this bot, it means that you have a story to share with? please continue love <3')
                                     
async def help_command (update: Update, context: contextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a listener bot! please type anything to get my response')

async def custom_command (update: Update, context: contextTypes. DEFAULT_TYPE):
    await update.message.reply_text ('This is a custom command!')