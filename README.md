# ERR0R Bomber

A multi-threaded SMS bomber script created for educational purposes, developed by ERR0R-V4U. This tool demonstrates how to send multiple HTTP requests concurrently with delays and progress feedback.

**Warning:** Use responsibly and legally. This tool should only be used for learning and testing with permission.

## Features

- Multi-threaded SMS request sending.
- Adjustable number of SMS, delay between requests, and threads.
- Progress bar with `tqdm` for visual feedback.
- Input validation for phone numbers and parameters.
- Clear banner and owner info display.

## Requirements

- Python 3.6+
- requests library
- tqdm library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python err0r_bomber.py
```

Follow the prompts:

1. Enter country code (without the +).
2. Enter target phone number (without country code).
3. Enter number of SMS to send (max 500).
4. Enter delay between requests in seconds (e.g., 0.5).
5. Enter number of threads to use.

Press CTRL+C to stop the bombing at any time.

## Disclaimer

This tool is intended for educational purposes only. Unauthorized use on any phone number or system without explicit permission is illegal and unethical.

## Author

ERR0R-V4U  
[Facebook](https://www.facebook.com/profile.php?id=61564222827738) | [Telegram](https://t.me/ERR0R_V4U_Your_Love)
