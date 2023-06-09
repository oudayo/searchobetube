# Generated by Django 4.1.6 on 2023-04-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.URLField()),
                ('snippet', models.TextField()),
                ('image', models.TextField(null=True)),
                ('level', models.TextField()),
                ('totalResults', models.FloatField()),
                ('count', models.FloatField()),
                ('startIndex', models.FloatField()),
            ],
        ),
    ]
