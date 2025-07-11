# ============================================================================
# MULTILINGUAL TEXT TO SPEECH WITH gTTS
# ============================================================================
# Uses Google Text-to-Speech (gTTS) with support for 100+ languages
# Requires: pip install gtts pygame
# Note: Requires internet connection for gTTS to work
# ============================================================================

import io
from gtts import gTTS
from gtts.lang import tts_langs
import pygame
import sys


def show_available_languages():
    """
    Display all available languages supported by gTTS
    """
    print("\n=== Available Languages ===")
    langs = tts_langs()
    for code, name in sorted(langs.items()):
        print(f"{code}: {name}")
    print(f"\nTotal languages supported: {len(langs)}")
    print("=" * 50)


def speak_with_gtts(text, lang='en'):
    """
    Convert text to speech using Google Text-to-Speech

    Args:
        text (str): Text to be spoken
        lang (str): Language code (default: 'en' for English)
                   Common codes: 'en' (English), 'es' (Spanish), 'fr' (French),
                   'de' (German), 'it' (Italian), 'pt' (Portuguese), 'ru' (Russian),
                   'ja' (Japanese), 'ko' (Korean), 'zh' (Chinese), 'ar' (Arabic)
    """
    try:
        print(f"Speaking in {lang}: '{text}'")

        # Validate language code
        available_langs = tts_langs()
        if lang not in available_langs:
            print(f"Language '{lang}' not supported!")
            print("Use 'languages' command to see available languages")
            return False

        # Create gTTS object
        tts = gTTS(text=text, lang=lang, slow=False)

        # Save to BytesIO object (in-memory file)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)  # Reset file pointer to beginning

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

        # Load and play the audio
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print("Speech completed!")

    except Exception as e:
        print(f"Error during speech synthesis: {e}")
        return False

    return True


def main():
    """
    Main function to handle user input and text-to-speech conversion
    """
    print("=== Multilingual Text-to-Speech with gTTS ===")
    print("Commands:")
    print("  'quit' or 'exit' - Stop the program")
    print("  'languages' - Show all available languages")
    print("  'lang:XX text' - Speak text in language XX (e.g., 'lang:es Hola mundo')")
    print("  'text' - Speak text in English (default)")
    print("Note: Requires internet connection\n")

    current_lang = 'en'  # Default language

    while True:
        try:
            # Get user input
            user_input = input(f"[{current_lang}] Enter text to speak: ").strip()

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            # Show available languages
            if user_input.lower() == 'languages':
                show_available_languages()
                continue

            # Check for language change command
            if user_input.startswith('lang:'):
                try:
                    parts = user_input.split(' ', 1)
                    lang_code = parts[0].split(':')[1].lower()

                    if len(parts) > 1:
                        text_to_speak = parts[1]
                        success = speak_with_gtts(text_to_speak, lang_code)
                    else:
                        print("Please provide text after the language code")
                        print("Example: lang:es Hola mundo")
                        continue

                except IndexError:
                    print("Invalid language command format")
                    print("Use: lang:XX text (e.g., lang:es Hola mundo)")
                    continue
            else:
                # Skip empty input
                if not user_input:
                    print("Please enter some text!")
                    continue

                # Convert text to speech using current language
                success = speak_with_gtts(user_input, current_lang)

            if not success:
                print("Failed to convert text to speech. Please try again.")

            print()  # Add blank line for readability

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue


# ============================================================================
# MULTILINGUAL EXAMPLES
# ============================================================================
def multilingual_demo():
    """
    Demonstrate text-to-speech in multiple languages
    """
    examples = [
        ("en", "Hello, this is English"),
        ("es", "Hola, esto es español"),
        ("fr", "Bonjour, c'est du français"),
        ("de", "Hallo, das ist Deutsch"),
        ("it", "Ciao, questo è italiano"),
        ("pt", "Olá, isto é português"),
        ("ru", "Привет, это русский"),
        ("ja", "こんにちは、これは日本語です"),
        ("ko", "안녕하세요, 이것은 한국어입니다"),
        ("zh", "你好，这是中文"),
        ("ar", "مرحبا، هذه هي اللغة العربية"),
    ]

    print("=== Multilingual Demo ===")
    print("Playing examples in different languages...")

    for lang, text in examples:
        print(f"\n{lang.upper()}: {text}")
        input("Press Enter to hear this language...")
        speak_with_gtts(text, lang)

    print("\nDemo completed!")


# ============================================================================
# QUICK TEST FUNCTION
# ============================================================================
def quick_test():
    """
    Quick test with predefined text - useful for initial testing
    """
    test_text = "Hello you wonderful human being!"
    print("Running quick test...")
    speak_with_gtts(test_text)


if __name__ == "__main__":
    # Uncomment the next line to run a quick test first
    # quick_test()

    # Uncomment the next line to run the multilingual demo
    # multilingual_demo()

    # Run the interactive version
    main()
