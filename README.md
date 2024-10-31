# CedulaChecker

This project is designed to validate and format Panamanian **cedula** numbers according to specific patterns based on their type and prefix. The system ensures that cedula numbers conform to required formats, identifies the type, and associates a province when applicable.

## Features

- **Cedula Validation**: Validates cedula numbers according to predefined patterns for different types (e.g., Regular, Panamanian Resident, Indigenous).
- **Cedula Formatting**: Adds leading zeros to parts of the cedula to ensure proper formatting.
- **Province Identification**: Determines the province based on the cedula prefix.

## Installation

1. Clone the repository and navigate to the project directory:


```sh
    git clone https://github.com/Johans1047/CedulaChecker.git
    cd your_project
```

2. Create a virtual environment (optional but recommended):

```sh
   python -m venv venv
   cd your_project
```

3. Activate the virtual environment:

```sh
   .\venv\Scripts\activate
```

4. Install the dependencies using requirements.txt:

```sh
   pip install -r requirements.txt
```

5. Run the project:

```sh
   python app.py
```