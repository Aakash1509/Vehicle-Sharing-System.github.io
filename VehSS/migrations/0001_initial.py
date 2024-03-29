# Generated by Django 4.1.5 on 2023-03-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('location', models.CharField(blank=True, choices=[('Vadodara', 'Vadodara'), ('Anand', 'Anand'), ('Nadiad', 'Nadiad')], max_length=50, null=True)),
                ('carname', models.CharField(max_length=120, null=True)),
                ('seats', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=120, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('image', models.ImageField(upload_to='Hello/static/image')),
            ],
        ),
    ]
