from django.db import models


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=200)
    subtitle = models.CharField('Подзаголовок (краткое описание)', max_length=300)
    price = models.CharField('Цена', max_length=100, help_text='Например: "100 руб." или "320 руб."')
    duration = models.CharField('Продолжительность', max_length=100, help_text='Например: "60-75 минут" или "1 месяц"')
    order = models.PositiveIntegerField('Порядок отображения', default=0)
    is_active = models.BooleanField('Активно', default=True)
    #  Дополнительные поля (необязательные)
    renewal_price = models.CharField('Цена продления', max_length=100, blank=True,
                                     help_text='Например: "160 руб." (оставьте пустым, если не нужно)')
    icon_class = models.CharField('Класс иконки (Font Awesome)', max_length=50, default='fa-check',
                                  help_text='Например: fa-check, fa-wand-magic-sparkles, fa-magnifying-glass')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='items')
    text = models.CharField('Пункт услуги', max_length=300)
    order = models.PositiveIntegerField('Порядок отображения', default=0)

    class Meta:
        verbose_name = 'Пункт услуги'
        verbose_name_plural = 'Пункты услуг'
        ordering = ['order']

    def __str__(self):
        return f"{self.service.title} - {self.text[:50]}"
