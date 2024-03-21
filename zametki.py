import json
import datetime
import os


def save_notes(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file)


def load_notes(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return json.load(file)


def add_note(notes, title, msg):
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": msg,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    return notes


def edit_note(notes, note_id, title, msg):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = msg
            note["timestamp"] = str(datetime.datetime.now())
            break
    return notes


def delete_note(notes, note_id):
    notes = [note for note in notes if note["id"] != note_id]
    return notes


def filter_notes_by_date(notes, date):
    filtered_notes = []
    for note in notes:
        if date in note["timestamp"]:
            filtered_notes.append(note)
    return filtered_notes


def print_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Message: {note['message']}")
        print(f"Timestamp: {note['timestamp']}")
        print()


def main():
    filename = "notes.json"
    notes = load_notes(filename)

    while True:
        print("Выберите команду:")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Показать заметки по дате")
        print("6. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            print_notes(notes)
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            notes = add_note(notes, title, msg)
            save_notes(notes, filename)
            print("Заметка успешно сохранена")
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            msg = input("Введите новое тело заметки: ")
            notes = edit_note(notes, note_id, title, msg)
            save_notes(notes, filename)
            print("Заметка успешно отредактирована")
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = delete_note(notes, note_id)
            save_notes(notes, filename)
            print("Заметка успешно удалена")
        elif choice == "5":
            date = input("Введите дату для фильтрации (гггг-мм-дд): ")
            filtered_notes = filter_notes_by_date(notes, date)
            print_notes(filtered_notes)
        elif choice == "6":
            break
        else:
            print("Некорректная команда, попробуйте снова.")


if __name__ == "__main__":
    main()
