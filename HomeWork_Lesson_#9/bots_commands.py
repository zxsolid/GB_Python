from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n'
                                    'Введите команду /sum и два числа через пробел.')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    number1 = int(items[1])
    number2 = int(items[2])
    await update.message.reply_text(f'Ваш результат: {number1} + {number2} = {number1 + number2}')