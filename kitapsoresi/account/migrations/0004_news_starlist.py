# Generated by Django 3.2.17 on 2023-02-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20230211_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='newsPhotos/%Y/%m/%d')),
                ('text', models.TextField(blank=True)),
                ('bookId', models.IntegerField(blank=True)),
                ('saveStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('postId', models.IntegerField(blank=True)),
                ('bookId', models.IntegerField(blank=True)),
            ],
        ),
    ]