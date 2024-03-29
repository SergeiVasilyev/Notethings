from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models.query import QuerySet
from django.template.defaulttags import register
from django_quill.fields import QuillField, FieldQuill, QuillDescriptor
from .html_to_delta import convert_html_to_delta
import json


class CustomUser(AbstractUser, PermissionsMixin):
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class CustomFieldQuill(FieldQuill):
    def __init__(self, instance, field, json_string):
        super().__init__(instance, field, json_string)

    @property
    def html(self):
        self._require_quill()
        try:
            text = self.quill.html
        except:
            text = self.json_string
        return text
    
class CustomQuillField(QuillField):
    attr_class = CustomFieldQuill
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

class Note(models.Model):
    COLORS = (
        ('yellow', 'yellow'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('red', 'red'),
        ('pink', 'pink'),
        ('purple', 'purple'),
        ('orange', 'orange'),
    )

    name = models.CharField(max_length=100, blank=True, null=True)
    text = CustomQuillField(blank=True, null=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(CustomUser, related_name='collaborators')
    is_private = models.BooleanField(default=True)
    link = models.URLField(unique=True, blank=True, null=True)
    color = models.CharField(max_length=10, choices=COLORS, default='yellow')
    category = models.ManyToManyField(Category, related_name='category', default=None)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def name_validator(name, text):
        if not name:
            if text:
                name = text[:100]
        return name
    
    @property
    def html(self):
        # print(self.text.html)
        try:
            text = self.text.html
        except:
            text = ''
        return text


    
    @classmethod
    def create_note(cls, name=None, text=None, creator=None, category=None, group=None, updated_at=None): 
        name = cls.name_validator(name, text)
        note = cls.objects.create(name=name, text=text, creator=creator, group=group, updated_at=updated_at)
        if category: note.category.set(category)
        return note