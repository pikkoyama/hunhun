# Generated by Django 5.1.3 on 2025-01-16 03:03

import guide.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0007_alter_case_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='number',
            field=models.CharField(default=guide.models.random_num, max_length=8, primary_key=True, serialize=False, verbose_name='社員番号'),
        ),
    ]
