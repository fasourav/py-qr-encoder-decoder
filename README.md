
# QR Code Generator & Decoder Web App

This is a simple web application built using Python and Flask to generate and decode QR codes. Users can input data to generate a QR code and upload QR code images to decode them. The app provides error handling and displays relevant messages for different actions. 

## Features

- **Generate QR Codes**: Enter any text or data, and the app will generate a corresponding QR code.
- **Decode QR Codes**: Upload an image of a QR code, and the app will decode the embedded data.
- **User-Friendly Interface**: A professional, easy-to-use interface with instant feedback for users.

## Prerequisites

Before you can run the project, make sure the following are installed on your system:

- **Python 3.x** (version 3.12 or later recommended)
- **Flask** web framework
- **qrcode** library (for generating QR codes)
- **pyzbar** and **Pillow** libraries (for decoding QR codes)
- **zbar** shared library (for decoding QR codes)

## Installation

### Step 1: Clone the Repository

First, clone this repository to your local machine using:

```bash
git clone https://github.com/your-repo/qr-code-app.git
cd qr-code-app
```

### Step 2: Set Up a Virtual Environment

Create a virtual environment to isolate the project’s dependencies:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **For Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```
- **For Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

### Step 3: Install Required Python Packages

Once inside the virtual environment, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file yet, you can create it by adding the following content:

```text
Flask
qrcode[pil]
opencv-python
pyzbar
Pillow
```

### Step 4: Install zbar Library (for QR Code Decoding)

To decode QR codes, you need to install the **zbar** library on your system. For Ubuntu/Debian-based systems, run:

```bash
sudo apt install libzbar0
```

For other platforms, refer to your package manager or the official zbar documentation.

### Step 5: Run the Application

Now, you can start the Flask app:

```bash
python app.py
```

You should see output similar to this:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure

```
/qr_web_app
    /static
        /qr_images    # Folder to store generated QR codes
        /styles.css   # CSS for styling the application
    /templates
        index.html    # HTML template for the web interface
    app.py            # Main Flask app
    README.md         # Project readme file
```

## Usage

### Generate QR Code

1. On the homepage, enter the data you want to encode in the text field.
2. Click the "Generate QR Code" button to generate the QR code.
3. The QR code will be displayed and available for download.

### Decode QR Code

1. On the homepage, upload an image of a QR code.
2. Click the "Decode QR Code" button.
3. The decoded data will be displayed on the page.

## Troubleshooting

If you encounter any errors:

- Ensure you have all the necessary dependencies installed.
- Make sure you installed `libzbar0` to decode QR codes.
- Activate the virtual environment using `source venv/bin/activate` (or `.env\Scriptsctivate` for Windows).

If you're still facing issues, try restarting the app or checking error logs in the terminal for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with any improvements or suggestions.

---

Thank you for using this QR Code Generator & Decoder app! Feel free to contact me for further support or questions.
