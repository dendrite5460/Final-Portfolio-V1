# Generated by Django 3.0.3 on 2020-04-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_investments'),
    ]

    operations = [
        migrations.CreateModel(
            name='money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mymoney', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]