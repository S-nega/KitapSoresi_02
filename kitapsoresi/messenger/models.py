from django.db import models

# Create your models here.
class Message(models.Model):
    authorid = models.IntegerField(max_length=50)
    readerid = models.IntegerField(max_length=50)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    text = models.TextField(blank=True)
    status = models.BooleanField(auto_now=False)

    def __str__(self):
        return self.readerid