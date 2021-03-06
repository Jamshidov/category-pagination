# Generated by Django 3.2.6 on 2021-09-16 18:01

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('text', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m')),
                ('price', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='capp.category')),
            ],
            options={
                'verbose_name': 'Maxsulot',
                'verbose_name_plural': 'Maxsulotlar',
            },
        ),
    ]
