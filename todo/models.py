from django.db import models


class Todo (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=50, default='', blank=True)
    is_done = models.BooleanField(default=False)
    due_date = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE, default='', blank=True)

    class Meta:
        ordering = ['created']
