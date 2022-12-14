# Generated by Django 4.1.1 on 2022-10-03 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('author', models.TextField()),
                ('first_publishing_year', models.CharField(max_length=200)),
                ('number_of_pages', models.CharField(max_length=200)),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.books')),
            ],
        ),
    ]
