from clients import Client, Coupon
from vehicles import Vehicle
from datetime import date

def main():
    client = Client('Ebenezer', '', 'Ofori-Mensah', 'Male', date(1995,8,5), '', email_address='quameophory@yahoo.com')
    # print(client.client_id)
    # print(client)
    coupon = Coupon()
    camry = Vehicle('Toyota', 'Camry 2022', 'GE-2988-22', client)
    coupon.set_coupon_amount(1000.00)
    client.purchase_coupon(coupon)
    print(client.list_coupon())
    print(camry.registration_number)

if __name__ == '__main__':
    main()