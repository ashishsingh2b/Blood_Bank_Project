# Generated by Django 4.2.13 on 2024-06-07 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=15, null=True)),
                ('dob', models.DateField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('blood_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
