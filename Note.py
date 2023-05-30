import uuid
from datetime import datetime


class Note:

    def __init__(self, id=str(uuid.uuid1())[0:3], heading="heading",
                 body="Ten little nigger boys went out to dine; One choked his little self, and then there were nine.",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.heading = heading
        self.body = body
        self.date = date

    def get_id(note):
        return note.id

    def get_heading(note):
        return note.heading

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def set_heading(note, heading):
        note.heading = heading

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.heading + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Title: ' + note.heading + '\n' + 'Content: ' + note.body + '\n' + 'Public date: ' + note.date
