from django.db import models
from multiselectfield import MultiSelectField


REGIONS = (
        ('S', '서울'),
        ('GI', '경인'),
        ('GW', '강원'),
        ('CC', '충청'),
        ('GS', '경상'),
        ('JL', '전라'),
        ('JJ', '제주'),
        )
MOONIGWA = (
        ('MG', '문과'),
        ('IG', '이과'),
        ('YCN', '예체능'),
        )


class University(models.Model):
    name = models.CharField(
            verbose_name='대학명',
            unique=True,
            max_length=31,
            )
    logo = models.ImageField(
            verbose_name='대학 로고',
            blank=True,
            upload_to='university/logo'
            )
    region = models.CharField(
            verbose_name='소재 지역',
            choices=REGIONS,
            max_length=31,
            )

    def __str__(self):
        return self.name


class College(models.Model):
    university = models.ForeignKey(
            verbose_name='소속 대학',
            to='University',
            on_delete=models.CASCADE,
            )
    name = models.CharField(
            verbose_name='단과대명',
            unique=True,
            max_length=31,
            )

    def __str__(self):
        return self.university.name + ' ' + self.name


class Major(models.Model):
    college = models.ForeignKey(
            verbose_name='소속 단과대',
            to='College',
            on_delete=models.CASCADE,
            )
    name = models.CharField(
            verbose_name='학과명',
            unique=True,
            max_length=31,
            )
    moonigwa = MultiSelectField(
            verbose_name='계열',
            choices=MOONIGWA,
            max_length=7,
            )

    def __str__(self):
        return self.college.university.name + ' ' + self.college.name + ' ' + self.name


