from django.db import models


class Subjects(models.Model):
    subject_text = models.CharField(max_length=200)
    hit_count = models.IntegerField(default=0)

