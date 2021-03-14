from django.db import models

class Corona(models.Model):
    uf = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    suspects = models.IntegerField()

    def __str__(self):
        return self.uf