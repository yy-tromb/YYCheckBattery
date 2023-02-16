import schedule
from plyer import notification
import psutil
import win11toast
import time
import os


def toast_plyer():
    battery = psutil.sensors_battery()
    m, s = divmod(battery.secsleft, 60)
    h, hm = divmod(m, 60)
    fixm = ""
    if hm < 10:
        fixm = f"0{hm}"
    else:
        fixm = f"{hm}"
    if battery.percent < 70 and battery.power_plugged == False:
        notification.notify(
            app_name="YYCheckBattery",
            title="Plug Now!!",
            message=f"Battery is {battery.percent}%.\nYou can use {h}:{fixm}",
            timeout=5
        )
    elif battery.percent > 90 and battery.power_plugged == True:
        notification.notify(
            app_name="YYCheckBattery",
            title="Remove the Plug!!",
            message=f"Battery is {battery.percent}%.\nYou can use {h}:{fixm}",
            timeout=5
        )


def toast_win11():
    battery = psutil.sensors_battery()
    m, s = divmod(battery.secsleft, 60)
    h, hm = divmod(m, 60)
    fixm = ""
    if hm < 10:
        fixm = f"0{hm}"
    else:
        fixm = f"{hm}"
    message = ""
    if battery.percent < 70 and battery.power_plugged == False:
        message = "Plug Now!!"
    elif battery.percent > 90 and battery.power_plugged == True:
        message = "Remove the Plug!!"
    else:
        return 0
    win11toast.notify(
        title="YYCheckBattery",
        body=message,
        progress={
            "title": "Now Battery:",
            "status": f"{h}:{fixm} left",
            "value": battery.percent / 100,
            "valueStringOverride": f"{battery.percent}%",
        },
        duration="short"
    )


if (os.name == "nt"):
    schedule.every(1).minutes.do(toast_win11)
    win11toast.toast(title="YYCheckBattery",body="Started check", audio={"silent": "true"})
else:
    schedule.every().minutes.do(toast_plyer)
    notification.notify(
        app_name="YYCheckBattery",
        title="Started check",
        message="@yyhome-tromb"
    )


while True:
    schedule.run_pending()
    time.sleep(5)
