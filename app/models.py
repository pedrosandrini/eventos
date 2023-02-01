# /**
#  * @author [ Pedro Henrique Garcia Sandrini ]
#  * @email [ sandrini.pedro@outlook.com ]
#  * @create date 2023-01-23 16:29:14
#  * @modify date 2023-01-25 12:17:39
#  * @desc [description]
#  */


from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(account_id):
    return Account.query.get(int(account_id))


class Account(db.Model, UserMixin):

    __tablename__ = 'ACCOUNT'

    account_id = db.Column(db.Integer, primary_key=True)

    account_email = db.Column(db.String(100), nullable=False, unique=True)

    account_password = db.Column(db.String(128), nullable=False)

    # Relation -> 1:1 (Participant, Account)
    participant_id = db.Column(
        db.Integer, db.ForeignKey('PARTICIPANT.participant_id'))

    @property
    def password(self):
        raise AttributeError(
            'Está informação não pode ser exibida por se tratar de uma informação sensível.')

    @password.setter
    def password(self, password):
        self.account_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.account_password, password)

    def __repr__(self):

        account = {
            'Email': self.account_email,
        }

        return account


class Participant(db.Model):

    __tablename__ = 'PARTICIPANT'

    partcipant_id = db.Column(db.Integer, primary_key=True)

    partcipant_name = db.Column(db.String(45), nullable=False)

    partcipant_surname = db.Column(db.String(45), nullable=False)

    partcipant_cpf = db.Column(db.String(11), nullable=False, unique=True)

    partcipant_telephone = db.Column(db.String(12), nullable=True)

    account = db.relationship(
        'Account', backref='participant')

    def __repr__(self):

        participant = {

            'Name': self.partcipant_name,
            'Suname': self.partcipant_surname,
            'CPF': self.partcipant_cpf,
            'Telephone': self.partcipant_telephone
        }

        return participant


class Event(db.Model):

    __tablename__ = 'EVENT'

    event_id = db.Column(db.Integer, primary_key=True)

    event_title = db.Column(db.String(60), nullable=False)

    event_description = db.Column(db.String(200), nullable=True)

    event_initial_date = db.Column(db.String(10), nullable=False)

    event_final_date = db.Column(db.String(10), nullable=False)

    event_seats_number = db.Column(db.Integer, nullable=False)

    event_banner = db.Column(
        db.String(45), nullable=False, default='default.jpg')

    event_status = db.Column(db.Integer, nullable=False, default=1)

    event_modality = db.Column(
        db.String(20), nullable=False, default='presencial')

    # Relation -> 1:1 (Event, SubEvent)
    subevents = db.relationship('SubEvent', backref='event')

    def __repr__(self):

        event = {
            'event_title': self.event_title,
            'event_description': self.event_description,
            'event_initial_date': self.event_initial_date,
            'event_final_date': self.event_final_date,
            'event_seats': self.event_seats_number,
            'event_modality': self.event_modality,
        }

        return event


class SubEvent(db.Model):

    __tablename__ = 'SUB_EVENT'

    sub_event_id = db.Column(db.Integer, primary_key=True)

    sub_event_title = db.Column(db.String(45), nullable=False)

    sub_event_description = db.Column(db.String(200), nullable=False)

    sub_event_initial_date = db.Column(db.String(10), nullable=False)

    sub_event_final_date = db.Column(db.String(10), nullable=False)

    sub_event_initial_hour = db.Column(db.String(8), nullable=False)

    sub_event_final_hour = db.Column(db.String(8), nullable=False)

    sub_event_seats_number = db.Column(db.Integer, nullable=False)

    sub_event_banner = db.Column(
        db.String(45), nullable=False, default='default.jpg')

    # Relation -> 1:1 (Event, SubEvent)
    event_id = db.Column(db.Integer, db.ForeignKey('EVENT.event_id'))

    # Relation -> 1:1 (SubEvent, Local)
    local_id = db.Column(db.Integer, db.ForeignKey('LOCAL.local_id'))

    # Relation -> 1:N (SubEvent, Guest)
    guests = db.relationship('Guest', backref='subevent')

    def __repr__(self):

        sub_event = {
            'sub_event_title': self.sub_event_title,
            'sub_event_description': self.sub_event_description,
            'sub_event_initial_date': self.sub_event_initial_date,
            'sub_event_final_date': self.sub_event_final_date,
            'sub_event_initial_hour': self.sub_event_initial_hour,
            'sub_event_final_hour': self.sub_event_final_hour,
            'sub_event_seats': self.sub_event_seats_number,
        }

        return sub_event


class Local(db.Model):

    __tablename__ = 'LOCAL'

    local_id = db.Column(db.Integer, primary_key=True)

    local_name = db.Column(db.Integer, nullable=False)

    local_latitude = db.Column(db.String(45), nullable=False)

    local_longitude = db.Column(db.String(45), nullable=False)

    # Relation -> 1:1 (Event, Local)
    subevents = db.relationship('Local', backref='local', uselist=False)

    def __repr__(self):
        local = {
            'local_name': self.local_name,
            'local_latitude': self.local_latitude,
            'local_longitude': self.local_longitude,
        }
        return local


class Guest(db.Model):

    __tablename__ = 'GUEST'

    guest_id = db.Column(db.Integer, primary_key=True)

    guest_name = db.Column(db.String(45), nullable=False)

    guest_email = db.Column(db.String(100), nullable=False, unique=True)

    guest_title = db.Column(db.String(45))

    guest_photo = db.Column(db.String(45), nullable=False,
                            default='guest_photo_default.jpg')

    # Relation -> 1:N (SubEvent, Guest)
    subevent_id = db.Column(db.Integer, db.ForeignKey('SUBEVENT.subevent_id'))

    def __repr__(self):

        guest = {
            'guest_name': self.guest_name,
            'guest_title': self.guest_title,
        }
        return guest
