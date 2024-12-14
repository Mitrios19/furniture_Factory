# Generated by Django 3.2.16 on 2024-12-13 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_alter_workshop_numberworkers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=256, verbose_name='ФИО рабочего')),
                ('dateBirth', models.DateField(verbose_name='Дата рождения')),
                ('status', models.CharField(choices=[('working', 'Работает'), ('on_leave', 'В отпуске'), ('fired', 'Уволен')], default='working', max_length=20, verbose_name='Статус')),
                ('workingHours', models.CharField(max_length=11, verbose_name='Рабочие часы')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='workshop.workshop', verbose_name='Цех')),
            ],
            options={
                'verbose_name': 'работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]