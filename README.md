# Regex data extraction script

This project demonstrates how to use Python's `re` module (regular expressions) to extract various types of structured data from a block of text.

##  Features

- Extracts:
  - Email addresses
  - URLs
  - HTML tags
  - Phone numbers
  - Credit card numbers
  - Currency values
  - Time formats

##  Project Structure

```bash
.
├── regex_data_extractor.py  # Main script with patterns, sample data, and function
├── README.md                # This file


---

##  How It Works

The script contains:

  1.Regex patterns stored in a dictionary.

  2.Sample data simulating real-world text input.

  3.A function that loops through patterns, finds all matches and prints them


##  Setup and run instructions

 1.Clone the repository

```bash

git clone https://github.com/Kellia855/alu_regex-data-extraction-Kellia855.git
cd alu_regex-data-extraction-Kellia855

2.Run the script

```bash

python regex_data_extractor.py


## Sample output

 When you run the script, you’ll see output like this:

 EMAIL matches:
- user@example.com
- firstname.lastname@company.co.uk

...

URL matches:
- https://www.example.com
- https://subdomain.example.org/page

...

HTML TAGS matches:
- ('', '')
- (' class="example"', '="example"')
- (' alt="description"', '="description"')

...

PHONE matches:
- 123-456-7890
- 123.456.7890

...

CREDIT_CARD matches:
- 1234 5678 9012 3456
- 1234-5678-9012-3456

...

CURRENCY matches:
- $19.99
- $1,234.56

...

TIME matches:
- 14:30 PM
- 02:59


---

AUTHOR:
Kellia Kamikazi