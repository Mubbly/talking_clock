from datetime import datetime
from gtts import gTTS
from time import sleep
import os

last_hour = -1


def notify(current_time: int):
    notification_text = "Current time is now:" + str(current_time)
    tts = gTTS(text=notification_text, lang="en")
    notification_sound_mp3 = "notification.mp3"
    tts.save(notification_sound_mp3)
    os.system("mpg321 notification.mp3")


while True:
    current_hour = datetime.now().hour
    if current_hour != last_hour:
        notify(current_hour)
        last_hour = current_hour
    sleep(5)
