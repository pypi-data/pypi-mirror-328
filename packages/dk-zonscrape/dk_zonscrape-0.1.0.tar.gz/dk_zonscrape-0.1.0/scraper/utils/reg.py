import re
def extract_numbers(input_string)->int:
    # Remove all non-numeric characters and convert to integer
    return int(re.sub(r'\D', '', input_string))


def filter_unicode(input_string)->str:
    return input_string.encode('ascii', 'ignore').decode()

def extract_text(text: str) -> str:
    """
    Filters out unicode characters and extra whitespace, returning clean text.
    Example: 'Product Dimensions\u200f:\u200e' -> 'Product Dimensions'
    """
    # Remove unicode characters and clean up whitespace
    cleaned = re.sub(r'[\u200e\u200f\n\t:]', '', text)
    # Remove multiple spaces and strip
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned