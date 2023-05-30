

from intermediate_control_work import userInstruction, notesFunctions


def run():
    play = True
    while play:
        print(f"{'*' * 20}")
        answer = input("This is the Notes app. You can use the following functions:\n"
                       "1. Show all notes\n"
                       "2. Add a note\n"
                       "3. Delete the note\n"
                       "4. Change the note\n"
                       "5. Selection by date\n"
                       "6. Selection by id\n"
                       "7. Exit\n")
        match answer:
            case "1":
                notesFunctions.show('all')
            case "2":
                notesFunctions.add()
            case "3":
                notesFunctions.show('all')
                notesFunctions.id_edit_del_show('del')
            case "4":
                notesFunctions.show('all')
                notesFunctions.id_edit_del_show('edit')
            case "5":
                notesFunctions.show('date')
            case "6":
                notesFunctions.show('id')
                notesFunctions.id_edit_del_show('show')
            case "7":
                userInstruction.farewell()
                play = False
            case _:
                print("Try again!\n")

