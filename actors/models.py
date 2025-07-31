from django.db import models


class Nationality(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome da Nacionalidade"
    )

    class Meta:
        verbose_name = "Nacionalidade"
        verbose_name_plural = "Nacionalidades"
        ordering = ['name']

    def __str__(self):
        return self.name


class ActorModel(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Nacionalidade"
    )

    def __str__(self):
        return self.name
