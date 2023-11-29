# import pyttsx3
#
# engine = pyttsx3.init()
#
# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 150)     # setting up new voice rate
#
# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#
# """ text write"""
# engine.say("Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework. It aims to cover the most common use cases of JWTs by offering a conservative set of default features. It also aims to be easily extensible in case a desired feature is not present.First we need to install django-rest-framework-simplejwt package")
# engine.runAndWait()

#
# def work_with_list(a):
#     b=a[0]
#     for i in a:
#         if i<b:
#             b=i
#     print(b)
#     for i in a:
#         s=i*b
#         print(s)
#
#
# work_with_list([12, 23, 89, 45,2])
# d="yes"
# print(type(d))

from datetime import date, datetime
from playsound import playsound

enter_hour = input("Budulnik uchun vaqt kiriting(15:34): ")
current_hour = enter_hour[0:2]
current_minut = enter_hour[3:]
print("Budulnik o'rnatilayapti...")
while True:
    time = datetime.now()
    if current_hour == time.strftime("%H"):
        if current_minut == time.strftime("%M"):
            print("Uyqudan Turing endi Burhon aka")
            playsound('audio.mp3')
            break