from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' | ' + str(self.completed)
