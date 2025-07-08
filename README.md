# Tax Calculator

A simple desktop tax calculator built with Python, Pygame, and pygame_gui.

![image](https://github.com/user-attachments/assets/7bd6dd48-a361-4c43-8e02-010b5a07179a)

## Features

- Enter an original price and calculate the total with 10% tax.
- Simple, user-friendly interface.
- Error handling for invalid input.

## Requirements

- Python 3.x
- pygame
- pygame_gui

## Installation

1. Install dependencies:
    ```
    pip install pygame pygame_gui
    ```

2. Clone or download this repository.

## Usage

1. Run the application:
    ```
    python main.py
    ```

2. Enter the original price (e.g., `699.99`) in the input field.

3. Click the **Calculate** button.

4. The total price including 10% tax will be displayed in the output field.

## Customization

- The tax rate is currently set to 10%. You can change it in the code:
  ```python
  total = float(calctxt.get_text()) * 0.10 + float(calctxt.get_text())
  ```

## Notes

- Make sure the `buttons.json` theme file is present in the same directory as `main.py` or update the path in the code.

## License

MIT License
