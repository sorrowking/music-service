# Generated by Django 5.1.3 on 2024-11-08 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_song_duration_song_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_date', models.IntegerField(default=1900)),
            ],
            options={
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'artists',
            },
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='main.album'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='main.artist'),
        ),
    ]