# Generated by Django 4.0.2 on 2022-02-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_donor_eligible_alter_donor_terms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usernamepasswords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
