from django import forms
from django.forms import ModelForm
from . models import Note

CATEGORY = (
    ('ho', 'home'),
    ('pe', 'personal'),
    ('wo', 'work'),
)
class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('note_info','category',)
        labels = {
            'note_info': '',
        }
        widgets = {
            'note_info': forms.Textarea(attrs={
                    'class': 'form-control mb-2 pl-2 pr-2',
                    'placeholder': 'write your note here',
                    'style': 'background: #ffdcdc',
                    'rows': 6,
                    'required':'required'
                }),
            'category': forms.Select(choices=CATEGORY, attrs={
                'class': 'form-control',
                'style': 'background: #ffdcdc;',
            })
        }

