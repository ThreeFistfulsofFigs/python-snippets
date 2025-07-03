# ============================================================================
# CAPTCHA IMAGE GENERATOR
# ============================================================================
# A simple script to generate visual CAPTCHA images from user-provided text.
# Creates distorted text images that can be used for bot prevention and
# human verification in web applications or security systems.
# ============================================================================

# Import required libraries
from captcha.image import ImageCaptcha  # For generating CAPTCHA images


# ============================================================================
# CAPTCHA CONFIGURATION CONSTANTS
# ============================================================================
# Define standard CAPTCHA image dimensions
CAPTCHA_WIDTH = 300   # Image width in pixels
CAPTCHA_HEIGHT = 100  # Image height in pixels
OUTPUT_FILENAME = 'CAPTCHA1.png'  # Default output file name


# ============================================================================
# CAPTCHA GENERATOR SETUP
# ============================================================================
def create_captcha_generator() -> ImageCaptcha:
    """
    Creates and configures a CAPTCHA image generator with specified dimensions.

    Returns:
        ImageCaptcha: Configured CAPTCHA generator instance with predefined size.
    """
    # CAPTCHA INSTANCE CREATION
    # Initialize ImageCaptcha with custom dimensions
    # Width and height determine the size of the generated CAPTCHA image
    image_generator = ImageCaptcha(width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT)

    return image_generator


# ============================================================================
# USER INPUT HANDLING
# ============================================================================
def get_captcha_text() -> str:
    """
    Prompts the user to enter text that will be converted into a CAPTCHA image.

    Returns:
        str: The text string to be rendered as a CAPTCHA image.
    """
    # TEXT INPUT PROMPT
    # Get user input for the text to be displayed in the CAPTCHA
    # This text will be distorted and styled to create the visual challenge
    captcha_text = input("Enter captcha text: ")

    # INPUT VALIDATION
    # Strip whitespace to clean the input
    captcha_text = captcha_text.strip()

    return captcha_text


# ============================================================================
# CAPTCHA IMAGE GENERATION
# ============================================================================
def generate_captcha_image(generator: ImageCaptcha, text: str) -> bytes:
    """
    Generates CAPTCHA image data from the provided text.

    Args:
        generator (ImageCaptcha): The configured CAPTCHA generator instance.
        text (str): The text to be rendered as a CAPTCHA image.

    Returns:
        bytes: The generated image data in binary format.
    """
    # IMAGE DATA GENERATION
    # Generate the CAPTCHA image as binary data
    # The generator applies distortion, styling, and visual effects
    # to make the text challenging for automated systems to read
    image_data = generator.generate(text)

    return image_data


# ============================================================================
# FILE OPERATIONS - SAVE FUNCTIONALITY
# ============================================================================
def save_captcha_image(generator: ImageCaptcha, text: str, filename: str) -> None:
    """
    Saves the generated CAPTCHA image to a file on disk.

    Args:
        generator (ImageCaptcha): The configured CAPTCHA generator instance.
        text (str): The text used to generate the CAPTCHA.
        filename (str): The filename where the image will be saved.

    Raises:
        IOError: If there is an error writing the image file.
    """
    try:
        # FILE WRITING OPERATION
        # Write the CAPTCHA image directly to file
        # The generator handles image encoding and file format
        generator.write(text, filename)

        # SUCCESS CONFIRMATION
        print(f"CAPTCHA image saved successfully as: {filename}")

    # ERROR HANDLING
    except IOError as e:
        print(f"Error saving CAPTCHA image: {e}")
        raise


# ============================================================================
# IMAGE DISPLAY FUNCTIONALITY
# ============================================================================
def display_captcha_image(generator: ImageCaptcha, filename: str) -> None:
    """
    Opens and displays the generated CAPTCHA image using the default system viewer.

    Args:
        generator (ImageCaptcha): The CAPTCHA generator instance.
        filename (str): The filename of the image to display.

    Raises:
        FileNotFoundError: If the specified image file does not exist.
        OSError: If there is an error opening the image file.
    """
    try:
        # IMAGE DISPLAY OPERATION
        # Open the saved CAPTCHA image using system default image viewer
        # This allows immediate visual verification of the generated CAPTCHA
        generator.open(filename)

        # SUCCESS CONFIRMATION
        print(f"CAPTCHA image opened: {filename}")

    # ERROR HANDLING
    except FileNotFoundError:
        print(f"Error: CAPTCHA image file '{filename}' not found.")
        raise
    except OSError as e:
        print(f"Error opening CAPTCHA image: {e}")
        raise


# ============================================================================
# MAIN PROGRAM LOGIC
# ============================================================================
def main() -> None:
    """
    Main function to orchestrate the CAPTCHA generation process.

    Handles the complete workflow from user input to image generation,
    saving, and display with comprehensive error handling.
    """
    try:
        # GENERATOR INITIALIZATION
        # Create the CAPTCHA generator with predefined settings
        captcha_generator = create_captcha_generator()

        # USER INPUT COLLECTION
        # Get the text that will be converted to CAPTCHA image
        user_text = get_captcha_text()

        # INPUT VALIDATION
        if not user_text:
            print("Error: No text provided. Please enter text for the CAPTCHA.")
            return

        # IMAGE GENERATION
        # Generate the CAPTCHA image data from user text
        image_data = generate_captcha_image(captcha_generator, user_text)

        # FILE SAVING OPERATION
        # Save the generated CAPTCHA image to disk
        save_captcha_image(captcha_generator, user_text, OUTPUT_FILENAME)

        # IMAGE DISPLAY
        # Open the saved image for immediate viewing
        display_captcha_image(captcha_generator, OUTPUT_FILENAME)

    # COMPREHENSIVE ERROR HANDLING
    except KeyboardInterrupt:
        print("\nCAPTCHA generation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error during CAPTCHA generation: {e}")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    # Execute main function only when script is run directly
    # (not when imported as a module)
    main()
