# Generated by Django 4.0.2 on 2022-02-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_listofbank_htmlfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofbank',
            name='htmlfile',
            field=models.URLField(default='none', max_length=100),
        ),
    ]
