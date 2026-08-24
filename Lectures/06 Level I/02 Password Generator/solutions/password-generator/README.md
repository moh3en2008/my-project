# Password Generator - OOP Approach

This project is a Python-based password generator that demonstrates Object-Oriented Programming (OOP) concepts.

The application can generate three types of passwords:

1. Random Passwords
2. Memorable Passwords
3. PIN Codes

## How It Works

The password generator uses the Python `random` module to generate passwords. The generator is split into three classes, each representing a different type of password generation:

1. `RandomPasswordGenerator` generates a random password of a specified length, with optional numbers and symbols.

2. `MemorablePasswordGenerator` creates a password made up of a set number of randomly chosen words from the NLTK English language corpus. It can optionally separate the words with a separator and change their capitalization.

3. `PinGenerator` creates a numeric password of a specified length.

Each generator class inherits from the base `PasswordGenerator` class. They override the base class's `generate()` method to provide their own password generation functionality.

## Project Structure

```text
Password-Generator/
├── src/
│   ├── main.py
│   └── main.ipynb
├── README.md
└── requirements.txt
```

### main.py

The main Python script of the project. It contains the password generator classes and demonstrates the generation of random, memorable, and PIN passwords.

### main.ipynb

A Jupyter Notebook used for personal testing and experimentation with the password generation functionality.

### requirements.txt

Contains the Python dependencies required to run the project.

## Requirements

- Python 3.7+
- NLTK 3.10.3

To install the required dependencies, use:

```bash
pip install -r requirements.txt
```

The NLTK `words` corpus is downloaded automatically when the program starts.

## Running the Project

Navigate to the `src` directory and run the project using Python:

```bash
cd src
python main.py
```

## Concepts Practiced

This project demonstrates several Object-Oriented Programming concepts, including:

- Abstract Classes
- Inheritance
- Polymorphism
- Type Hints
- Python Modules
- Working with External Libraries

That's all you need to know to get started with this project. Enjoy generating passwords!