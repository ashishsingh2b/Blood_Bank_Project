# Generated by Django 4.2.13 on 2024-06-07 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_blood_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('blood_donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood.blood_donation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood.userprofile')),
            ],
        ),
    ]