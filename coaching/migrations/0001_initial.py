# Generated by Django 4.1.1 on 2022-09-14 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('katysite', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('comments_mode', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coaching.category')),
            ],
        ),
        migrations.CreateModel(
            name='PostData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/coach/post_False/')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='coaching.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=90)),
                ('comment', models.TextField()),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('author_ip', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coaching.post')),
            ],
        ),
        migrations.CreateModel(
            name='CoachMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('slug', models.SlugField(unique=True)),
                ('main_page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='katysite.mainmenu')),
            ],
        ),
    ]
