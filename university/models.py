from django.db import models


class University(models.Model):
    class Meta:
        verbose_name = '대학'
        verbose_name_plural = '대학'

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
    review_url = models.CharField(
            verbose_name='리뷰 url',
            blank=True,
            max_length=63,
            )

    def __str__(self):
        return self.name


class SusiMajorBlock(models.Model):
    class Meta:
        verbose_name = '수시 학과 블록'
        verbose_name_plural = '수시 학과 블록'

    university = models.ForeignKey(
            verbose_name='소속 대학',
            to='University',
            related_name='susi_major_blocks',
            on_delete=models.CASCADE,
            )
    name = models.CharField(
            verbose_name='분류명',
            max_length=255,
            )

    def __str__(self):
        return self.university.name + '/' + self.name


class JeongsiMajorBlock(models.Model):
    class Meta:
        verbose_name = '정시 학과 블록'
        verbose_name_plural = '정시 학과 블록'

    university = models.ForeignKey(
            verbose_name='소속 대학',
            to='University',
            related_name='jeongsi_major_blocks',
            on_delete=models.CASCADE,
            )
    name = models.CharField(
            verbose_name='분류명',
            max_length=255,
            )

    def __str__(self):
        return self.university.name + '/' + self.name

