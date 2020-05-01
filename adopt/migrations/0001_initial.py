# Generated by Django 3.0.5 on 2020-05-01 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('color', models.CharField(choices=[('red', 'Red'), ('yellow', 'Yellow'), ('black', 'Black')], max_length=50, verbose_name='Color')),
            ],
        ),
    ]
