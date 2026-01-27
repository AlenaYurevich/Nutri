from django.contrib import sitemaps
from django.urls import reverse
from django.utils import timezone


class HelenStaticSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'


    def items(self):
        return [
            {'name': 'home', 'priority': 1.0},
            {'name': 'about', 'priority': 0.9},
            {'name': 'services', 'priority': 0.9},
            {'name': 'calculator', 'priority': 0.8},
        ]

    def location(self, item):
        return reverse(item['name'])

    def priority(self, item):
        return item['priority']

    def lastmod(self, item):
        return timezone.now()


sitemaps = {
    'static': HelenStaticSitemap,
    }
