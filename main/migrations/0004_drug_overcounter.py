# Generated by Django 3.2.4 on 2021-06-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_recommndations_illness_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='overCounter',
            field=models.BooleanField(default=False),
        ),
    ]