% rebase('base.tpl', title='Students')
<script type="text/javascript">
    function success_callback(response){
        $('#ajax_error').html('&nbsp;');
        $('#data_table tbody').prepend(
          "<tr><td>" + response.name +
          "</td><td>" + response.birth + "</td></tr>"
        )
    }
    function error_callback(response){
        $('#ajax_error').text(response.responseText);
    }
    $(document).ready(() => {
        fetch_source("/api/students", (objs) => {
            for (let i = 0; i < objs.length; i++) {
                $('#data_table').append(
                    "<tr><td>" + objs[i].name +
                    "</td><td>" + objs[i].birth + "</td></tr>"
                );
            }
        });
    });
</script>
<h4 class="ml-4">Add students:</h4>
<form id="simpleform" method="post" action="/api/students" class="ml-4">
  <div class="form-group row mb-0">
      <label for="name" class="col-sm-1 col-form-label">
          Name
      </label>
      <div class="col-sm-2">
          <input id="name" type="text" name="name" class="form-control form-control-sm" required />
      </div>
  </div>
  <div class="form-group row mb-0">
      <label for="birth" class="col-sm-1 col-form-label">
          Birth
      </label>
      <div class="col-sm-2">
          <input id="birth" type="date" name="birth" class="form-control form-control-sm" required />
      </div>
  </div>
<input type="submit" class="btn btn-primary" value="Submit Form">
</form>

<p id="ajax_error" class="ml-4">&nbsp;</p>
<h4 class="ml-4">List of students:</h4>
<table id="data_table" class="table col-sm-3 ml-4">
    <thead>
    <tr><th scope="col">Name</th><th scope="col">Birth</th></tr>
    </thead>
    <tbody></tbody>
</table>