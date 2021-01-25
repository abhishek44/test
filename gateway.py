class BasePaymentGateway:
    def __init__(self, repeat = 0, backup_gateway=None):
        self.repeat = repeat
        self.gateway = None
        self.backup_gateway = backup_gateway

    def connect_to_gateway(self, gateway = None, details = None):
        if gateway is not None:
            if self.authenticate_user(details):
                return True
        return False

    def authenticate_user(self, details = None):
        if details is not None:
            return True
        return False

    def pay(self, amount, user_details = None, gateway = None):
        if gateway is None:
            gateway = self.gateway

        while self.repeat + 1 > 0:
            if self.connect_to_gateway(gateway, user_details):
                print("Payment of {} done successfully using {}".format(amount, self.gateway))
                return True
            if gateway == 'ExpensiveBasePaymentGateway' and self.repeat == 1:
                if self.connect_to_gateway(gateway, user_details):
                    if self.backup_gateway is not None:
                        print("Payment of {} done successfully using {}".format(amount, self.backup_gateway))
                        return True
                    return False
            else:
                return False
            self.repeat -= 1
        return False


class PremiumBasePaymentGateway(BasePaymentGateway):
    def __init__(self, repeat = 3):
        super(PremiumBasePaymentGateway, self).__init__(repeat, None)
        self.gateway = "PremiumBasePaymentGateway"

    def __repr__(self):
        return "<PremiumBasePaymentGateway>"


class ExpensiveBasePaymentGateway(BasePaymentGateway):
    def __init__(self, repeat = 1):
        super(ExpensiveBasePaymentGateway, self).__init__(repeat, 'CheapBasePaymentGateway')
        self.gateway = "ExpensiveBasePaymentGateway"

    def __repr__(self):
        return "<ExpensiveBasePaymentGateway>"


class CheapBasePaymentGateway(BasePaymentGateway):
    def __init__(self, repeat = 0):
        super(CheapBasePaymentGateway, self).__init__(repeat, None)
        self.gateway = "CheapBasePaymentGateway"

    def __repr__(self):
        return "<CheapBasePaymentGateway>"


class ExternalPayment:
    def __init__(self, amount, card_details = None):
        self.amount = amount
        self.card_details = card_details

    def make_payment(self):
        try:
            payment_mode = None
            if self.amount <= 20:
                # print("Cheap payment")
                payment_mode = CheapBasePaymentGateway()
            elif 20 < self.amount <= 500:
                # print("Expensive payment")
                payment_mode = ExpensiveBasePaymentGateway()
            elif self.amount > 500:
                # print("Premium payment")
                payment_mode = PremiumBasePaymentGateway()
            else:
                return False

            status = payment_mode.pay(self.amount, self.card_details)
            return status
        except:
            return False
