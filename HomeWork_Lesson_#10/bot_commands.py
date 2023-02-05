from telegram import Update
from telegram.ext import ContextTypes

import datetime


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f' Приветствую ВАС!!!\t {update.effective_user.first_name}\nЯ бот. Cообщать пользователю, сколько дней осталось до Нового Года')
    await update.message.reply_text(f'/time - Настоящее время\n/new_year - сколько дней осталось до НГ\n/exit - Выход')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'time {datetime.datetime.now().time()}')


async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Досвидание")


async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.today()
    NY = datetime.datetime(2024, 1, 1)
    d = NY - now

    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    await update.message.reply_text('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))