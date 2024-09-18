// export_data.js
function exportVisibleData(datasetIndex) {
    var plotlyGraph = document.getElementById('plotly-graph');
    var data = plotlyGraph.data;
    var layout = plotlyGraph.layout;
    
    var xRange = layout.xaxis.range;
    var yRange = layout.yaxis.range;

    if (!data[datasetIndex] || !data[datasetIndex].x || !data[datasetIndex].y) {
        console.error('Dataset not found or invalid');
        return;
    }

    var visibleData = data[datasetIndex].x.map((x, i) => {
        return {x: x, y: data[datasetIndex].y[i]};
    }).filter(point => 
        point.x >= xRange[0] && point.x <= xRange[1] &&
        point.y >= yRange[0] && point.y <= yRange[1]
    );

    var csv = 'x,y\n' + visibleData.map(point => `${point.x},${point.y}`).join('\n');

    var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement("a");
    if (link.download !== undefined) {
        var url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", `dataset_${datasetIndex + 1}_visible_data.csv`);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('export1').addEventListener('click', function() {
        console.log('Button 1 clicked');
        exportVisibleData(0);
    });

    document.getElementById('export2').addEventListener('click', function() {
        console.log('Button 2 clicked');
        exportVisibleData(1);
    });
});