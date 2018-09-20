var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        console.log(myObj)
        plot(myObj)
        // return myObj
    }
};

function plot(json_obj)
{
    window.onload = function()
    {
        var ctx = document.getElementById('bar_plot').getContext('2d');
        window.myBar = new Chart(ctx, {
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

}

xmlhttp.open("GET", "data.json", true);
xmlhttp.send();