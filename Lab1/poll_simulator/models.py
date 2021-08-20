from django.db import models

class Candidates(models.Model):
    candidate = models.CharField(max_length=50, blank=True, null=True, unique=True)\

    def __str__(self):
        return str(self.candidate)


class Vote(models.Model):
    studentid = models.IntegerField(max_length=20, blank=True, null=True, unique=True)
    nominee = models.ForeignKey(Candidates, on_delete=models.CASCADE)


