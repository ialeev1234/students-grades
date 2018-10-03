import datetime
import json

from bottle import post, get, request, response

from helpers import (
    get_or_create_by_required, get_by_id, import_students,
    objects_to_json, prepare_response, collect_chart)
from models import Student, Room, Subject, Quarter, Statistic, create_session


@post('/api/subjects')
@prepare_response
def add_subject():
    """API Routes for posting new subject"""
    name = request.forms.get('name')
    return get_or_create_by_required(Subject, name=name)


@post('/api/quarters')
@prepare_response
def add_quarter():
    """API Routes for posting new quarter"""
    year = request.forms.get('year')
    quarter = request.forms.get('quarter')
    return get_or_create_by_required(Quarter, year=year, quarter=quarter)


@post('/api/rooms')
@prepare_response
def add_room():
    """API Routes for posting new room"""
    name = request.forms.get('name')
    return get_or_create_by_required(Room, name=name)


@post('/api/students')
@prepare_response
def add_student():
    """API Routes for posting new student"""
    name = request.forms.get('name')
    birth = datetime.datetime.strptime(request.forms.get('birth'), "%Y-%m-%d").date()
    return get_or_create_by_required(Student, name=name, birth=birth)


@post('/api/statistics')
def add_statistic():
    """API Routes for posting new statistic"""
    params = {
        'student_id': int(request.forms.get('student')),
        'room_id': int(request.forms.get('room')),
        'quarter_id': int(request.forms.get('quarter')),
        'subject_id': int(request.forms.get('subject')),
        'value': request.forms.get('value')
    }
    obj, new = get_or_create_by_required(Statistic, **params)
    response.content_type = 'application/json'
    if not new:
        session = create_session()
        obj.value = params['value']
        session.commit()
    return json.dumps(obj.as_dict())


@post('/api/import')
def import_file():
    """API Routes for file importing"""
    upload = request.files.get('upload')
    success = import_students(upload)
    response.content_type = 'application/json'
    if success:
        result = json.dumps({'msg': 'Import finished'})
    else:
        response.status = 422
        result = "Bad file's format"
    return result


@get('/api/charts')
def get_charts():
    """API Routes for getting statistics charts"""
    response.content_type = 'application/json'
    return json.dumps(collect_chart(request.query))


@get('/api/statistics')
@get('/api/statistics/<statistic_id:int>')
def get_statistics(db, statistic_id=None):
    """API Routes for getting statistics"""
    return objects_to_json(get_by_id(db, Statistic, statistic_id))


@get('/api/students')
@get('/api/students/<student_id:int>')
def get_students(db, student_id=None):
    """API Routes for getting students"""
    return objects_to_json(get_by_id(db, Student, student_id))


@get('/api/subjects')
@get('/api/subjects/<subject_id:int>')
def get_subject(db, subject_id=None):
    """API Routes for getting subjects"""
    return objects_to_json(get_by_id(db, Subject, subject_id))


@get('/api/quarters')
@get('/api/quarters/<quarter_id:int>')
def get_quarter(db, quarter_id=None):
    """API Routes for getting quarters"""
    return objects_to_json(get_by_id(db, Quarter, quarter_id))


@get('/api/rooms')
@get('/api/rooms/<room_id:int>')
def get_room(db, room_id=None):
    """API Routes for getting rooms"""
    return objects_to_json(get_by_id(db, Room, room_id))
