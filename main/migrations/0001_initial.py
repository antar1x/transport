# Generated manually for the first version of the main app.

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ім’я')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('service', models.CharField(choices=[('demontazh', 'Демонтаж'), ('pereizd', 'Квартирний або офісний переїзд'), ('perevezennia', 'Вантажні перевезення'), ('vantazhnyky', 'Послуги вантажників'), ('smittya', 'Вивіз будівельного сміття'), ('other', 'Інше')], max_length=30, verbose_name='Послуга')),
                ('comment', models.TextField(blank=True, verbose_name='Коментар')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_at'],
            },
        ),
    ]
