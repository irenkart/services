from django.db import models


# Create your models here.
class Services(models.Model):
    name = models.CharField(verbose_name=u'Название услуги', max_length=20)
    price_before_100 = models.FloatField(verbose_name=u'Цена до 100')
    price_after_100 = models.FloatField(verbose_name=u'Цена после 100')
    old = models.BooleanField(verbose_name=u'Архив', default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + str(self.date_created)


class ServicesUrls(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=20)
    url = models.URLField(verbose_name=u'URL')

    def __str__(self):
        return self.name
