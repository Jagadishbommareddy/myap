# Generated by Django 2.2.6 on 2019-11-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_systemconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('original_name', models.CharField(max_length=255)),
            ],
        ),
    ]
