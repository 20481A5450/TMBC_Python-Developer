import re

def is_valid_phone(phone):
    pattern = re.compile(r"^\+\d{10,15}$")
    return pattern.match(phone)
