import re

def extract_ip(message):
    if message:
        try:
            text = " ".join(message)
            match = re.search(r'\d+\.\d+\.\d+\.\d+', text)
            return match.group() if match else "Unknown"
        except:
            return "Unknown"
    return "Unknown"