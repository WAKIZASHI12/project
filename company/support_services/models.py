from django.db import models


class SupportRequest(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='open')

    def __str__(self):
        return self.subject