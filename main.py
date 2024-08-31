import asyncio
from pyrogram import Client
import time
import betterlogging as logging

logger = logging.get_colorized_logger(name="test")

handler = logging.StreamHandler()
handler.setFormatter(logging.ColorizedFormatter(hide_lib_diagnose=False))

logger.addHandler(handler)
logger.setLevel(logging.TRACE)

proxy = {
    "scheme": "http",
    "hostname": "149.154.167.51",
    "port": 3128,
}

# Messages
message_uzb = """Assalomu alaykum. Ahvollaringiz yaxshimi?"""
message_eng = """Good day, sir. How are you doing today?"""
ms_Fr = """Assalomu alaykum, qalaysan jo'ra?"""


api_id = 25082563
api_hash = "06b32fda7848f364cf2f8f3bbfbb6569"

foreign_teachers = {"MrRichard": 1027127916, "MrMark": 1386729860}
relatives_weekly = {"DilbarAnam": 5080056361, "EldorOgom": 5850989566, "NasibaOyopom": 1909437369,
                    "OgabekOgom": 5150749605, "SardorOgom": 661366378, "ShohidaOyopom": 671094725,
                    "XushnudOgom": 5887223087, "RavshanOgom": 213657604}
uzb_teachers = {"DilfuzaOpa": 288169871, "DilshodOgom": 5220655446, "GenjegulOpa": 795517191, "HamidOga": 454690085,
                "XumoroyOpa": 196677465, "GulnazOpa": 353474941, "MuhabbatEmjarovna": 493381511,
                "ValibekOgo": 852034815, "ShavkatAka": 244850114}
relatives_daily = {"Ammam": 584282619, "Oyim": 6185732889}

friends = {
    "Kamol": 815168501, 
    "ShohruhYuldashev": 1882150090, 
    "Rustam": 5167399424
}


# sending messages
async def send_daily_relatives(app):
    for key, value in relatives_daily.items():
        try:
            await app.send_message(chat_id=value, text=message_uzb)
            print("Sent to Daily relatives")
        except Exception as err:
            logger.exception(err)


# sending messages
async def send_weekly_relatives(app):
    for key, value in relatives_weekly.items():
        try:
            await app.send_message(chat_id=value, text=message_uzb)
            print("Weekly relatives.... done")
        except Exception as err:
            logger.exception(err)
    
    for key, value in friends.items():
        try: 
            await app.send_message(chat_id=value, text=ms_Fr)
            print("friends done")
        except Exception as err:
            logger.exception(err)



# sending messages
async def send_teachers(app):
    for key, value in uzb_teachers.items():
        try:
            await app.send_message(chat_id=value, text=message_uzb)
            print("Sent to Uzb teachers")
        except Exception as err:
            logger.exception(err)
    for key, value in foreign_teachers.items():
        try:
            await app.send_message(chat_id=value, text=message_eng)
            print("Sent to foreign teachers")

        except Exception as err:
            logger.exception(err)


async def additional_function(meet, app):
    while not meet:
        print("main function initiated")
        current_time = {
            "day": time.localtime().tm_wday,
            "hours": time.localtime().tm_hour,
            "minutes": time.localtime().tm_min,
            "seconds": time.localtime().tm_sec
        }
        print(current_time['day'])
        await send_daily_relatives(app)
        if current_time['day'] == 5:
            await send_weekly_relatives(app)
        if current_time['day'] == 6:
            await send_teachers(app)
        meet = True
        print("sleeping...")
        await asyncio.sleep(86400)
        print("woke up")


async def main_function(app):
    print("initiated...")
    meet = False
    await additional_function(meet, app)
    await main_function(app)


async def main():
    async with Client(name="6393999936", api_id=api_id, api_hash=api_hash, phone_number="998945956113", password="Imagine_Believer1_Dragons") as app:
        await main_function(app)


asyncio.run(main())
