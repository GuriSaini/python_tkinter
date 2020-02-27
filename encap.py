class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def make_a_call(self,phone_number):
        print(f"Calling{phone_number}")
    def full_name(self):
        return f"{self.brand} {self.model}"
    def send_message(self):
        pass