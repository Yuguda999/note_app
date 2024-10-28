import markdown
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from notes.services.grammar_check import check_grammar
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        # Use the serializer to validate and save the uploaded data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = serializer.save()

        # Read the uploaded markdown file content with error handling for encoding issues
        try:
            with open(note.markdown_file.path, 'r', encoding='utf-8', errors='replace') as f:
                markdown_content = f.read()
        except UnicodeDecodeError:
            return Response({"error": "Unable to decode the uploaded file. Please ensure it is UTF-8 encoded."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Grammar check
        grammar_issues = check_grammar(markdown_content)

        # Render markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Save HTML content to the note
        note.html_content = html_content
        note.save()

        # Return the custom response with grammar issues and HTML content
        return Response({
            "id": note.id,
            "title": note.title,
            "html_content": html_content,
            "grammar_issues": grammar_issues
        }, status=status.HTTP_201_CREATED)
