from django.db import models


class Suneung(models.Model):
    class Meta:
        verbose_name = '수능 및 모의고사 일정'
        verbose_name_plural = '수능 및 모의고사 일정'

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
        return self.description

