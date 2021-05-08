from django.db import models


class ComprasItem(models.Model):

    nome = models.CharField(max_length=60)
    quantidade = models.PositiveSmallIntegerField()
    check = models.BooleanField(default=False)