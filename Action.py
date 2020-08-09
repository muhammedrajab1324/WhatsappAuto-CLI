"""
This program is only for 1366x768 resolution display monitor.
If u got different Resolution U have to assign your own Mouse position
If you found this helpful don't forget to subscribe my channel
Created by Muhammed Rajab
About Me:
I am Muhammed Rajab,14 year old. Really passionate about Hacking, programming
and some music. I you guys want to work with me in my new projects contact me: 9544240675
This one is for those who knows  python a little.
If you are complete beginner, and if you want the GUI version , Stay tuned and subscribe my youtube channel!
link to youtube: https://youtu.be/03EWk-EJSXU
GUI VERSION COMING SOON!
"""

try:
    import os
    import pyautogui
    from webbrowser import open
    import time
    import schedule
except ImportError as err:
    print(f"Some modules are not found! {err}")


class Whatsapp_Bot:
    """
    time_to_do is the time that u wanna send the message.
    message is the message that u wanna snd
    person is the guy u wanna send the message
    This is the best version of whatsapp bot
    """

    def __init__(self, message, time_to_do, person):
        self.message = message
        self.time_to_do = time_to_do
        self.person = person.lower()

    """
    This function opens minimize all the active window, sleeps for 3 seconds, Opens
    WhatsApp Web
    
    """

    @staticmethod
    def open_browser():
        pyautogui.hotkey('winleft', 'm')
        time.sleep(3)
        open("https://web.whatsapp.com/")
        time.sleep(15)
        pyautogui.press('f11')
        time.sleep(15)

    """
    The function to send message.
    U have to define your own positions.
    First One is whatsapp web search box position
    Second one is the message box position
    """

    def snd_msg(self):
        # Search box position
        pyautogui.click(134, 76)
        pyautogui.typewrite(self.person, 0.25)
        pyautogui.press('return')
        time.sleep(3)
        pyautogui.click(601, 699)
        pyautogui.typewrite(self.message)
        pyautogui.press('return')
        time.sleep(5)

    """
    A main function to make this code more simple and easy to read!
    """

    def main(self):
        self.open_browser()
        self.snd_msg()
        pyautogui.press('f11')

    """
    Function to snd message at time! 
    """

    def do_at_time(self):
        schedule.every().day.at(self.time_to_do).do(self.main)