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
