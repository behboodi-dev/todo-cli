# Quickstart

Get the Todo CLI running in less than a minute.

## Requirements

- Python 3.10+
- pip

## Setup

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create your environment file
cp .env.example .env
# On Windows, use: copy .env.example .env