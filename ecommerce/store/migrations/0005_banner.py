# Generated by Django 5.0.3 on 2024-05-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('link_output', models.CharField(blank=True, max_length=400, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
