import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في بوت الذكاء الاصطناعي!\n\n"
        "أرسل لي صورة واكتب ماذا تريد أن أفعل بها."
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ وصلتني رسالتك!\n\n"
        "نحن الآن نجهز ربط الذكاء الاصطناعي."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, message))

app.run_polling()
