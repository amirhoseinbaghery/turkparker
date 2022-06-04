from django.utils import timezone

from . import jalali


def persian_num(mystr):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }

    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr


def jalali_conv(time):
    jmonth = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    time = timezone.localtime(time)

    time_str = "{},{},{}".format(time.year, time.month, time.day)
    time_tuple = jalali.Gregorian(time_str).persian_tuple()
    time_list = list(time_tuple)
    for index, month in enumerate(jmonth):
        if time_list[1] == index + 1:
            time_list[1] = month
            break

    output = "{}/ {}/ {}, ساعت {}:{}".format(
        time_tuple[2],
        time_tuple[1],
        time_tuple[0],
        time.hour,
        time.minute,
    )
    return persian_num(output)
