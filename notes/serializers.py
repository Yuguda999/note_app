from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'markdown_file', 'html_content', 'created_at']
        read_only_fields = ['html_content', 'created_at']
