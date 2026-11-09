# Non-Metal Elements Information Finder
from pyscript import document, display # type: ignore[reportMissingImports]

# Python Dictionary storing every kinds of non-metal elements
non_metals = {
    "H": {
        "name": "Hydrogen",
        "atomic_number": 1,
        "atomic_mass": 1.008
    },
    "He": {
        "name": "Helium",
        "atomic_number": 2,
        "atomic_mass": 4.0026
    },
    "C": {
        "name": "Carbon",
        "atomic_number": 6,
        "atomic_mass": 12.011
    },
    "N": {
        "name": "Nitrogen",
        "atomic_number": 7,
        "atomic_mass": 14.007
    },
    "O": {
        "name": "Oxygen",
        "atomic_number": 8,
        "atomic_mass": 15.999
    },
    "F": {
        "name": "Fluorine",
        "atomic_number": 9,
        "atomic_mass": 18.998
    },
    "Ne": {
        "name": "Neon",
        "atomic_number": 10,
        "atomic_mass": 20.180
    },
    "P": {
        "name": "Phosphorus",
        "atomic_number": 15,
        "atomic_mass": 30.974
    },
    "S": {
        "name": "Sulfur",
        "atomic_number": 16,
        "atomic_mass": 32.06
    },
    "Cl": {
        "name": "Chlorine",
        "atomic_number": 17,
        "atomic_mass": 35.45
    },
    "Ar": {
        "name": "Argon",
        "atomic_number": 18,
        "atomic_mass": 39.948
    },
    "Se": {
        "name": "Selenium",
        "atomic_number": 34,
        "atomic_mass": 78.971
    },
    "Br": {
        "name": "Bromine",
        "atomic_number": 35,
        "atomic_mass": 79.904
    },
    "Kr": {
        "name": "Krypton",
        "atomic_number": 36,
        "atomic_mass": 83.798
    },
    "I": {
        "name": "Iodine",
        "atomic_number": 53,
        "atomic_mass": 126.90
    },
    "Xe": {
        "name": "Xenon",
        "atomic_number": 54,
        "atomic_mass": 131.29
    },
    "Rn": {
        "name": "Radon",
        "atomic_number": 86,
        "atomic_mass": 222
    }
}

def check_details(event):
    # Getting input from the HTML text field
    symbol_input = document.getElementById("symbol_input").value.strip()
    
    # Formatting input answer still valid while capitalizing the first letter
    formatted_symbol = symbol_input.capitalize()
    
    # Check if element exists in the non-metals dictionary
    if formatted_symbol in non_metals:
        element = non_metals[formatted_symbol]
        
        # Formatting the resulting display
        result_text = (
            f"Symbol: {formatted_symbol}\n"
            f"Element: {element['name']}\n"
            f"Atomic Number: {element['atomic_number']}\n"
            f"Atomic Mass: {element['atomic_mass']}"
        )
        display(result_text, target="result_output", append=False)
    else:
        # Error message if symbol is not on or in this list
        display("The entered symbol does not exist in the non-metals list.", target="result_output", append=False)