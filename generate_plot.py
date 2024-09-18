import plotly.graph_objects as go
import pandas as pd
import json
import argparse
import os

def load_dataset(file_path):
    if '.csv' in file_path:
        return pd.read_csv(file_path)
    elif '.xls' in file_path:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format")

def generate_plot(file_path1, file_path2):
    df1 = load_dataset(file_path1)
    df2 = load_dataset(file_path2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df1['x'].tolist(), y=df1['y'].tolist(), mode='markers', name='Dataset 1'))
    fig.add_trace(go.Scatter(x=df2['x'].tolist(), y=df2['y'].tolist(), mode='markers', name='Dataset 2'))

    fig.update_layout(
        title='Scatter Plot Comparison',
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        height=600,
        width=800
    )
    print('generating fig...')
    return fig



def main():
    file_path1 = r'dataset_2_visible_data(2).csv'
    file_path2 = r'dataset_1_visible_data(7).csv'
    
    fig = generate_plot(file_path1, file_path2)

    # Custom JSON encoder to handle NumPy types
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, pd.Series):
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
        <link rel="stylesheet" href="styles.css">
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

    print("Scatter plot comparison has been saved as 'scatter_comparison.html'. Make sure 'export_data.js' and 'styles.css' are in the same directory, then open the HTML file in a web browser to view and interact with the plot.")

if __name__ == "__main__":
    main()