from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Note


class NoteForm(forms.Form):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
        fields = ['name', 'text', 'creator', 'collaborators', 'is_private', 'link', 'color', 'category', 'group']
