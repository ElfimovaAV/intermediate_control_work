from intermediate_control_work import userInstruction, editFile
from intermediate_control_work.Note import Note
from intermediate_control_work.userInstruction import number

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = userInstruction.create_note(number)
    array = editFile.read_file()
    for notes in array:
        if Note.get_id(note) == Note.get_id(note):
            Note.set_id(note)
    array.append(note)
    editFile.write_file(array, 'a')
    print('The note added...')


def show(text):
    logic = True
    array = editFile.read_file()
    if text == 'date':
        date = input('Enter date in format dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.get_date(notes):
                print(Note.map_note(notes))
    if logic == True:
        print('There is not a single note...')


def id_edit_del_show(text):
    id = input('Enter the id of the selected note: ')
    array = editFile.read_file()
    logic = True
    for notes in array:
        if id == Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = userInstruction.create_note(number)
                Note.set_heading(notes, note.get_heading())
                Note.set_body(notes, note.get_body())
                Note.set_date(notes)
                print('The note changed...')
            if text == 'del':
                array.remove(notes)
                print('The note deleted...')
            if text == 'show':
                print(Note.map_note(notes))
    if logic == True:
        print('There is no such note, perhaps you entered the wrong id')
    editFile.write_file(array, 'a')
