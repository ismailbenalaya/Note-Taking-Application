# Note-Taking Application

This is a Python-based **Note-Taking Application** designed to manage and organize your notes efficiently. The application uses a simple command-line interface (CLI) to perform actions such as adding, editing, deleting, and displaying notes. It is built using the `dataclasses` module for simplicity and clarity.

## Features

- **Add Notes**: Create new notes by providing a title and body.
- **Edit Notes**: Modify the title or body of an existing note.
- **Delete Notes**: Remove a note from your collection.
- **View Notes**: Display all existing notes in the application.
- **Unique Note ID**: Each note is assigned a unique identifier using the `uuid` module.

## Technologies Used

- Python 3.10+
- `dataclasses` for structured data representation.
- `uuid` for generating unique IDs for notes.

## How to Run the Application

### Prerequisites

- Install Python 3.10 or higher.

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/ismailbenalaya/Note-Taking-Application.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Note-Taking-Application
    ```

3. Run the application:
    ```bash
    python note_app.py
    ```

4. Follow the on-screen instructions to interact with the application.

## How It Works

### Structure

- **`Note` Class**:
  - Represents a single note with a `title`, `body`, and a unique `id`.
  - Automatically generates a unique `id` for each note upon creation.

- **`NoteApp` Class**:
  - Manages a collection of notes.
  - Provides methods to add, edit, delete, and display notes.

### User Interaction

- The application runs in an infinite loop.
- Users select actions by entering a command number (1-4).
- Invalid inputs are handled gracefully to ensure a smooth experience.

### Commands

1. **Add Note**: Create a new note by providing a title and body.
2. **Edit Note**: Modify an existing note by selecting its index.
3. **Delete Note**: Remove a note by selecting its index.
4. **Display Notes**: View all saved notes.

## Example Output

```plaintext
Welcome To Notes!
Here are the commands:
1 - Add new note
2 - Edit note
3 - Delete note
4 - Display all notes
YOU: 1
Title: Shopping List
Body: Buy milk and eggs
Note was added!
YOU: 4
[1] Shopping List: Buy milk and eggs
YOU: 2
Which note would you like to edit?
[1] Shopping List: Buy milk and eggs
Index: 1
New Title: Updated Shopping List
New Body: Buy milk, eggs, and bread
Note was updated!
YOU: 4
[1] Updated Shopping List: Buy milk, eggs, and bread
```

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, feel free to reach out to me:

- **Name**: Mohamed Ismail
- **GitHub**: [https://github.com/ismailbenalaya](https://github.com/ismailbenalaya)

