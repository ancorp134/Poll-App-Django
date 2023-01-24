from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    user = models.ForeignKey(User , on_delete =models.CASCADE)

    def __str__(self):
        return self.question
