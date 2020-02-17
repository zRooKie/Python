# pip install python-telegram-bot
import telegram

# zrookietestbot
bot = telegram.Bot(token = "1087555363:AAHAOQxPvUCCOmARXKHUBiKO4-4ra7BmRyQ")

# for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id=1005667850, text="테스트입니다.")