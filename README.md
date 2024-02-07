# Patchwork Generator

## Overview
The Patchwork Generator is a Python-based program designed to create a customizable patchwork pattern based on a student number. Users can select the size of the patchwork and colors to personalize their design. This project utilizes the `graphics.py` library for drawing the graphical interface and shapes.

## Features
- **Customizable Sizes**: Choose from three sizes for your patchwork - 5x5, 7x7, or 9x9.
- **Color Selection**: Select three different colors from a predefined list to customize the patchwork.
- **Unique Patterns**: Generates two types of patterns, square and arrow, arranged in a unique composition based on the selected size.
- **Interactive Input**: User inputs for size and color selections are taken via the console.

## Prerequisites
Before running the Patchwork Generator, ensure you have Python installed on your system along with the `graphics.py` library, which is used for all graphical operations.

## Installation
1. **Install Python**:
   Ensure Python is installed on your system. Python 3.x is recommended.

2. **Install graphics.py**:
   You may need to install the `graphics.py` library if it's not already available in your Python environment.
```
pip install graphics.py
```

## Usage Instructions
1. **Running the Program**:
- Open a terminal or command prompt.
- Navigate to the directory where the script is saved.
- Run the script using Python.
```
python patchwork_generator.py
```

2. **Input Parameters**:
- When prompted, enter the desired size of the patchwork (5, 7, or 9).
- Select three different colors for the patchwork when prompted. The valid colors are red, green, blue, magenta, orange, and pink.

3. **Viewing the Patchwork**:
- After entering the inputs, the patchwork will be displayed in a new window.
- Close the window to end the program.

## Code Explanation
- The program starts by taking user inputs for the patchwork size and color selection.
- Based on the inputs, it calculates the layout and determines where to draw square and arrow patches.
- It utilizes two different functions for drawing patches: `drawSquarePatch` for square patches and `drawArrowPatch` for arrow patches, applying the selected colors accordingly.
- The graphical window's size adjusts based on the selected patchwork size, ensuring that the entire patchwork is visible.

## Contributing
Feedback and contributions are welcome! Please feel free to fork the project, make improvements, and submit pull requests.

## License
This project is open-source and available under the MIT License.
