# Generated by Django 4.1.7 on 2023-02-25 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_alter_category_options_alter_part_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['code'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]