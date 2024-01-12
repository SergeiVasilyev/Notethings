from django import forms
from django_editorjs_fields import EditorJsWidget
from .models import Note


# class NoteForm(forms.Form):
#     text = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Note
#         fields = ['name', 'text', 'creator', 'collaborators', 'is_private', 'link', 'color', 'category', 'group']




class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['category', 'collaborators', 'color', 'creator', 'is_private', 'link', 'group']
        fields = ['name', 'text']
        widgets = {
            'text': EditorJsWidget(config={'minHeight': 100}),
        }