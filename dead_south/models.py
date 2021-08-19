from django.db import models

class Article(models.Model):
    source_text = models.JSONField()
    source_url = models.URLField(primary_key=True)
    output_text = models.JSONField()
    title = models.TextField(default='title')

    class Meta:
        indexes = [
            models.Index(fields=['source_url']),
        ]
