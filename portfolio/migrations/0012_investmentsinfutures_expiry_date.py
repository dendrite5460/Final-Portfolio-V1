# Generated by Django 3.0.3 on 2020-05-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_investmentsinfutures'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentsinfutures',
            name='expiry_date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
