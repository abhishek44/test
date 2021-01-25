from datetime import datetime

from cardvalidator import luhn


class ValidateCard():
    def __init__(self):
        pass

    def verify_card_details(self, card_details):

        card_number = card_details['CreditCardNumber']
        card_holder = card_details['CardHolder']
        expiry_date = card_details['ExpirationDate']
        cvv_number = card_details['SecurityCode']
        amount = card_details['Amount']

        # Validate card number
        if card_number and card_number.isdigit():
            # validate card number using Luhn algorithm
            if not luhn.is_valid(card_number):
                print('Invalid card number')
                return False
        else:
            print('Invalid card number')
            return False

            # Check for card name if empty
        # print('verify card data name')
        if card_holder is None:
            print('Invalid card holder name')
            return False

        # Check for cvv is a number
        print('verify card security number')
        if cvv_number is not None:
            try:
                if len(cvv_number) == 3:
                    int(cvv_number)
                else:
                    return False
            except:
                print('security code is invalid')
                return False

        # Check for expiry date and validate with today's date
        # print('verify card expiry date')
        if expiry_date is not None:
            date = expiry_date.split('/')
            month = int(date[0])
            year = int(date[1])

            current_date = datetime.today()

            if year >= current_date.year:
                if month < current_date.month:
                    print('card is expired')
                    return False
            else:
                print('card is expired')
                return False
        else:
            print('Invalid card expiry date')
            return False

        # print('Verify Amount')
        if amount is not None:
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Amount Should be greater than zero")
                    return False
            except ValueError:
                print("Invalid amount")
        else:
            return False

        return True, amount
