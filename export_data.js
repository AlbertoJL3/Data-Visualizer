// export_data.js
function exportVisibleData(datasetIndex, datasetId) {
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
        link.setAttribute("download", `dataset_${datasetId}_visible_data.csv`);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var exportButtons = document.querySelectorAll('[id^="export"]');
    exportButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            console.log(`Button ${index + 1} clicked`);
            exportVisibleData(index, this.getAttribute('data-id'));
        });
    });
});