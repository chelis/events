# -*- coding: utf-8 -*-
# @Author: Marcela Campo
# @Date:   2016-05-06 18:23:46
# @Last Modified by:   Marcela Campo
# @Last Modified time: 2016-05-12 20:32:48
from server import db
from sqlalchemy.dialects.postgresql import JSON
import datetime
from collections import OrderedDict

class EventType(db.Model):
    __tablename__ = 'event_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    events = db.relationship('Event',
        backref=db.backref('event_type_name', lazy='joined'), lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<EventType id {}>'.format(self.id)

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.Integer, db.ForeignKey('event_type.id'))
    notes = db.Column(db.String())
    date = db.Column(db.DateTime())
    user = db.Column(db.String())


    def __init__(self, user, event_type, notes, date=None):
        self.user = user
        self.event_type = event_type
        self.notes = notes
        self.date = date or datetime.datetime.utcnow()
        self.user = user

    def __repr__(self):
        return '<Event id {}  user {} event_type  {} date {}>'.format(self.id, self.user, str(self.event_type_name) if self.event_type else '', self.date or '')

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if isinstance(value, datetime.datetime):
                    value = value.isoformat()

            result[key] = value

        if self.event_type:
            result['event_type_name'] = self.event_type_name.name
        return result


