from turtle import update
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5545375040:AAHYL00-0cjUEpsRxWbAIva7M7jS5o6IC-0",use_context=True)


def unknown_text(update: Update, context: CallbackContext):
    if update.message.text[0]!='/' and update.message.text[0:5]!='https':
        update.message.reply_text("Send Link 💜")
        update.message.reply_text("Not this shit🌝")
    if update.message.text[0]=='/':
         update.message.reply_text("Send Link 💜")
    if update.message.text[0:5]=='https':
         l=""+update.message.text
         l = l[32:65]
         lss = 'https://www.googleapis.com/drive/v3/files/'  
         rss = '?alt=media&key=AIzaSyBokHWqYruKtek6j7vN_VGS3PY56bFFZ2w'
         fl = lss + l + rss
         update.message.reply_text(" %s "% fl)

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()
