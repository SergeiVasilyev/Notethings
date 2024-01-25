from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Note


class NoteForm(forms.ModelForm):
    # text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
        fields = ['name', 'text', 'creator',]
