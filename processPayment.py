import ast

from gateway import ExternalPayment
from validate import ValidateCard


class Payment:
    def __init__(self):
        pass

    def process_payment(self, data):
        if not str(data.decode('utf-8')) == '':
            dict_payment_param = ast.literal_eval(str(data.decode('utf-8')))
        else:
            return False

        card_data = ValidateCard()
        print('verify card data')
        try:
            status , amount = card_data.verify_card_details(dict_payment_param)
            if not status:
                print("card data invalid")
                return False
        except:
            print('verification of card data failed')
            return False

        try:
            # payment procedure begins
            print("payment status started")
            payment_status = ExternalPayment(amount, dict_payment_param)

            print("payment process started")
            payment_success = payment_status.make_payment()
            # checking the transaction status, if it is successful or not.
            if payment_success:
                return {"status code": 200}, 200
            else:
                return False
        except:
            return False
