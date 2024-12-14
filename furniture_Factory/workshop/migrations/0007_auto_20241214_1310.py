# Generated by Django 3.2.16 on 2024-12-14 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0006_alter_worker_workshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='workshop.workshop', verbose_name='Цех'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='supervisor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workshop_supervised', to='workshop.worker', verbose_name='Начальник цеха'),
        ),
    ]
