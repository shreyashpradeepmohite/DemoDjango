from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    pdf_file = models.FileField(upload_to='pdf_files/')
    text_content = models.TextField()