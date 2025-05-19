import re

# Define regex patterns
patterns = {
         "email": r"\b[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9.-]+\.)[a-zA-Z]{2,}\b",
         "url": r"https?://[^\s/$.?#].[^\s]*",
         "HTML tags": r"<[a-zA-Z][a-zA-Z0-9]*(\s+[a-zA-Z_:][-a-zA-Z0-9_:.]*(\s*=\s*\"[^\"]*\")?)*\s*/?>",
         "phone":  r"\b(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b",
         "credit_card": r"\b(?:\d{4}[-.\s]?){3}\d{4}\b",
         "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
         "time": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b"

}


