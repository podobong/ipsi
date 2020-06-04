import datetime

from django.db import models

from university.models import *


YEARS = []
for r in range(2021, (datetime.datetime.now().year+2)):
    YEARS.append((r,r))


class Susi(models.Model):
    class Meta:
        verbose_name = '수시전형'
        verbose_name_plural = '수시전형'

    university = models.ForeignKey(
            verbose_name='대학',
            to='university.University',
            related_name='susis',
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

    def __str__(self):
        return str(self.year) + '학년도 ' + self.university.name + ' 수시전형 (' + self.name + ')'
        # ex) 2021학년도 서울대학교 수시전형 (일반전형)


class SusiSchedule(models.Model):
    class Meta:
        verbose_name = '수시전형 일정'
        verbose_name_plural = '수시전형 일정'

    susi = models.ForeignKey(
            verbose_name='수시전형 종류',
            to='Susi',
            related_name='susi_schedules',
            on_delete=models.CASCADE,
            )
    major_block = models.ForeignKey(
            verbose_name='학과 블록',
            to='university.SusiMajorBlock',
            related_name='susi_schedules',
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
        return str(self.susi.year) + '학년도 ' + self.susi.university.name + ' 수시전형 (' + self.susi.name + ') 일정: ' + self.description + ' (' + self.major_block.name + ')'
        # ex) 2021학년도 서울대학교 수시전형 (일반전형) 일정: 지원서 접수 (의과대학, 수의과대학, 치의과대학)

