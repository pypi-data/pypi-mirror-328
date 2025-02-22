from .translator import TranslatorLib

# Tạo một đối tượng TranslatorLib để sử dụng chung
_translator = TranslatorLib()

# Định nghĩa hàm translate để có thể gọi trực tiếp translib.translate()
def translate(text: str, target_language: str) -> str:
    return _translator.translate(text, target_language)

