import datetime

from django.db import models

from university.models import *


YEARS = []
for r in range(1970, (datetime.datetime.now().year+2)):
    YEARS.append((r,r))


SUSI_TYPES = (
        ('HJ', '학생부 종합전형'),
        ('HG', '학생부 교과전형'),
        ('NS', '논술전형'),
        ('SG', '실기전형'),
        ('GG', '기회균등전형'),
        )


class Susi(models.Model):
    university = models.ForeignKey(
            verbose_name='대학',
            to='university.University',
            on_delete=models.CASCADE,
            )
    name = models.CharField(
            verbose_name='전형명',
            max_length=31,
            )
    year = models.IntegerField(
            verbose_name='학년도',
            choices=YEARS,
            )
    susi_type = models.CharField(
            verbose_name='전형 종류',
            choices=SUSI_TYPES,
            max_length=31,
            )

    def __str__(self):
        return str(self.year) + '학년도 ' + self.university.name + ' ' + self.name


class SusiDetail(models.Model):
    susi = models.ForeignKey(
            verbose_name='수시전형',
            to='Susi',
            on_delete=models.CASCADE,
            )
    major = models.ManyToManyField(
            verbose_name='학과',
            to=Major,
            )
    required_documents = models.TextField(
            verbose_name='필요 서류',
            blank=True,
            )
    min_grade = models.TextField(
            verbose_name='수능 최저등급',
            )

    def __str__(self):
        return str(self.susi.year) + '학년도 ' + self.susi.university.name + ' ' + self.susi.name + ' ' + str(self.id)


class SusiSchedule(models.Model):
    susi_detail = models.ForeignKey(
            verbose_name='수시전형 종류',
            to='SusiDetail',
            on_delete=models.CASCADE,
            )
    description = models.CharField(
            verbose_name='설명',
            max_length=255,
            )
    start_date = models.DateTimeField(
            verbose_name='시작시간',
            )
    end_date = models.DateTimeField(
            verbose_name='종료시간',
            )

    def __str__(self):
        return str(self.susi_detail.susi.year) + '학년도 ' + self.susi_detail.susi.university.name + ' ' + self.susi_detail.susi.name + ' ' + str(self.susi_detail.id) + ' 일정 ' + str(self.id)

