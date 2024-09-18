# Data-Visualizer
This project generates an interactive scatter plot comparison of two datasets, allowing users to visualize and export visible data points.

## Features

- Interactive scatter plot with two datasets
- Ability to zoom and pan the plot
- Export visible data points for each dataset as CSV files
- Loading indicator to show when the plot is ready

## Files

1. `generate_plot.py`: Python script to generate the scatter plot and HTML file
2. `export_data.js`: JavaScript file for exporting visible data points
3. `scatter_comparison.html`: Generated HTML file containing the interactive plot

## Requirements

- Python 3.x
- Plotly
- Pandas
- NumPy

## Setup and Usage

1. Install the required Python packages:
   ```
   pip install plotly pandas numpy
   ```

2. Run the Python script to generate the plot:
   ```
   python generate_plot.py
   ```

3. Ensure that `export_data.js` is in the same directory as the generated `scatter_comparison.html` file.

4. Open `scatter_comparison.html` in a web browser to view and interact with the plot.

5. Use the "Export Dataset 1" and "Export Dataset 2" buttons to download CSV files containing the visible data points for each dataset.

## How It Works

- `generate_plot.py` creates sample data, generates a Plotly scatter plot, and embeds it into an HTML file along with necessary styling and scripts.
- The HTML file includes buttons for exporting data and a loading indicator.
- `export_data.js` contains the logic for exporting visible data points as CSV files when the export buttons are clicked.

## Customization

To use your own data:
1. Modify the data generation section in `generate_plot.py` to load or create your desired datasets.
2. Adjust the plot title, axis labels, and other layout properties in the `fig.update_layout()` call.

## Notes

- The exported data will only include points currently visible in the plot view.
- Zooming and panning the plot will affect which data points are exported.
