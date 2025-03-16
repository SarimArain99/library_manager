# Library Management System (CLI-Based)

## 📚 Overview

This is a command-line interface (CLI) program for managing a personal library. It allows users to add, remove, search, and display books, as well as track reading statistics. The program leverages the `colorama` library for enhanced terminal output.

## 🚀 Features

- Add new books with details (title, author, year, genre, and read status).
- Remove books by title.
- Search for books by title or author.
- Display all books with formatted output.
- Show reading statistics (read/unread percentages).
- Save and load data from a `library.json` file.

## 🛠️ Prerequisites

- Python 3.x
- `colorama` library

### Install `colorama`

```bash
pip install colorama
```

## 📂 Project Structure

```
library_manager/
│
├── library.json      # Data storage file
├── library_manager.py          # Main script
└── requirements.txt # Dependencies
```

## 🏁 Usage

1. Clone the repository:

```bash
git clone https://github.com/SarimArain99/library_manager.git
```

2. Navigate to the project folder:

```bash
cd library_manager
```

3. Install dependencies:

```bash
pip install colorama

```

4. Run the program:

```bash
python library_manager.py
```

## 🛑 Exit and Save

To exit the program and save the current library state, select option `6` from the menu.

## 📝 License

This project is licensed under the MIT License.
