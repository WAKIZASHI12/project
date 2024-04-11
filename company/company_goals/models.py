from django.db import models
  
class CompanyGoal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    is_achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
  