##########################################################################################
# QR Code Generator with Random Background Color
#
# Description: This script creates a QR code from user-provided data (filename or URL) 
# and saves it as a PNG image with a random RGB background color. The QR code is 
# displayed upon generation.
#
# Dependencies: 
#   - qrcode: Library for generating QR codes
#   - random: Library for generating random numbers
#
# Usage: Run the script, input a filename or data string when prompted, and the script 
# will generate and save a QR code as a PNG file with the provided name.
#
##########################################################################################

import qrcode
import random

# Prompt user for input data (e.g., filename or URL to encode in the QR code)
data = input("Enter the name of the file to save a QR code:  ")

# Initialize QRCode object with specified settings
# - version=1: QR code version (size of the QR code)
# - error_correction=ERROR_CORRECT_L: Low error correction level (~7% data recovery)
# - box_size=10: Size of each QR code module (pixels)
# - border=4: Border thickness around the QR code (in modules)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add user-provided data to the QR code
qr.add_data(data)
# Generate the QR code, automatically fitting the data to the version
qr.make(fit=True)

# Generate a random RGB color tuple for the background
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Create the QR code image with black foreground and random background color
img = qr.make_image(fill_color='black', back_color=random_color)

# Save the generated QR code as a PNG file using the user-provided filename
img.save(f"{data}.png")
# Display the generated QR code image
img.show()

##########################################################################################
# Notes:
# - Ensure the 'qrcode' and 'Pillow' (PIL) libraries are installed (`pip install qrcode pillow`).
# - The generated QR code is saved as '[data].png' in the current working directory.
# - The random background color is an RGB tuple with values between 0 and 255 for each channel.
# - The QR code uses low error correction (ERROR_CORRECT_L) for simplicity; other options 
#   include ERROR_CORRECT_M, ERROR_CORRECT_Q, or ERROR_CORRECT_H for higher correction levels.
##########################################################################################
