# Generated by Django 2.1.2 on 2019-08-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190808_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='solve',
            field=models.IntegerField(blank=True, choices=[(1, '解決'), (2, '非解決')], null=True, verbose_name='選択肢'),
        ),
    ]
