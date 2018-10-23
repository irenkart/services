import requests
import urllib3
import certifi
from bs4 import BeautifulSoup
from main.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = list(ServicesUrls.objects.all())
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        for item in urls:
            if item.name == u'Электричество':
                r = requests.get(item.url)
                status = r.status_code
            else:
                r = http.request('GET', item.url)
                status = r.status
            prev_object = None
            price = None
            if status == 200:
                if item.name == u'Газ':
                    a = BeautifulSoup(r.data, 'html.parser').table.find_all('td')
                    for item in a:
                        if item.has_attr('rowspan'):
                            price = float(item.get_text().replace(',', '.'))
                            break
                    try:
                        prev_object = Services.objects.get(name='Gas', old=False)
                    except:
                        'No previous object'
                    if price is not None:
                        if prev_object is None:
                            Services.objects.create(name='Gas',
                                                    price_before_100=price,
                                                    price_after_100=price)
                        elif prev_object.price_before_100 != price:
                            prev_object.old = True
                            prev_object.save()
                            Services.objects.create(name='Gas',
                                                    price_before_100=price,
                                                    price_after_100=price)
                elif item.name == u'Вода':
                    a = BeautifulSoup(r.data, 'html.parser').table.find_all('th')
                    try:
                        price = float(a[3].get_text().replace(',', '.'))
                    except:
                        'No Price'
                    try:
                        prev_object = Services.objects.get(name='Water', old=False)
                    except:
                        'No previous object'
                    if price is not None:
                        if prev_object is None:
                            Services.objects.create(name='Water',
                                                    price_before_100=price,
                                                    price_after_100=price)
                        elif prev_object.price_before_100 != price:
                            prev_object.old = True
                            prev_object.save()
                            Services.objects.create(name='Water',
                                                    price_before_100=price,
                                                    price_after_100=price)
                elif item.name == u'Электричество':
                    a = BeautifulSoup(r.content, 'html.parser').find_all('table')[1].find_all('td')
                    price_before_100 = None
                    price_after_100 = None
                    try:
                        price_before_100 = float(a[4].get_text().replace(',', '.'))
                        price_after_100 = float(a[6].get_text().replace(',', '.'))
                    except:
                        'No Price'
                    try:
                        prev_object = Services.objects.get(name='Electricity', old=False)
                    except:
                        'No previous object'
                    if price_before_100 is not None and price_after_100 is not None:
                        if prev_object is None:
                            Services.objects.create(name='Electricity',
                                                    price_before_100=price_before_100,
                                                    price_after_100=price_after_100)
                        elif prev_object.price_before_100 != price_before_100 or prev_object.price_after_100 != price_after_100:
                            prev_object.old = True
                            prev_object.save()
                            Services.objects.create(name='Electricity',
                                                    price_before_100=price_before_100,
                                                    price_after_100=price_after_100)
