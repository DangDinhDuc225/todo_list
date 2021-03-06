# Generated by Django 3.1 on 2020-08-07 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_create_by', to='web.user')),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_update_by', to='web.user')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_by', to='web.user'),
        ),
        migrations.AddField(
            model_name='category',
            name='update_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update_by', to='web.user'),
        ),
    ]
