# THis is a file that i can not use for now due to mysqldb issues
from app import app, db

# create the cardinalaties later
class class_room(db.Model):
    __tablename__ = 'class_room'
    class_room_id = db.Column(db.Integer, primary_key = True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher_info.teacher_id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student_info.student_id'))


class course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key = True)
    course_section = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher_info.teacher_id'))
    course_time = db.Column(db.Unicode)
    student_id = db.Column(db.Integer, db.ForeignKey('student_info.student_id'))
    course_room = db.Column(db.Unicode)
    course_code = db.Column(db.Unicode, db.ForeignKey('course_info.course_code'))


class course_info(db.Model):
    __tablename__ = 'course_info'
    course_code = db.Column(db.Unicode, primary_key = True)
    course_name = db.Column(db.Unicode)
    course_description = db.Column(db.Unicode)


class notice_board(db.Model):
    __tablename__ = 'notice_board'
    notice_id = db.Column(db.Integer, primary_key = True)
    class_room_id = db.Column(db.Integer, db.ForeignKey('class_room.class_room_id'))


class post_comments(db.Model):
    __tablename__ = 'post_comments'
    comment_id = db.Column(db.Integer, primary_key = 'True')
    post_id = db.Column(db.Integer, db.ForeignKey('wall_post.post_id'))
    commenter_id = db.Column(db.Integer)
    user_identity = db.Column(db.Unicode)
    comment = db.Column(db.Unicode)


class quiz_mark(db.Model):
    __tablename__ = 'quiz_marks'
    quiz_row_id = db.Column(db.Integer, primary_key = True)
    class_room_id = db.Column(db.Integer, db.ForeignKey('class_room.class_room_id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student_info.student_id'))
    quiz_number = db.Column(db.Integer)
    quiz_marks = db.Column(db.Integer)


class student_info(db.Model):
    __tablename__ = 'student_info'
    student_id = db.Column(db.Integer, primary_key = True)
    student_name = db.Column(db.Unicode, nullable = False)
    student_email = db.Column(db.Unicode, nullable = False)
    student_password = db.Column(db.Unicode, nullable = False)
    student_phone_no = db.Column(db.Integer, nullable = False)
    student_profile_pic = db.Column(db.Unicode)
    student_dpt = db.Column(db.Unicode, nullable = False)
    student_sem = db.Column(db.Integer, nullable = False)


class teacher_availability(db.Model):
    __tablename__ = 'teacher_availability'
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher_info.teacher_id'), primary_key = True)
    availability = db.Column(db.Integer)


class teacher_info(db.Model):
    __tablename__ = 'teacher_info'
    teacher_id = db.Column(db.Integer, primary_key = True)
    teacher_name = db.Column(db.Unicode, nullable = False)
    teacher_password = db.Column(db.Unicode, nullable = False)
    teacher_department = db.Column(db.Unicode, nullable = False)
    teacher_phone = db.Column(db.Integer, nullable = False)
    teacher_room = db.Column(db.Unicode)
    teacher_consultation = db.Column(db.Unicode)
    teacher_profile_pic = db.Column(db.Unicode)


class wall_post(db.Model):
    __tablename__ = 'wall_post'
    post_id = db.Column(db.Integer, primary_key = True)
    class_room_id = db.Column(db.Integer, db.ForeignKey('class_room.class_room_id'))
    user_identity = db.Column(db.Unicode)
    poster_id = db.Column(db.Integer)
    post = db.Column(db.Unicode)


# Setting up the Many to Manny Cardinality Relation Ship and association tables
# belongs_to = db.Table('belongs_to', {
#     db.Column('student_id', db.Integer, db.ForeignKey('student_info.student_id'))
#     db.Column('class_room_id', db.Integer, db.ForeignKey('class_room.class_room_id'))
# })
