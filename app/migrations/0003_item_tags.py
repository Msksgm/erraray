# Generated by Django 2.1.2 on 2019-08-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190807_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.TextField(blank=True, null=True, verbose_name='タグorライブラリ'),
        ),
    ]
