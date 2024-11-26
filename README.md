# Dev tools

## Installation

1. Clone the repository:

```bash
git clone https://github.com/wavteam/dev
cd tools
```

2. Install dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

```bash
python bomber.py [--file FILE] [--country-code COUNTRY_CODE] [--phone PHONE_NUMBER] [-e]
```

### Arguments

- `--file FILE`: Path to the JSON file with request descriptions. Default: `service.json`.
- `--country-code COUNTRY_CODE`: Country code for the phone number. Default: `7`.
- `--phone PHONE_NUMBER`: Phone number to be used in the requests. If not specified, prompts user input.
- `-e`, `--edit`: Launches an interactive editor for editing the JSON file with request descriptions.

### Examples

1. Running the script with `services.json` file:

```bash
python bomber.py --file services.json
```

2. Running the script with specifying the phone number:

```bash
python bomber.py --country-code 7 --phone 1234567890
```

3. Editing the JSON file with request descriptions:

```bash
python bomber.py -e
```