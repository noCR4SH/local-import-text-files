from note_manager import add_note, list_notes

while True:
    print("\nNote-taking Application")
    print("1. Add Note")
    print("2. List Notes")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Write your note: ")
        add_note(note)
        print("Note added successfully!")
    elif choice == "2":
        notes = list_notes()
        print("\nNotes:")
        for note in notes:
            print(f"- {note}")
        if not notes:
            print("No notes found.")
    elif choice == "3":
        print("Exiting application")
        break
    else:
        print("Invalid option!")