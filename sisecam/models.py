from django.db import models

class Piles(models.Model):
    sorszam = models.CharField(max_length=20)
    terulet = models.CharField(max_length=100)
    kivitelezett_hossz = models.FloatField()

    def __str__(self):
        return f"{self.sorszam} - {self.terulet} - {self.kivitelezett_hossz}"

    class Meta:
        verbose_name = "Cölöp"
        verbose_name_plural = "Cölöpök"