# Generated by Django 4.2.1 on 2023-06-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('word_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('english_word', models.CharField(max_length=255, verbose_name='Англійське слово')),
                ('translation', models.CharField(max_length=255, verbose_name='Переклад')),
            ],
        ),
    ]
