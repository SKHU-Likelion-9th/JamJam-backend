# Generated by Django 3.2.6 on 2021-08-06 18:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jamjamapp', '0003_auto_20210806_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Big_Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_site_name', models.CharField(max_length=30)),
                ('book_url', models.URLField()),
                ('book_contents', models.TextField(blank=True)),
                ('book_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-book_created'],
            },
        ),
        migrations.CreateModel(
            name='Small_Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='Blog_likes',
            field=models.ManyToManyField(related_name='Blog_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Play_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Writer', models.CharField(max_length=100)),
                ('Write_day', models.DateTimeField(verbose_name='date published')),
                ('Content', models.TextField()),
                ('Image', models.ImageField(blank=True, upload_to='images/')),
                ('view_count', models.IntegerField(default=0)),
                ('big_region', models.ManyToManyField(blank=True, to='jamjamapp.Big_Region')),
                ('play_likes', models.ManyToManyField(related_name='Play_likes', to=settings.AUTH_USER_MODEL)),
                ('small_region', models.ManyToManyField(blank=True, to='jamjamapp.Small_Region')),
            ],
        ),
        migrations.CreateModel(
            name='Look_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Writer', models.CharField(max_length=100)),
                ('Write_day', models.DateTimeField(verbose_name='date published')),
                ('Content', models.TextField()),
                ('Image', models.ImageField(blank=True, upload_to='images/')),
                ('view_count', models.IntegerField(default=0)),
                ('Look_likes', models.ManyToManyField(related_name='Look_likes', to=settings.AUTH_USER_MODEL)),
                ('big_region', models.ManyToManyField(blank=True, to='jamjamapp.Big_Region')),
                ('small_region', models.ManyToManyField(blank=True, to='jamjamapp.Small_Region')),
            ],
        ),
        migrations.CreateModel(
            name='Eat_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Writer', models.CharField(max_length=100)),
                ('Write_day', models.DateTimeField(verbose_name='date published')),
                ('Content', models.TextField()),
                ('Image', models.ImageField(blank=True, upload_to='images/')),
                ('view_count', models.IntegerField(default=0)),
                ('Eat_likes', models.ManyToManyField(related_name='Eat_likes', to=settings.AUTH_USER_MODEL)),
                ('big_region', models.ManyToManyField(blank=True, to='jamjamapp.Big_Region')),
                ('small_region', models.ManyToManyField(blank=True, to='jamjamapp.Small_Region')),
            ],
        ),
    ]
