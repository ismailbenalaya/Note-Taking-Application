from dataclasses import dataclass, field  # Import necessary modules for data classes and fields.
from uuid import uuid4, UUID  # Import `uuid4` and `UUID` for unique identifiers.


# Define the Note class using a dataclass for simplified initialization and representation.
@dataclass
class Note:
    id: UUID = field(init=False)  # Automatically generate a unique ID when a Note object is created.
    title: str  # Title of the note.
    body: str  # Body of the note.

    # Post-initialization to set the `id` field to a new UUID.
    def __post_init__(self) -> None:
        self.id = uuid4()


# Define the NoteApp class to manage notes.
class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None) -> None:
        """
        Initialize the NoteApp with an author and an optional list of notes.
        If no notes are provided, initialize with an empty list.
        """
        self.author = author  # Store the author's name.
        if notes is None:
            self._notes = []  # Initialize an empty list of notes if none are provided.
        else:
            self._notes = notes  # Use the provided notes.

        # Display instructions when the app starts.
        self.display_instructions()

    @staticmethod
    def display_instructions() -> None:
        """Static method to display the app instructions."""
        print("Welcome To Notes!")
        print("Here are the commands:")
        print('1 - Add new note')
        print("2 - Edit note")
        print('3 - Delete note')
        print("4 - Display all notes")

    def _add_note(self) -> None:
        """Add a new note by taking user input for title and body."""
        title: str = input('Title: ')
        body: str = input('Body: ')
        # Validate input; both title and body must not be empty.
        if title == "" and body == "":
            print("You have to enter a real value.")
        else:
            # Create a new note and append it to the list.
            note: Note = Note(title, body)
            self._notes.append(note)
            print('Note was added!')

    def _edit_note(self) -> None:
        """Edit an existing note selected by the user."""
        print("Which note would you like to edit?")
        self._show_notes()  # Display all notes with indices.
        try:
            # Prompt the user to select a note index.
            note_ind: int = int(input('Index: ')) - 1
            current: Note = self._notes[note_ind]  # Fetch the selected note.

            # Get new title and body for the note.
            new_title: str = input('New Title: ')
            new_body: str = input('New Body: ')

            # Update the note's content.
            current.title = new_title
            current.body = new_body

            print('Note was updated!')
        except IndexError:
            print('Please select a valid index...')
            self._edit_note()  # Retry editing.
        except ValueError:
            print('Index cannot be empty...')
            print('Aborting operation...')

    def _delete_note(self) -> None:
        """Delete a note selected by the user."""
        print("Which note would you like to delete?")
        self._show_notes()  # Display all notes with indices.
        try:
            # Prompt the user to select a note index.
            note_ind: int = int(input('Index: ')) - 1
            del self._notes[note_ind]  # Delete the selected note.
            print('Note was deleted!')
        except IndexError:
            print('Please select a valid index...')
            self._delete_note()  # Retry deletion.
        except ValueError:
            print('Index cannot be empty...')
            print('Aborting operation...')

    def _show_notes(self) -> None:
        """Display all notes with their indices."""
        if not self._notes:  # Check if there are no notes.
            print('No notes...')
            return
        # Display each note with its index.
        for i, note in enumerate(self._notes, start=1):
            print(f'[{i}] {note.title}: {note.body}')

    def _select_option(self, user_input: str) -> None:
        """Handle user input and execute the corresponding action."""
        if user_input not in ['1', '2', '3', '4']:  # Validate input.
            print('Please pick a valid option.')
            return
        # Map user input to the corresponding method.
        if user_input == "1":
            self._add_note()
        elif user_input == "2":
            self._edit_note()
        elif user_input == "3":
            self._delete_note()
        elif user_input == "4":
            self._show_notes()

    def run_app(self) -> None:
        """Run the app in a loop, allowing the user to interact with it."""
        while True:
            user_input: str = input('YOU: ')
            self._select_option(user_input)


# Main function to initialize and run the NoteApp.
def main() -> None:
    # Create sample notes for the app.
    sample_notes: list[Note] = [
        Note(title='Title1', body='Hello there, Bob!!'),
        Note(title='Title2', body='More text')
    ]
    # Instantiate the NoteApp with an author and sample notes.
    note_app: NoteApp = NoteApp(author='Bob', notes=sample_notes)
    # Start the app.
    note_app.run_app()


# Entry point of the script.
if __name__ == '__main__':
    main()
