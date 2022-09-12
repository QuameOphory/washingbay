from dataclasses import dataclass, field
from datetime import date
from helpers.generate_coupon import (
    coupon_number, 
    coupon_expiry
)
import random

@dataclass
class Coupon:
    _amount_on_coupon: float = field(default=0.00)
    coupon_id: str = field(default_factory=coupon_number)
    valid_from: date = field(default=date.today)
    expires_on: date = field(default_factory=coupon_expiry)

    def set_coupon_amount(self, amount):
        self._amount_on_coupon = amount

    def use_coupon(self, amount):
        self._amount_on_coupon -= amount

    def __repr__(self) -> str:
        return f'{self.coupon_id} expires on [{self.expires_on}]'

@dataclass
class Client:

    GENDER = ('Male', 'Female', 'Other')

    first_name: str
    middle_name: str
    last_name: str
    gender: str
    date_of_birth: date
    mobile_number: str
    email_address: str = field(default='')
    


    def client_age(self):
        return date.today() - self.date_of_birth

    def __post_init__(self):
        self.client_id = self.first_name[0] + self.last_name[0] + str(date.today().year)[-2:] + str(random.randrange(100, 999))
        self._coupon = []
    
    def purchase_coupon(self, coupon: Coupon):
        self._coupon.append(coupon)

    def list_coupon(self):
        return self._coupon


def main():
    client = Client('Ebenezer', '', 'Ofori-Mensah', 'Male', date(1995,8,5), '', email_address='quameophory@yahoo.com')
    # print(client.client_id)
    # print(client)
    coupon = Coupon()
    coupon.set_coupon_amount(1000.00)
    client.purchase_coupon(coupon)
    print(client.list_coupon())
    print(client.client_age())

if __name__ == '__main__':
    main()