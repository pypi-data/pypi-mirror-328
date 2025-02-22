def to_upper(text):
    """Преобразует текст в верхний регистр."""
    return text.upper()

def to_lower(text):
    """Преобразует текст в нижний регистр."""
    return text.lower()

def remove_extra_spaces(text):
    """Удаляет лишние пробелы из текста."""
    return ' '.join(text.split())

def reverse_text(text):
    """Переворачивает строку."""
    return text[::-1]

def replace_substring(text, old, new):
    """Заменяет подстроку в тексте."""
    return text.replace(old, new)
