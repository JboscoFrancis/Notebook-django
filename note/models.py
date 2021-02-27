from django.db import models

# Create your models here.

CATEGORY = (
    ('ho', 'home'),
    ('pe', 'personal'),
    ('wo', 'work'),
)

class Note(models.Model):
    note_info = models.TextField(max_length=200, null=True)
    category = models.CharField(choices=CATEGORY, default='ho', max_length=2)
    complete = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def label(self):
        if self.category == 'ho':
            label = 'primary'
        elif self.category == 'pe':
            label = 'success'
        else:
            label = 'warning'
        
        return label

    def __str__(self):
        return self.note_info