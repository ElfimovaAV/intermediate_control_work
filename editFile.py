from intermediate_control_work.Note import Note


def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for note in array:
        file.write(Note.to_string(note))
        file.write('\n')
    file.close


def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        note = file.read().strip().split("\n")
        for n in note:
            split_n = n.split(';')
            note = Note(
                id=split_n[0], heading=split_n[1], body=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('No saved notes...')
    finally:
        return array
