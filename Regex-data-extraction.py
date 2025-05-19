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

# Sample data to test the regex patterns
sample_data = """
Email: user@example.com
Another Email: firstname.lastname@company.co.uk
Website: https://www.example.com
Subdomain URL: https://subdomain.example.org/page
HTML tag1:<p>
HTML tag2:<div class="example">
HTML tag3:<img src="image.jpg" alt="description">
Phone1: (123) 456-7890
Phone2: 123-456-7890
Phone3: 123.456.7890
Price: $19.99 and $1,234.56
Card1: 1234 5678 9012 3456
Card2: 1234-5678-9012-3456
time1: 14:30 PM
time2: 02:59
"""


#Define a function to extract and print data using regex

def extract_data(pattern,text):
    for label, regex in patterns.items():
        matches = re.findall(regex, text)
        print(f"\n{label.upper()} matches:")
        if matches:
            for match in matches:
                print("-", match)
        else:
            print("No matches found.")


# Run the function with the sample data
extract_data(patterns, sample_data)
