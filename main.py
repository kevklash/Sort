"""
sort.py

This module provides a function to sort packages into categories based on their dimensions and mass.
Packages are classified as 'STANDARD', 'SPECIAL', or 'REJECTED' depending on their size and weight.

Author: Kevin Romero
Date: May 23, 2025
"""


def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts packages based on their dimensions and mass. Returns STANDARD, SPECIAL, or REJECTED.

    Args:
        width (float): Width of the package in cm.
        height (float): Height of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.

    Returns:
        str: The stack where the package should go ('STANDARD', 'SPECIAL', or 'REJECTED').
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"


if __name__ == "__main__":
    print(sort(10, 10, 10, 5))
    print(sort(100, 100, 100, 5))
    print(sort(10, 10, 10, 25))
    print(sort(200, 200, 200, 25))
