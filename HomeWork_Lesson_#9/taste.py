from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bots_commands import *

app = ApplicationBuilder().token("6004768309:AAEBGBTzC2CmxpWhZ8To-wMyYKT6484_Rpg").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()