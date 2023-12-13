from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Folder(models.Model):
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
    text = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    coeditors = models.ManyToManyField(CustomUser, related_name='coeditors')
    color = models.CharField(max_length=10, choices=COLORS, default='yellow')
    category = models.ManyToManyField(Category, related_name='category', default=None)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, default=None, blank=True, null=True)

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
    
    @classmethod
    def create_note(cls, name=None, text=None, creator=None, category=None, folder=None): 
        name = cls.name_validator(name, text)
        note = cls.objects.create(name=name, text=text, creator=creator, folder=folder)
        if category: note.category.set(category)
        return note