from telegram import Update
from telegram.ext import (Updater, CommandHandler, MessageHandler,Filters,
                          CallbackContext)
import configparser
import logging
from ChatGPT_HKBU import HKBU_ChatGPT
import os
import mysql.connector

# 更改当前工作目录到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def main():
    # Load your token and create an Updater for your Bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    sql_config = {
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'host': config.get('mysql', 'host'),
    'database': config.get('mysql', 'database')
}   
    # db4free database
    # 连接到数据库
    try:
        conn = mysql.connector.connect(**sql_config)
        cursor = conn.cursor()
        print('sql connection success')

    except mysql.connector.Error as err:
        print(f'sql connection error: {err}')
        
    # You can set this logging module, so you will know when and why things do not work as expected Meanwhile, update your config.ini as:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    # register a dispatcher to handle message: here we register an echo dispatcher
    # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    # dispatcher.add_handler(echo_handler)

    # dispatcher for chatgpt
    global chatgpt
    chatgpt = HKBU_ChatGPT(config)
    chatgpt_handler = MessageHandler(Filters.text & (~Filters.command), equiped_chatgpt)
    dispatcher.add_handler(chatgpt_handler)

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("hello", Hello))
    
    # To start the bot:
    updater.start_polling()
    updater.idle()



def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)


def equiped_chatgpt(update, context): 
    global chatgpt
    reply_message = chatgpt.submit(update.message.text + "Recommend similar or relevent songs to me.")
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def Hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi,i am a LBBo, i am good at recommending music based on your taste. Please tell me what you like!')



if __name__ == '__main__':
    main()
