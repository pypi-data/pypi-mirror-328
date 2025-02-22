from os import system
from sys import platform
from collections.abc import Container

def isInt(input: str) -> bool:
    """
    Check if a str is an integer or not. Return True if yes, else return False.
    """
    if not isinstance(input, int):
        raise ValueError("Already an int.")
    if not isinstance(input, str):
        raise TypeError(f"Parameter 'input' expect str, got {type(input).__name__} instead.")
    
    try:
        int(input)
        return True
    except ValueError:
        return False

def clear():
    """
    Clear the terminal, that's all.
    """
    if platform == "win32":
        system("cls")
    else:
        system("clear")

def num_to_roman(input: int) -> str:
    """
    Convert input (of type int), into Roman numerals.
    """
    if not isinstance(input, int):
        raise TypeError(f"Parameter 'input' expects type int, got {type(input).__name__} instead.")

    roman: str = ""
    number_map: dict[str, int] = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL", 
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    for value in number_map:
        while input >= value:
            roman += number_map[value]
            input -= value

    return roman

def menu(config: Container, start: int = 1, trailing_dot: bool = True, roman_numeral_mode: bool = False) -> str:
    """
    Generate the options in a menu.

    :type config: Container
    :param config:
    + Accept any container type
    + For any container but dict, the items in the said container will be the option for the menu.
    + For dict, the keys in the dict will the options and the value.
    + Do note that whitespace in str will also count into the option.
    :type start: int
    :param start: Accept int. Specify where to start generate a menu. Default is 1.
    :type trailing_dot: bool
    :param trailing_dot: Accept bool. Decide whether option should end with a dot. Default is True.
    :type roman_numeral_mode: bool
    :param roman_numeral_mode: Decide whether or not to use Roman numerals instead of integer. Default is False.
    """
    if not isinstance(config, Container):
        TypeError(f"Parameter 'config' expect container type (e.g list, str, dict,...), got {type(config).__name__} instead.")
    if not isinstance(start, int):
        TypeError(f"Parameter 'start' expect int, got {type(start).__name__} instead.")
    if not isinstance(trailing_dot, bool):
        TypeError(f"Parameter 'trailing_dot' expect bool, got {type(trailing_dot).__name__} instead.")
    if not isinstance(roman_numeral_mode, bool):
        TypeError(f"Parameter 'roman_numeral_mode' expect bool, got {type(trailing_dot).__name__} instead.")
    if isinstance(config, dict):
        config = [x for x in config.keys()]

    output = ""
    for i in range(start, len(config) + start):
        if not roman_numeral_mode:
            if trailing_dot:
                output += f"{i}. {config[i - start]}."
            else:
                output += f"{i}. {config[i - start]}"
        else:
            if trailing_dot:
                output += f"{num_to_roman(i)}. {config[i - start]}."
            else:
                output += f"{num_to_roman(i)}. {config[i - start]}"
        
        if i - start + 1 < len(config):
            output += "\n"
    return output

if __name__ == "__main__":
    print(menu([*"abcdefghijklmnopqrstuvwxyz"]))