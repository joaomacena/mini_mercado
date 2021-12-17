class PaymentMethodsNotAvailableException(Exception):
    def __init__(self):
        self.message = "This payment method is not available"
        super().__init__(self.message)


class PaymentMethodDiscountAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "Already exists a discount with this payment method"
        super().__init__(self.message)


class CouponCodeAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "this coupon code already exists"
        super().__init__(self.message)


class Admin_userAlereadyExistsEmailException(Exception):
    def __init__(self):
        self.message = 'This email is already being used'
        super().__init__(self.message)


class AddressAlereadyExistsCustomerException(Exception):
    def __init__(self):
        self.message = 'This Address is not used with this cUrtomer'
        super().__init__(self.message)
