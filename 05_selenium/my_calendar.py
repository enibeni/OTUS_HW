import requests
from datetime import datetime


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.ok:
        return r
    return None