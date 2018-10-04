% rebase('base.tpl', title='Imports')
<script type="text/javascript">
    $(document).ready(() => {
        $('#importform').submit(function(event) {
            event.preventDefault();
            var data = new FormData(this);
            $("#importform :input").attr("disabled", true);
            $('#ajax_response').text('Please, wait...');
            $.ajax({
                type: 'POST',
                url: this.action,
                data: data,
                contentType: false,
                processData: false,
                success: success_callback,
                error: error_callback,
                complete: () => {$("#importform :input").attr("disabled", false);}
            });
        });
        $('#delete_all').click(function(){
            $.ajax({
                type: 'DELETE',
                url: '/api/import',
                success: delete_callback
            });
        });
    });
    delete_callback = (response) => {$('#ajax_delete').text(response);}
    success_callback = (response) => {$('#ajax_response').text(response.msg);}
    error_callback = (response) => {$('#ajax_response').text(response.responseText);}
</script>
<form id="importform" method="post" action="/api/import" enctype="multipart/form-data" class="ml-4">
  <div class="form-group row mb-0">
      <label for="upload"  class="col-sm-1 col-form-label">
          File
      </label>
      <div class="col-sm-2">
          <input id="upload" type="file" name="upload" class="form-control-file form-control-sm" required />
      </div>
  </div>
<input type="submit" class="btn btn-primary" value="Submit Form">
</form>
<p id="ajax_response" class="ml-4">&nbsp;</p>
<button type="button" class="btn btn-danger ml-4 mb-3" id="delete_all">Delete all</button>
<p id="ajax_delete" class="ml-4">&nbsp;</p>
