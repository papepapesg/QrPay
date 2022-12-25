from flask import Flask, request
from pyqrcode import QRCode

app = Flask(__name__)

@app.route('/generate-qr-code', methods=['POST'])
def generate_qr_code():
    # Parse the request parameters
    merchant_id = request.form['merchantID']
    trx_id = request.form['trxID']
    products = request.form['products']

    # Generate the QR code data string
    data = f"Merchant ID: {merchant_id}\nTransaction ID: {trx_id}\n"
    for product in products:
        data += f"{product['name']}: {product['price']}\n"

    # Generate the QR code
    qr = QRCode(data)
    qr.png('qr_code.png', scale=8)

    # Return the QR code image
    with open('qr_code.png', 'rb') as f:
        image = f.read()
    return image, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run()
To test the API, you can use a tool like cURL or Postman to send a POST request to the /generate-qr-code endpoint with the following form data:

Copy code
merchantID: 12345
trxID: 67890
products[0][name]: Product 1
products[0][price]: 10.00
products[1][name]: Product 2
products[1][price]: 5.00
This will generate a QR code image with the following data encoded:

Copy code
Merchant ID: 12345
Transaction ID: 67890
Product 1: 10.00
Product 2: 5.00



