var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        plot(JSON.parse(this.responseText))
    }
};

function plot(json_obj)
{
    var ctx = document.getElementById('bar_plot').getContext('2d');
    var bar_plot = new Chart(ctx, {
        type: 'bar',
        data: json_obj,
        options: {
            title: {
                display: true,
                text: 'Activity log',
            },
            tooltips: {
                mode: 'index',
                intersect: true
            },
            responsive: true,
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true
                }]
            }
        }
    })
    

}

xmlhttp.open("GET", "../static/data.json", true);
xmlhttp.send();