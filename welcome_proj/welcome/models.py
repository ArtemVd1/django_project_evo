from django.db import models


class User(models.Model):
    """User Model"""
    first_name = models.CharField(max_length=256,
                                  blank=False,
                                  verbose_name="Ім'я"
                                  )
    last_name = models.CharField(max_length=256,
                                 blank=False,
                                 verbose_name="Прізвище"
                                 )

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    class Meta:
        verbose_name = "Гість"
        verbose_name_plural = "Гості"
