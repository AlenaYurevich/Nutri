from django.db import models
from django.core.validators import MinLengthValidator


class Service(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок услуги"
    )
    subtitle = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Подзаголовок"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="Цена"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активна"
    )

    # Блок "Кому"
    target_audience = models.TextField(
        verbose_name="Кому (целевая аудитория)",
        help_text="Каждый пункт с новой строки",
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True
    )

    # Блок "Для чего"
    purpose_title = models.CharField(
        max_length=200,
        default="Для чего:",
        verbose_name="Заголовок блока 'Для чего'"
    )
    purposes = models.TextField(
        verbose_name="Для чего (цели)",
        help_text="Каждый пункт с новой строки",
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True
    )

    # Блок "Что входит"
    includes_title = models.CharField(
        max_length=200,
        default="Что входит:",
        verbose_name="Заголовок блока 'Что входит'"
    )
    included_items = models.TextField(
        verbose_name="Что входит (список услуг)",
        help_text="Каждый пункт с новой строки",
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_target_audience_list(self):
        if self.target_audience:
            return [item.strip() for item in self.target_audience.splitlines() if item.strip()]
        return []

    def get_purposes_list(self):
        if self.purposes:
            return [item.strip() for item in self.purposes.splitlines() if item.strip()]
        return []

    def get_included_items_list(self):
        if self.included_items:
            return [item.strip() for item in self.included_items.splitlines() if item.strip()]
        return []
