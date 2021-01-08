class Phone():
    """This is a phone class that can be used for inheritance purposes"""
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"this phone belongs to {self.phone_number}"

    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f'Sending text to {other_number}')
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")

class Android(Phone):
    def __init__(self, phone_number, color ):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unclocked')

    def view_battery_life(self):
        print(f"Battery life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

frank_phone = Android('888-777-3333', 'black')

frank_phone.view_battery_life()
frank_phone.charge_phone(40)
frank_phone.view_battery_life()
frank_phone.view_phone_number()
frank_phone.call('859-699-0000')
frank_phone.open_app('Zoom')

class Iphone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.faceid = None
        self.apple_pay = 1000

    def __str__(self):
        return f"iphone belongs to number {self.phone_number}"

    def set_faceid(self, faceid):
        self.faceid = faceid

    def unclock_iphone(self, faceid):
        if faceid == self.faceid:
            print('recognized iphone unlocked')

    def amount_left(self):
        print(f"Balance of account: {self.apple_pay}")

    def add_amount(self, add_money):
        self.apple_pay += add_money

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

user_phone = Iphone('999-999-9999', 'white')
user_phone.amount_left()

