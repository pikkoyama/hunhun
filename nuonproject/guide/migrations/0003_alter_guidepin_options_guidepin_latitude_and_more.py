# Generated by Django 5.1.3 on 2025-01-10 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_remove_customuser_name_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guidepin',
            options={'verbose_name_plural': 'ガイドピン'},
        ),
        migrations.AddField(
            model_name='guidepin',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9, verbose_name='緯度'),
        ),
        migrations.AddField(
            model_name='guidepin',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9, verbose_name='経度'),
        ),
    ]
