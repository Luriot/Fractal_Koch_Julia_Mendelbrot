
# Fractals Visualization: Koch Snowflake, Julia Set, and Mandelbrot Set

This project visualizes three fascinating mathematical fractals: the **Koch Snowflake**, the **Julia Set**, and the **Mandelbrot Set**. Each fractal is generated using Python and can be visualized individually or together in a combined view.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Overview

Fractals are infinitely complex patterns that are self-similar across different scales. This project provides an interactive way to explore these fractals:

1. **Koch Snowflake**: A recursively generated geometric fractal.
2. **Julia Set**: A set of complex numbers that generate beautiful patterns.
3. **Mandelbrot Set**: The iconic fractal set representing complex numbers under iteration.

## Features

- Visualize the **Koch Snowflake** up to a customizable recursion depth.
- Generate the **Julia Set** for any given complex constant.
- Render the **Mandelbrot Set** with adjustable resolution and iteration limits.
- Display all fractals together in a single plot for comparison.
- Interactive visualizations using **Plotly** for individual fractals.

## Requirements

Ensure you have the following installed:

- Python 3.7 or higher
- Required libraries (install with `pip`):
  - `numpy`
  - `matplotlib`
  - `plotly`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Luriot/Fractal_Koch_Julia_Mendelbrot.git
   cd Fractal_Koch_Julia_Mendelbrot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to generate and visualize the fractals:

```bash
python fractal.py
```

### Parameters

You can modify the fractal parameters directly in the script:

- **Koch Snowflake**:
  - `order`: Recursion depth (default: 10)
- **Julia Set**:
  - `julia_c`: Complex constant (default: `-0.7 + 0.27015j`)
  - `julia_resolution`: Resolution of the grid (default: 3000)
  - `julia_iterations`: Maximum iterations (default: 500)
- **Mandelbrot Set**:
  - `mandelbrot_resolution`: Resolution of the grid (default: 3000)
  - `mandelbrot_iterations`: Maximum iterations (default: 500)

## Examples

### Combined View

Displays all three fractals side by side:

![Combined Fractals Example](assets/combined_fractals.png)

### Koch Snowflake

Visualizes the Koch Snowflake at the specified recursion depth:

![Koch Snowflake Example](assets/koch_snowflake.png)

### Julia Set

Generates the Julia Set for a given complex constant:

![Julia Set Example](assets/julia_set.png)

### Mandelbrot Set

Renders the Mandelbrot Set with the specified resolution and iterations:

![Mandelbrot Set Example](assets/mandelbrot_set.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
