import json
import os
import datetime


NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
        return notes
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(title, message):
    notes = load_notes()
    note_id = len(notes) + 1
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": note_id,
        "title": title,
        "message": message,
        "timestamp": current_time
    }
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"Заметка {note['id']}:")
        print(f"Заголовок: {note['title']}")
        print(f"Сообщение: {note['message']}")
        print(f"Дата/время: {note['timestamp']}")
        print("-" * 20)

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print(f"Заметка {note_id} удалена")

def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Удалить заметку")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите номер заметки для удаления: "))
            delete_note(note_id)
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
