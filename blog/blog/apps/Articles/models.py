import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    name_article = models.CharField("ім'я статьї", max_length=150)
    text_article = models.TextField('Текст статьї')
    pub_date = models.DateTimeField('дата публікації стітьї')

    def __str__(self):
        return self.name_article

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=5))

    class Meta:
        verbose_name ='Статья'
        verbose_name_plural ='Статьї'

class Comment(models.Model):
    articale = models.ForeignKey(Article, on_delete=models.CASCADE)
    name_user = models.CharField("ім'я користувача", max_length=40)
    text_comment = models.TextField('Самий коментарії')
    date_comment = models.DateTimeField('дата публікації коментарія')

    def __str__(self):
        return self.name_user

    def was_published_recently(self):
        return self.date_comment >= (timezone.now() - datetime.timedelta(days=2))

    class Meta:
        verbose_name ='Коментарій'
        verbose_name_plural ='Коментарії'