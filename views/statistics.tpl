% rebase('base.tpl', title='Statistics')
<script type="text/javascript">
    function success_callback(response){
        $('#ajax_error').html('&nbsp;');
        $('#data_table tbody').prepend(
          "<tr><td>" + response.student_name +
          "</td><td>" + response.room_name +
          "</td><td>" + response.quarter_name +
          "</td><td>" + response.subject_name +
          "</td><td>" + response.value + "</td></tr>"
        )
    }
    function error_callback(response){
        $('#ajax_error').text(response.responseText);
    }
    $(document).ready(() => {
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
</script>
<h4 class="ml-4">Add subjects:</h4>
<form id="simpleform" method="post" action="/api/statistics" class="ml-4">
    %fields = ['student', 'room', 'quarter', 'subject']
    %for f in fields:
      <div class="form-group row mb-0">
          <label for="{{f}}"  class="col-sm-1 col-form-label">
              {{f.capitalize() if f != 'room' else 'Class'}}
          </label>
          <div class="col-sm-2">
              <select id="{{f}}" name="{{f}}" class="form-control form-control-sm" required></select>
          </div>
      </div>
    %end
    <div class="form-group row mb-0">
      <label for="value"  class="col-sm-1 col-form-label">
          Value
      </label>
      <div class="col-sm-2">
          <input id="value" name="value" type="number" min="1" max="10" class="form-control form-control-sm" required />
      </div>
    </div>
<input type="submit" class="btn btn-primary" value="Submit Form">
</form>

<p id="ajax_error" class="ml-4">&nbsp;</p>
<h4 class="ml-4">Statistics history:</h4>
<table id="data_table" class="table col-sm-8 ml-4">
    <thead>
    <tr>
        <th scope="col">Name</th>
        <th scope="col">Class</th>
        <th scope="col">Quarter</th>
        <th scope="col">Subject</th>
        <th scope="col">Value</th>
    </tr>
    </thead>
    <tbody></tbody>
</table>