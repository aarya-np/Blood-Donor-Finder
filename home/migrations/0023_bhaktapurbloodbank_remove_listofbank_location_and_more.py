# Generated by Django 4.0.2 on 2022-02-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_listofbank_htmlfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BhaktapurBloodBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=10)),
                ('locationame', models.CharField(default='none', max_length=100)),
                ('location', models.URLField(max_length=300)),
                ('Aplus', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='listofbank',
            name='location',
        ),
        migrations.RemoveField(
            model_name='listofbank',
            name='locationame',
        ),
        migrations.RemoveField(
            model_name='listofbank',
            name='name',
        ),
        migrations.RemoveField(
            model_name='listofbank',
            name='phone',
        ),
    ]
