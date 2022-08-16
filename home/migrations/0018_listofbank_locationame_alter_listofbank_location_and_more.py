# Generated by Django 4.0.2 on 2022-02-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_listofbanks_listofbank'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofbank',
            name='locationame',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='listofbank',
            name='location',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='listofbank',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
