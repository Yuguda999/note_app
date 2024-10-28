from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    markdown_file = models.FileField(upload_to='markdown_files/')
    html_content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
