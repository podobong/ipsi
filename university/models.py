from django.db import models


class University(models.Model):
    name = models.CharField(
            verbose_name='대학명',
            unique=True,
            max_length=31,
            )
    logo = models.CharField(
            verbose_name='대학 로고',
            blank=True,
            max_length=31,
            )

    def __str__(self):
        return self.name


class Major(models.Model):
    university = models.ForeignKey(
            verbose_name='소속 대학',
            to='University',
            related_name='majors',
            on_delete=models.CASCADE,
            )
    name = models.CharField(
            verbose_name='학과명',
            unique=True,
            max_length=31,
            )

    def __str__(self):
        return self.university.name + ' ' + self.name


