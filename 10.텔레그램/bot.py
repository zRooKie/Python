# pip install telepot
import telepot
import logging
import os
import module

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# python_zbot
TELEGRAM_TOKEN = "1008187595:AAGL02LaLikb01ongTvYCHXECuazHXSjbpM"

    
def handler(msg):
    content_type, chat_Type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)

    print(msg)
    if content_type == "text":
        # bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))
        str_message = msg["text"]
        if str_message[0:1] == "/": # 명령어 라면 ex) /dir c:\\test
            args = str_message.split(" ")
            command = args[0]
            del args[0]

            if command == "/dir":
                filepath = " ".join(args) # 리스트를 문자열화
                if filepath.strip() == "":
                    bot.sendMessage(chat_id, "/dir [대상폴더] 로 입력해주세요.")
                else:
                    filelist = module.get_dir_list(filepath)
                    bot.sendMessage(chat_id, filelist)
            elif command == "/weather" or command == "/날씨":
                w = " ".join(args)
                weather = module.get_weather(w)
                bot.sendMessage(chat_id, weather)
            elif command == "/money" or command == "/환율":
                w = " ".join(args)
                output = module.money_translate(w)
                bot.sendMessage(chat_id, output)
            elif command[0:4] == "/get":
                filepath = " ".join(args)
                if os.path.exists(filepath):
                    try:
                        if command == "/getfile":
                            bot.sendDocument(chat_id, open(filepath, "rb")) # 파일 전송
                        elif command == "/getimage":
                            bot.sendPhoto(chat_id, open(filepath, "rb"))
                        elif command == "/getaudio":
                            bot.sendAudio(chat_id, open(filepath, "rb"))
                        elif command == "/getvideo":
                            bot.sendVideo(chat_id, open(filepath, "rb"))
                    except Exception as e:
                        bot.sendMessage(chat_id, "파일 전송 실패 {}".format(e))
                else:
                    bot.sendMessage(chat_id, "파일이 존재하지 않습니다.")


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)