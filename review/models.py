from django.db import models


class Review(models.Model):
    class Meta:
        verbose_name = '대학 리뷰'
        verbose_name_plural = '대학 리뷰'

    university = models.CharField(
            verbose_name='대학명',
            unique=True,
            max_length=20,
            )
    url = models.CharField(
            verbose_name='리뷰 url',
            max_length=50,
            )

    def __str__(self):
        return self.university

