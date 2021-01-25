from flask import Flask, request, abort
from flask_api import status

from processPayment import Payment

app = Flask(__name__)


@app.route('/')
def display_home():
    return 'If you see this message. The flask service is working.'


@app.route('/ProcessPayment/', methods = ['GET', 'POST'])
def payment():
    # proceed with payment
    data = request.data if str(request.method).lower() == 'post' else ''
    print(data)
    if not data:
        abort(400)
    result = Payment().process_payment(data)
    if not result:
        return "Record not found", status.HTTP_400_BAD_REQUEST
    else:
        return "Payment is processed"


if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 8081)
