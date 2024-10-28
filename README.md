
# Note-Taking App

A simple note-taking application built with Django and Django REST Framework that allows users to upload markdown files, check grammar, save notes, and render them as HTML. This project is designed to help users manage markdown notes while exploring key functionalities of Django REST API development, file uploads, markdown parsing, and grammar checking. 
**https://roadmap.sh/projects/markdown-note-taking-app**

## Features

- **Markdown File Upload**: Upload notes in markdown format.
- **Grammar Check**: Integrates with LanguageTool API to check for grammar errors.
- **HTML Rendering**: Converts markdown notes to HTML for easy viewing.
- **File Handling**: Demonstrates handling of file uploads and parsing in Django REST framework.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Grammar Check**: LanguageTool API
- **Markdown Parsing**: Python-Markdown library

## Installation

### Prerequisites

- Python 3.7+
- Django 4.0+
- `pip` package manager

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/note-taking-app.git
   cd note-taking-app
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Django Database**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Visit `http://127.0.0.1:8000` in your browser.

## API Endpoints

- **POST** `/api/notes/` - Upload a new markdown file, save the note, check grammar, and render HTML.
- **GET** `/api/notes/` - Retrieve a list of all notes.
- **GET** `/api/notes/<id>/` - Retrieve a specific note by ID.

## Example Usage

To upload a note, send a `POST` request with a markdown file using a tool like [Postman](https://www.postman.com/) or `curl`.

```bash
curl -X POST -F "title=Sample Note" -F "markdown_file=@path/to/your_note.md" http://127.0.0.1:8000/api/notes/
```

This request will return:
- `id`: The note ID.
- `title`: Title of the note.
- `html_content`: HTML rendering of the markdown file.
- `grammar_issues`: A list of grammar issues found in the note.

## Project Structure

```plaintext
note_taking_app/
│
├── notes/                   # App for note management
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates for viewing notes
│   ├── __init__.py          # App initialization
│   ├── models.py            # Note model
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views
│   ├── urls.py              # App URLs
│
├── note_taking_app/         # Main project directory
│   ├── settings.py          # Project settings
│   ├── urls.py              # Project URLs
│   └── wsgi.py              # WSGI entry point
│
├── manage.py                # Django management tool
└── requirements.txt         # Python package requirements
```

## Dependencies

- Django
- Django REST Framework
- requests
- markdown

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any feature requests or bug reports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Happy Coding!**
