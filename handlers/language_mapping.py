
LANGUAGE_MAPPING = {
    "af": "Afrikaans",
    "ar": "Arabic (non-diacriticized words)",
    "ar-tashkeel": "Arabic (diacriticized words)",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "br": "Breton",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en-gb": "English (GB)",
    "en-us": "English (US)",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "gl": "Galician",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ka": "Georgian",
    "kk": "Kazakh",
    "ko": "Korean",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "ms": "Malay",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sq": "Albanian",
    "sr": "Serbian",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "tl": "Tagalog",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese"
}

def get_language_code(language_input):
    if language_input in LANGUAGE_MAPPING:
        return language_input
    for code, name in LANGUAGE_MAPPING.items():
        if language_input.lower() == name.lower():
            return code
    return None

def is_supported_language(language_input):
    return get_language_code(language_input) is not None

def get_supported_languages_info():
    message = (
        "The tool supports the following languages. "
        "Please use the corresponding language codes or full names listed below when specifying the language in your input:\n\n"
        "Language Code : Language Name\n"
        "------------------------------\n"
    )
    for code, language in LANGUAGE_MAPPING.items():
        message += f"  {code:<12}: {language}\n"
    message += (
        "\nFor example, to analyze words in Spanish, use either 'es' or 'Spanish'. "
        "Make sure to input the code or name exactly as listed, including any hyphens."
    )
    return message