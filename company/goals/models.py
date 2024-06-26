from django.db import models

class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_data = models.DateField()
    
    def __str__(self):
        return self.name
    