# Generated by Django 2.2.5 on 2019-09-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='desc',
            field=models.CharField(default='', max_length=20),
        ),
    ]
