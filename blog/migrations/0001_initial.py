# Generated by Django 3.0.7 on 2020-06-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('post_date', models.DateTimeField()),
                ('post_image', models.ImageField(upload_to='blog_images/')),
                ('post_text', models.CharField(max_length=300)),
            ],
        ),
    ]
