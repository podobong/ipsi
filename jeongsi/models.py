from django.db import models

from university.models import *
from susi.models import YEARS


GUNS = (
        ('GA', '가군'),
        ('NA', '나군'),
        ('DA', '다군'),
        ('ETC', '군외'),
       )


class Jeongsi(models.Model):
    class Meta:
        verbose_name = '정시전형'
        verbose_name_plural = '정시전형'

    university = models.ForeignKey(
            verbose_name='대학',
            to='university.University',
            related_name='jeongsis',
            on_delete=models.CASCADE,
            )
    year = models.IntegerField(
            verbose_name='학년도',
            choices=YEARS,
            )
    gun = models.CharField(
            verbose_name='군',
            choices=GUNS,
            max_length=7,
            )

    def __str__(self):
        return str(self.year) + '학년도 '+ self.university.name + ' 정시전형 (' + self.gun + ')'
        # ex) 2021학년도 서울대학교 정시전형 (가군)


class JeongsiSchedule(models.Model):
    class Meta:
        verbose_name = '정시전형 일정'
        verbose_name_plural = '정시전형 일정'

    jeongsi = models.ForeignKey(
            verbose_name = '정시전형 종류',
            to='Jeongsi',
            related_name='jeongsi_schedules',
            on_delete=models.CASCADE,
            )
    major_block = models.ForeignKey(
            verbose_name='학과 블록',
            to='university.JeongsiMajorBlock',
            related_name='jeongsi_schedules',
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
        return str(self.jeongsi.year) + '학년도 ' + self.jeongsi.university.name + ' 정시전형 (' + self.jeongsi.gun + ') 일정: ' + self.description + ' (' + self.major_block.name + ')'
        # ex) 2021학년도 서울대학교 정시전형 (가군) 일정: 지원서 접수 (의과대학, 수의과대학, 치의과대학)

