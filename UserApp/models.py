from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('text', 'Text'),
        ('video', 'Video'),
        ('image', 'Image'),
        # Add more choices for other resource types as needed
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    file = models.FileField(upload_to='resources/', null=True, blank=True)
    # You can add more fields specific to each resource type.

    def __str__(self):
        return self.title

class Documentary(models.Model):
    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(default= '')
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    def __str__(self):
        return self.title

class DocumentarySector(models.Model):
    documentary = models.ForeignKey(Documentary, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    rich_content = models.TextField(blank=True)
    def __str__(self):
        return self.title
    
class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_badge = models.ImageField()
    def __str__(self):
        return self.name
    
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documentarysector = models.ForeignKey(DocumentarySector,models.DO_NOTHING, null = True)
    completed = models.BooleanField(default=False)
    quiz_score = models.IntegerField(null=True, blank=True)
    # You can add more fields like time spent, badges, etc.

    def __str__(self):
        return f"{self.user.username} - {self.documentarysector.title}"
    
class Document(models.Model):
    file = models.FileField(upload_to='documents/')    