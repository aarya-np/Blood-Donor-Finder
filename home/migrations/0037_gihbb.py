# Generated by Django 4.0.2 on 2022-03-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_bhbb_bankid'),
    ]

    operations = [
        migrations.CreateModel(
            name='gihbb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankid', models.CharField(default='6', max_length=100)),
                ('Aplus', models.CharField(default='none', max_length=30)),
                ('Aminus', models.CharField(default='none', max_length=30)),
                ('Bplus', models.CharField(default='none', max_length=30)),
                ('Bminus', models.CharField(default='none', max_length=30)),
                ('ABplus', models.CharField(default='none', max_length=30)),
                ('ABminus', models.CharField(default='none', max_length=30)),
                ('Oplus', models.CharField(default='none', max_length=30)),
                ('Ominus', models.CharField(default='none', max_length=30)),
            ],
        ),
    ]
