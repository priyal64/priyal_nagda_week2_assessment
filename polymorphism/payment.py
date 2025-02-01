# •	12. Write a `Payment` class with a method `process_payment()`. 
# Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` 
# that override the method differently.
# Base class Payment
class Payment:
    def process_payment(self, amount):
        print("Processing payment...")  

# Subclass for Credit Card Payment
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment of ${amount} made using Credit Card.")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment of ${amount} made using PayPal.")


class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment of ${amount} made using Bitcoin.")

amount = 100  

credit_card = CreditCardPayment()
credit_card.process_payment(amount)

paypal = PayPalPayment()
paypal.process_payment(amount)

bitcoin = BitcoinPayment()
bitcoin.process_payment(amount)
