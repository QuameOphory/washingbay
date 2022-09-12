import random
from datetime import date, timedelta

def coupon_number():
    return 'C' + str(date.today().year)[-2:] + str(date.today().month)[-2:] + str(random.randrange(100, 999))

def coupon_expiry():
    return date.today() + timedelta(weeks=2)