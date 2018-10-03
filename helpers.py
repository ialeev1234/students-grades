import datetime
import itertools
import json

from bottle import response
from sqlalchemy import func

from models import create_session, Student, Subject, Room, Quarter, Statistic

HEADER = 'Student ID,Student Name,Date Of Birth,Student Class,Year,Quarter,'


def objects_to_json(objs):
    """
    Wrapper for format objects to JSON.
    :param objs:
    :return:
    """
    return json.dumps([o.as_dict() for o in objs])


def get_stat_join_params(field):
    """
    Query.join params getter by field of Statistic.
    :param field:
    :return:
    """
    attr = getattr(Statistic, field + '_id')
    join = getattr(Statistic, field)
    return attr, join, join.prop.mapper.entity


def prepare_response(f):
    """
    Decorator for format object to JSON and response preparing.
    :param f:
    :return:
    """
    def wrapper(*args, **kwargs):
        obj, new = f(*args, **kwargs)
        response.content_type = 'application/json'
        if new:
            result = json.dumps(obj.as_dict())
        else:
            response.status = 409
            result = 'Already exist'
        return result
    return wrapper


def get_or_create_by_required(model, **kwargs):
    """
    Creating object if it not exists by required fields
    :param model:
    :param kwargs:
    :return:
    """
    session = create_session()
    obj = session.query(model).filter_by(**kwargs).first()
    new = not obj
    if new:
        obj = model(**kwargs)
        session.add(obj)
        session.commit()
    return obj, new


def get_by_id(db, model, obj_id):
    """
    Object getter from model by id.
    :param db:
    :param model:
    :param obj_id:
    :return:
    """
    query = db.query(model)
    if obj_id:
        obj = query.get(obj_id)
        result = [query.get(obj_id)] if obj else []
    else:
        result = query.all()
    return result


def collect_chart(filters):
    """
    Helper for collecting data for charts.
    :return:
    """
    gr_attr, gr_rel, gr_model = get_stat_join_params(filters.pop('grouping'))
    title = f'Average per {gr_model.title()}'

    session = create_session()
    query = session.query(gr_model.name, func.avg(Statistic.value)).join(gr_rel)

    filter_titles = []
    for k, v in filters.items():
        v = int(v)
        if not v:
            continue
        f_attr, f_rel, f_model = get_stat_join_params(k)
        if f_attr == gr_attr:
            query = query.filter(f_attr == v)
        else:
            query = query.join(f_model, f_attr == v)
        filter_name = session.query(f_model).get(v).name
        filter_titles.append(f'{f_model.title()}: {filter_name}')
    chart = query.group_by(gr_attr).all()
    if filter_titles:
        title += f" for {', '.join(filter_titles)}"

    return {
        'title': title,
        'data': [list(x) for x in chart]
    }


def import_students(upload):
    """
    Importer Statistics from file.
    Additionally imports all new object, which will be found.
    :param upload:
    :return:
    """
    success = False
    try:
        # check format
        header = upload.file.readline().decode()
        assert header.startswith(HEADER)
    except:
        header = None

    if header:
        session = create_session()
        subject_ids = []

        # collect existing objects and map it
        for subject in header.replace(HEADER, '').split(','):
            obj, new = get_or_create_by_required(Subject, name=subject)
            subject_ids.append(obj.id)
        statistics = {
            (x.student_id, x.room_id, x.quarter_id, x.subject_id): x
            for x in session.query(Statistic).filter(Statistic.subject_id.in_(subject_ids)).all()
        }
        students = {(x.name, x.birth): x.id for x in session.query(Student).all()}
        quarters = {(x.year, x.quarter): x.id for x in session.query(Quarter).all()}
        rooms = {x.name: x.id for x in session.query(Room).all()}

        # look at new row from the file
        nextline = upload.file.readline()
        while nextline:
            fields = nextline.decode().replace('\n', '').split(',')
            _id, name, birth, room, year, quarter = fields[:6]
            birth = datetime.datetime.strptime(birth, "%d/%m/%Y").date()
            year = int(year)
            stats = fields[6:]
            if room in rooms:
                room_id = rooms[room]
            else:
                obj = Room(name=room)
                session.add(obj)
                session.flush()
                room_id = obj.id
                rooms[room] = room_id
            student_key = (name, birth)
            if student_key in students:
                student_id = students[student_key]
            else:
                obj = Student(name=name, birth=birth)
                session.add(obj)
                session.flush()
                student_id = obj.id
                students[student_key] = student_id
            quarter_key = (year, quarter)
            if quarter_key in quarters:
                quarter_id = quarters[quarter_key]
            else:
                obj = Quarter(year=year, quarter=quarter)
                session.add(obj)
                session.flush()
                quarter_id = obj.id
                quarters[quarter_key] = quarter_id

            # look at every subject column
            for subject_id, value in itertools.zip_longest(subject_ids, stats):
                value = int(value)
                statistic_key = (student_id, room_id, quarter_id, subject_id)
                if statistic_key in statistics:
                    obj = statistics[statistic_key]
                    if obj.value != value:
                        obj.value = value
                        session.flush()
                else:
                    obj = Statistic(
                        student_id=student_id,
                        room_id=room_id,
                        quarter_id=quarter_id,
                        subject_id=subject_id,
                        value=value
                    )
                    session.add(obj)
                    session.flush()

            # commit new row objects
            session.commit()
            nextline = upload.file.readline()
        success = True
    return success
