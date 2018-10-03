from bottle import template, route, redirect, get, static_file


@route('/imports')
def imports():
    """Route for imports"""
    return template('imports')


@route('/charts')
def charts():
    """Route for charts"""
    return template('charts')


@route('/rooms')
def rooms():
    """Route for rooms"""
    return template('rooms')


@route('/students')
def students():
    """Route for students"""
    return template('students')


@route('/quarters')
def quarters():
    """Route for quarters"""
    return template('quarters')


@route('/subjects')
def subjects():
    """Route for subjects"""
    return template('subjects')


@route('/statistics')
def statistics():
    """Route for statistics"""
    return template('statistics')


@route('/')
def empty():
    """Redirect to charts"""
    redirect('/charts')


@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    """Route for statics"""
    return static_file(filepath, root="static/js")
