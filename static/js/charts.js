function success_callback(response){
    $('#ajax_error').html('&nbsp;');
    refresh_chart(response);
}
function error_callback(response){
    $('#ajax_error').text(response.responseText);
}
function refresh_chart(data){
  chart.removeAllSeries();
  chart.column(data.data);
  chart.title(data.title);
}
var chart;
function anychart_init() {
  chart = anychart.column();
  chart.animation(true);

  var series = chart.column();
  series.tooltip()
    .position('center-top')
    .anchor('center-bottom')
    .offsetX(0)
    .offsetY(5)
    .format('{%Value}');

  chart.yScale().minimum(0);
  chart.tooltip().positionMode('point');
  chart.yAxis(0).title('Average');
  chart.tooltip().format('{%Value}');
  chart.container('container');
  chart.draw();
}
$(document).ready(() => {
    anychart_init();
    fetch_source("/api/subjects", (objs) => {
        for (let i = 0; i < objs.length; i++) {
            $('#subject').append("<option value=" + objs[i].id + ">" + objs[i].name + "</option>");
        }
    });
    fetch_source("/api/rooms", (objs) => {
        for (let i = 0; i < objs.length; i++) {
            $('#room').append("<option value=" + objs[i].id + ">" + objs[i].name + "</option>");
        }
    });
    fetch_source("/api/quarters", (objs) => {
        for (let i = 0; i < objs.length; i++) {
            $('#quarter').append(
            "<option value=" + objs[i].id + ">" + objs[i].year + " - " + objs[i].quarter + "</option>"
            );
        }
    });
    fetch_source("/api/students", (objs) => {
        for (let i = 0; i < objs.length; i++) {
            $('#student').append(
            "<option value=" + objs[i].id + ">" + objs[i].name + " (" + objs[i].birth + ")</option>"
            );
        }
    });
});