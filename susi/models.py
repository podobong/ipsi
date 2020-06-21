import datetime

from django.db import models

from university.models import University, SusiMajorBlock


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
        return str(self.year) + '/' + self.university.name + '/수시전형/' + self.name
        # ex) 2021/서울대학교/수시전형/일반전형


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

    university = models.CharField(
            max_length=31,
            default='',
            editable=False,
    )
    sj = models.CharField(
            max_length=15,
            default='수시',
            editable=False,
    )
    jh = models.CharField(
            max_length=63,
            default='',
            editable=False,
    )
    block = models.CharField(
            max_length=63,
            default='',
            editable=False,
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

    def save(self, **kwargs):
        self.university = self.susi.university.name
        self.sj = '수시'
        self.jh = self.susi.name
        self.block = self.major_block.name
        super().save()

    def __str__(self):
        return str(self.susi.year) + '/' + self.susi.university.name + '/수시전형/' + self.susi.name + '/' + self.description + '/' + self.major_block.name
        # ex) 2021/서울대학교/수시전형/일반전형/지원서 접수/의과대학, 수의과대학, 치의과대학
