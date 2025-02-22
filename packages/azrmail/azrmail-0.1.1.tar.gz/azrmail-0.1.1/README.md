# AZRMail API Wrapper

AZRMail is a simple Python wrapper for interacting with the AZRMail API, allowing users to generate temporary email addresses and fetch received emails effortlessly.

## Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install azrmail
```

## Usage

Below is an example demonstrating how to use the AZRMail API wrapper in Python:

```python
from azrmail import Email

# Initialize Email API with your API key
mail = Email(api_key="API_KEY")

# Generate a temporary email address
email, inboxId = mail.generate()

# Retrieve emails from the generated inbox ID
emails = Email.getmail("inboxId")

# Print generated email and inbox ID
print(email, inboxId)

# Print received emails
print(emails)
```

## Features
- Generate temporary email addresses
- Retrieve received emails from a specific inbox

## API Reference

### `Email(api_key: str)`
Initializes the email API wrapper with your provided API key.

### `generate()`
Generates a new temporary email address and returns the email and `inboxId`.

### `getmail(inboxId: str)`
Retrieves all received emails from the specified inbox ID.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues or contribute by submitting pull requests!

