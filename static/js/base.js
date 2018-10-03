function fetch_source(url, callback){
    fetch(url, {
      method: "GET",
      data: {},
      dataType: 'json',
      ContentType: 'application/json'
    })
    .then((resp) => {
      return resp.json();
    })
    .then((objs) => {
        callback(objs);
    })
    .catch((err) => {
      console.log(err);
    });
}
$(document).ready(() => {
    $('#simpleform').submit(function(event)  {
        event.preventDefault();
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            success: success_callback,
            error: error_callback
        });
    });
});