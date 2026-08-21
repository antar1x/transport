from django.db import models


class Request(models.Model):
    SERVICE_CHOICES = [
        ('demontazh', 'Демонтаж'),
        ('pereizd', 'Квартирний або офісний переїзд'),
        ('perevezennia', 'Вантажні перевезення'),
        ('vantazhnyky', 'Послуги вантажників'),
        ('smittya', 'Вивіз будівельного сміття'),
        ('other', 'Інше'),
    ]

    name = models.CharField('Ім’я', max_length=100)
    phone = models.CharField('Телефон', max_length=30)
    service = models.CharField('Послуга', max_length=30, choices=SERVICE_CHOICES)
    comment = models.TextField('Коментар', blank=True)
    created_at = models.DateTimeField('Створено', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.get_service_display()}'
