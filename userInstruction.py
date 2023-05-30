from intermediate_control_work.Note import Note

number = 6  # Минимальное количество знаков в тексте заметке


def create_note(number):
    heading = check_length_text_input(
        input('Enter the name of the note: '), number)
    body = check_length_text_input(
        input('Enter the text of the note: '), number)
    return Note(heading=heading, body=body)


def check_length_text_input(text, n):
    while len(text) <= n:
        print(f'Еhe text must contain more than {n} characters\n')
        text = input('Enter the text: ')
    else:
        return text


def farewell():
    print("See you!")
