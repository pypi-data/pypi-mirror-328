# translib/translator.py
from googletrans import Translator

class TranslatorLib:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, dest_language="english"):
        """Translates text into the target language using language names."""
        language_map = {
            "english": "en",
            "french": "fr",
            "german": "de",
            "spanish": "es",
            "chinese": "zh-cn",
            "japanese": "ja",
            "korean": "ko",
            "vietnamese": "vi",
            "russian": "ru",
            "italian": "it",
            # Add more languages as needed
        }
        
        dest_lang_code = language_map.get(dest_language.lower(), "en")  # Default to English if not found
        try:
            translated = self.translator.translate(text, dest=dest_lang_code)
            return translated.text
        except Exception as e:
            return f"Translation error: {str(e)}"
