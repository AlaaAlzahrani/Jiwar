
LANGUAGE_MAPPING = {
    "af": "Afrikaans",
    "am": "Amharic",
    "an": "Aragonese",
    "ar": "Arabic",
    "as": "Assamese",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bpy": "Bishnupriya Manipuri",
    "bs": "Bosnian",
    "ca": "Catalan",
    "chr": "Cherokee",
    "cmn": "Mandarin Chinese",
    "cs": "Czech",
    "cv": "Chuvash",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "en-029": "Caribbean English",
    "en-gb": "British English",
    "en-gb-scotland": "Scottish English",
    "en-gb-x-gbclan": "Lancastrian English",
    "en-gb-x-gbcwmd": "West Midlands English",
    "en-gb-x-rp": "Received Pronunciation English",
    "en-us": "American English",
    "eo": "Esperanto",
    "es": "Spanish",
    "es-419": "Latin American Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fa-latn": "Persian (Latin script)",
    "fi": "Finnish",
    "fr": "French",
    "fr-be": "Belgian French",
    "fr-ch": "Swiss French",
    "ga": "Irish Gaelic",
    "gd": "Scottish Gaelic",
    "gn": "Guarani",
    "grc": "Ancient Greek",
    "gu": "Gujarati",
    "hak": "Hakka Chinese",
    "haw": "Hawaiian",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "ht": "Haitian Creole",
    "hu": "Hungarian",
    "hy": "Armenian",
    "hyw": "Western Armenian",
    "ia": "Interlingua",
    "id": "Indonesian",
    "io": "Ido",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jbo": "Lojban",
    "ka": "Georgian",
    "kk": "Kazakh",
    "kl": "Greenlandic",
    "kn": "Kannada",
    "ko": "Korean",
    "kok": "Konkani",
    "ku": "Kurdish",
    "ky": "Kyrgyz",
    "la": "Latin",
    "lb": "Luxembourgish",
    "lfn": "Lingua Franca Nova",
    "lt": "Lithuanian",
    "ltg": "Latgalian",
    "lv": "Latvian",
    "mi": "Maori",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "nci": "Classical Nahuatl",
    "ne": "Nepali",
    "nl": "Dutch",
    "nb": "Norwegian Bokmål",
    "nog": "Nogai",
    "om": "Oromo",
    "or": "Oriya",
    "pa": "Punjabi",
    "pap": "Papiamento",
    "piqd": "Klingon",
    "pl": "Polish",
    "pt": "Portuguese",
    "pt-br": "Brazilian Portuguese",
    "qdb": "Lang Belta",
    "qu": "Quechua",
    "quc": "K'iche'",
    "qya": "Quenya",
    "ro": "Romanian",
    "ru": "Russian",
    "ru-lv": "Latvian Russian",
    "sd": "Sindhi",
    "shn": "Shan",
    "si": "Sinhala",
    "sjn": "Sindarin",
    "sk": "Slovak",
    "sl": "Slovenian",
    "smj": "Lule Sami",
    "sq": "Albanian",
    "sr": "Serbian",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tk": "Turkmen",
    "tl": "Tagalog",
    "tn": "Setswana",
    "tr": "Turkish",
    "tt": "Tatar",
    "ug": "Uyghur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "vi-vn-x-central": "Central Vietnamese",
    "vi-vn-x-south": "Southern Vietnamese",
    "yue": "Cantonese"
}


def get_language_code(language_input):
    language_input = language_input.lower()
    if language_input in LANGUAGE_MAPPING:
        return language_input
    for code, name in LANGUAGE_MAPPING.items():
        if language_input == name.lower():
            return code
    return None


def is_supported_language(language_input):
    return get_language_code(language_input) is not None


def get_supported_languages_info():
    message = (
        "The tool supports the following languages and variants. "
        "Please use the corresponding language codes or full names listed below when specifying the language in your input:\n\n"
        "Language Code         : Language Name\n"
        "---------------------------------------\n"
    )
    for code, language in LANGUAGE_MAPPING.items():
        message += f"  {code:<20}: {language}\n"
    message += (
        "\nFor example, to analyze words in American English, use either 'en-us' or 'American English'. "
        "Make sure to input the code or name exactly as listed, including any hyphens or regional specifiers."
    )
    return message