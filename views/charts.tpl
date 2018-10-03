<html>
<head>
  <title>Charts</title>
  <link rel="stylesheet" type="text/css" href="https://cdn.anychart.com/releases/develop/css/anychart-ui.min.css"/>
  <link rel="stylesheet" type="text/css" href="https://cdn.anychart.com/releases/develop/fonts/css/anychart-font.min.css"/>
    %include('heads.tpl')
  <script src="https://cdn.anychart.com/releases/develop/js/anychart-base.min.js"></script>
  <script src="https://cdn.anychart.com/releases/develop/js/anychart-ui.min.js"></script>
  <script src="https://cdn.anychart.com/releases/develop/js/anychart-exports.min.js"></script>
  <script src="/static/js/charts.js"></script>
  <style>
    #container {
      width: 100%;
      height: 50%;
      margin: 0;
      padding: 0;
    }
  </style>
</head>
<body>
    %include('header.tpl')
    <h4 class="ml-4">Choose filters:</h4>
    <form id="simpleform" action="/api/charts" class="ml-4">
        %fields = ['student', 'room', 'quarter', 'subject', 'grouping']
        %for f in fields:
          <div class="form-group row mb-0">
              <label for="{{f}}"  class="col-sm-1 col-form-label">
                  {{f.capitalize() if f != 'room' else 'Class'}}
              </label>
              <div class="col-sm-2">
                  <select id="{{f}}" name="{{f}}" class="form-control form-control-sm">
                      %if f != 'grouping':
                        <option value="0">Please, select</option>
                      %else:
                        %for o in fields:
                            %if o != 'grouping':
                                <option value="{{o}}">{{o.capitalize() if f != 'room' else 'Class'}}</option>
                            %end
                        %end
                      %end
                  </select>
              </div>
          </div>
        %end
    <input type="submit" class="btn btn-primary" value="Submit Form">
    </form>
    <div id="container"></div>
</body>
</html>



                