% rebase('base.tpl', title='Quarters')
<script type="text/javascript">
    function success_callback(response){
        $('#ajax_error').html('&nbsp;');
        $('#data_table tbody').prepend(
          "<tr><td>" + response.year + " - " + response.quarter + "</td></tr>"
        )
    }
    function error_callback(response){
        $('#ajax_error').text(response.responseText);
    }
    $(document).ready(() => {
        fetch_source("/api/quarters", (objs) => {
            for (let i = 0; i < objs.length; i++) {
                $('#data_table').append("<tr><td>" + objs[i].year + " - " + objs[i].quarter + "</td></tr>");
            }
        });
    });
</script>
<h4 class="ml-4">Add quarters:</h4>
<form id="simpleform" method="post" action="/api/quarters" class="ml-4">
  <div class="form-group row mb-0">
      <label for="year"  class="col-sm-1 col-form-label">
          Year
      </label>
      <div class="col-sm-2">
          <input id="year" type="number" name="year" min="0" class="form-control form-control-sm" required />
      </div>
  </div>
  <div class="form-group row mb-0">
      <label for="quarter" class="col-sm-1 col-form-label">
          Quarter
      </label>
      <div class="col-sm-2">
          <input id="quarter" type="text" name="quarter" class="form-control form-control-sm" required />
      </div>
  </div>
<input type="submit" class="btn btn-primary" value="Submit Form">
</form>

<p id="ajax_error" class="ml-4">&nbsp;</p>
<h4 class="ml-4">List of quarters:</h4>
<table id="data_table" class="table col-sm-1 ml-4">
    <thead>
    <tr><th scope="col">Name</th></tr>
    </thead>
    <tbody></tbody>
</table>