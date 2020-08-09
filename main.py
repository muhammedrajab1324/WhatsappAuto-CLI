from Action import *
import pyautogui

name_of_person = str(input("Name of the person that you want to send: "))
msg = str(input("Enter your message: "))
time_to_snd = str(input("Enter the time to send(In 24-hour format): "))

bot = Whatsapp_Bot(msg, time_to_snd, name_of_person)

bot.do_at_time()

while True:
    schedule.run_pending()
