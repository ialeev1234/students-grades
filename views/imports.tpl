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
    });
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
<p id="ajax_response" class="ml-4"></p>