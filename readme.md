

# Installation Guide


## Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

- Python 3.x (You can download it from [python.org](https://www.python.org/downloads/))
- `virtualenv` (This can be installed via pip: `pip install virtualenv`)

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/ircNewBie/stock-ticker>
cd stock-ticker
```

### Step 2: Create a Virtual Environment

#### On Windows

Open a command prompt and run the following commands:

```batch
python -m venv venv
venv\Scripts\activate
```

#### On macOS and Linux

Open a terminal and run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

With the virtual environment activated, run the following command to install the project dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Deactivating the Virtual Environment

To deactivate the virtual environment when you're done working on the project, simply run:

```bash
deactivate
```

## Running the Project

After completing the installation steps, you can run your Python project within the virtual environment you created. Activate the virtual environment using the instructions provided in Step 2, and then use the appropriate command to start your project.

## Additional Notes

The following are the command-line options to run the project:
```
make sure you are at './<main-project-folder>/src'  directory to start.
Command-Line: 
    python main.py --feth-data

other options:
------------------------------------------------------
  -h, --help      show this help message and exit
  --fetch-data    Pull market data from api. This should run first and foremost.
  --chart         Show / render ticker chart
  --show-bullish  Show tickers that are potentially bullish
  --show-bearish  Show tickers that are potentially bearish
  --show-tickers  Show tickers that are configured
  --add-ticker    Add ticker to be configured
  --top-buy       Show tickers that are possible to go higher on the next following days

  ````

- It is recommended to create a virtual environment for each Python project to isolate dependencies and avoid conflicts.

---

This README provides instructions for setting up a virtual environment and installing project dependencies from a `requirements.txt` file on Windows, macOS, and Linux. 