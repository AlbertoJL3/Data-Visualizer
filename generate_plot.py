# generate_plot.py
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json

# Generate sample data
np.random.seed(42)
n = 1000
x1 = np.random.randn(n)
y1 = 2 * x1 + np.random.randn(n)
x2 = np.random.randn(n)
y2 = -2 * x2 + np.random.randn(n)

# Create DataFrames
df1 = pd.DataFrame({'x': x1, 'y': y1})
df2 = pd.DataFrame({'x': x2, 'y': y2})

# Create scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df1['x'].tolist(), y=df1['y'].tolist(), mode='markers', name='Dataset 1'))
fig.add_trace(go.Scatter(x=df2['x'].tolist(), y=df2['y'].tolist(), mode='markers', name='Dataset 2'))

# Update layout
fig.update_layout(
    title='Scatter Plot Comparison',
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    height=600,
    width=800
)

# Custom JSON encoder to handle NumPy types
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# Convert the figure to JSON
plot_json = json.dumps(fig.to_dict(), cls=NumpyEncoder)

# Create the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scatter Plot Comparison</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        #button-container {{
            margin-bottom: 20px;
        }}
        button {{
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            margin: 0 10px;
        }}
        button:hover {{
            background-color: #45a049;
        }}
        #plotly-graph {{
            width: 100%;
            height: 600px;
        }}
        #loading-indicator {{
            font-size: 18px;
            margin-bottom: 10px;
            color: #ff6600;
        }}
    </style>
</head>
<body>
    <div id="loading-indicator">Initializing...</div>
    <div id="button-container">
        <button id="export1" disabled>Export Dataset 1</button>
        <button id="export2" disabled>Export Dataset 2</button>
    </div>
    <div id="plotly-graph"></div>
    <script>
        var plotlyJson = {plot_json};
        window.addEventListener('load', function() {{
            Plotly.newPlot('plotly-graph', plotlyJson.data, plotlyJson.layout);
            document.getElementById('loading-indicator').textContent = 'Ready!';
            document.getElementById('loading-indicator').style.color = '#4CAF50';
            document.getElementById('export1').disabled = false;
            document.getElementById('export2').disabled = false;
        }});
    </script>
    <script src="export_data.js"></script>
</body>
</html>
"""

# Write the HTML content to a file
with open('scatter_comparison.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Scatter plot comparison has been saved as 'scatter_comparison.html'. Make sure 'export_data.js' is in the same directory, then open the HTML file in a web browser to view and interact with the plot.")