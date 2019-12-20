from django.db import models


class q_a(models.Model):
    Question = models.CharField(max_length=255)
    Answer1 = models.CharField(max_length=255)
    Answer2 = models.CharField(max_length=255)
    Answer3 = models.CharField(max_length=255)
    Answer4 = models.CharField(max_length=255)
    CorAns = models.CharField(max_length=255)
