# Generated by Django 3.2.6 on 2022-01-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0012_auto_20190502_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
