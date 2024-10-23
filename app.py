from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Route to the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Generate QR Code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form.get('data', '').strip()

    if not data:
        flash("Error: No data provided to generate the QR code.", "danger")
        return redirect(url_for('index'))

    try:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate image
        img = qr.make_image(fill='black', back_color='white')

        # Save image
        img_path = os.path.join('static/qr_images', 'qr_code.png')
        img.save(img_path)

        return send_file(img_path, mimetype='image/png')

    except Exception as e:
        flash(f"Error generating QR Code: {str(e)}", "danger")
        return redirect(url_for('index'))

# Decode QR Code
@app.route('/decode_qr', methods=['POST'])
def decode_qr():
    if 'qr_image' not in request.files or request.files['qr_image'].filename == '':
        flash("Error: No file uploaded.", "danger")
        return redirect(url_for('index'))

    file = request.files['qr_image']
    
    try:
        img = Image.open(file)
        decoded_objects = decode(img)
        
        if decoded_objects:
            data = decoded_objects[0].data.decode("utf-8")
            flash(f"Decoded Data: {data}", "success")
        else:
            flash("Error: No QR code detected in the image.", "danger")
        
    except Exception as e:
        flash(f"Error decoding QR Code: {str(e)}", "danger")

    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ensure the static directory exists
    os.makedirs(os.path.join('static', 'qr_images'), exist_ok=True)
    app.run(debug=True)
