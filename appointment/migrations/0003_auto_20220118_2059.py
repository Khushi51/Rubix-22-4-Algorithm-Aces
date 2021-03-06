# Generated by Django 3.2.6 on 2022-01-18 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20190502_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='phone',
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='appointment.patient'),
            preserve_default=False,
        ),
    ]
