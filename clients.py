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
class Person:
    first_name: str
    middle_name: str
    last_name: str
    gender: str
    date_of_birth: date
    mobile_number: str
    email_address: str = field(default='')

    def get_age(self):
        return date.today() - self.date_of_birth

@dataclass
class Client(Person):

    GENDER = ('Male', 'Female', 'Other')
    first_name: str
    middle_name: str
    last_name: str
    gender: str
    date_of_birth: date
    mobile_number: str
    email_address: str = field(default='')
    

    def __post_init__(self):
        super().__init__(self.first_name, self.middle_name, self.last_name, self.gender, self.date_of_birth, self.mobile_number, self.email_address)
        self.client_id = self.first_name[0] + self.last_name[0] + str(date.today().year)[-2:] + str(random.randrange(100, 999))
        self._coupon = []
    
    def purchase_coupon(self, coupon: Coupon):
        self._coupon.append(coupon)

    def list_coupon(self):
        return self._coupon

@dataclass
class Staff(Person):
    first_name: str
    middle_name: str
    last_name: str
    gender: str
    date_of_birth: date
    mobile_number: str
    email_address: str = field(default='')

    def __post_init__(self):
        super().__init__(self.first_name, self.middle_name, self.last_name, self.gender, self.date_of_birth, self.mobile_number, self.email_address)
