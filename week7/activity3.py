from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):
    """Abstract payment type that all concrete payment methods inherit from."""
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class CryptoPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} via Cryptocurrency"

class GooglePayPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} via Google Pay"


# Factory 
class PaymentFactory:
    """
    Factory that dynamically creates the correct payment method object
    based on a string key.
    """
    _processors = {
        "paypal": PayPalPayment,
        "creditcard": CreditCardPayment,
        "cryptopayment": CryptoPayment,
        "googlepay": GooglePayPayment
    }

    @classmethod
    def create_processor(cls, payment_method: str) -> Payment:
        processor_class = cls._processors.get(payment_method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment method: {payment_method}")
        return processor_class()


# Singleton 
class PaymentGateway:
    """
    Singleton that represents the single point of access to the payment system.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def checkout(self, payment_method: str, amount: float) -> str:
        processor = PaymentFactory.create_processor(payment_method)
        return processor.process_payment(amount)


if __name__ == "__main__":
    gateway1 = PaymentGateway()
    gateway2 = PaymentGateway()

    print(gateway1.checkout("PayPal", 100))
    print(gateway1.checkout("GooglePay", 200))

    # Check Singleton behaviour
    print("Both gateway variables point to same object:", gateway1 is gateway2)
