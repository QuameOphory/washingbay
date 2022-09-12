from clients import Client, Coupon
from vehicles import Vehicle
from datetime import date

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