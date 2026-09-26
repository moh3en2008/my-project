# 🔐 Password Generator

A password generator application built with Python and Streamlit.

The project uses Object-Oriented Programming (OOP) to provide three different password generation methods through a simple web interface.

## ✨ Features

* 🔑 Random Password Generator

  * Custom password length
  * Optional numbers
  * Optional symbols

* 🧠 Memorable Password Generator

  * Choose the number of words
  * Custom separator
  * Optional capitalization

* 🔢 PIN Code Generator

  * Custom PIN length

## 🛠️ Technologies

* Python
* Streamlit
* NLTK
* Object-Oriented Programming (OOP)
* Abstract Base Classes

## 📁 Project Structure

```text
Password_Generator/
├── README.md
├── requirements.txt
├── images/
│   └── banner.jpeg
└── src/
    ├── dashboard.py
    └── password_generator.py
```

## 🚀 Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/moh3en2008/my-project.git
cd my-project/Password_Generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the Streamlit application with:

```bash
streamlit run src/dashboard.py
```

The application will open locally in your browser.

## 🧩 OOP Concepts

This project demonstrates several Object-Oriented Programming concepts, including:

* Abstract Base Classes
* Abstract Methods
* Inheritance
* Method Overriding
* Encapsulation through class design

The `PasswordGenerator` class acts as an abstract base class, while the specific generators implement their own `generate()` methods.

## 📌 Project Status

Completed as part of my Python learning and project-based practice.
