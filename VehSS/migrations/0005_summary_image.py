# Generated by Django 4.1.5 on 2023-04-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VehSS', '0004_alter_summary_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='image',
            field=models.ImageField(default=' ', upload_to='Hello/static/image'),
            preserve_default=False,
        ),
    ]
