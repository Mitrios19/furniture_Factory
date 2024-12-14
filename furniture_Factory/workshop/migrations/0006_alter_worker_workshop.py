# Generated by Django 3.2.16 on 2024-12-14 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0005_alter_workshop_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='workshop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='workshop.workshop', verbose_name='Цех'),
        ),
    ]
