# Generated by Django 4.1.7 on 2023-02-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image_file_namne',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=12),
        ),
    ]
