import re
from typing import Optional

regext_digit_pattern = re.compile(r"\d+(?:\.\d+)?")

def extract_quantity_from_string(text: str) -> Optional[int]:
    digit_match = regext_digit_pattern.search(text)

    if digit_match:
        return int(float(digit_match.group()))

    return None
