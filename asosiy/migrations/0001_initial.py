# Generated by Django 4.2.1 on 2024-01-17 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Qarzdorlik_sotuvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot_nomi', models.CharField(max_length=50)),
                ('narxi', models.PositiveIntegerField()),
                ('soni', models.PositiveIntegerField()),
                ('olingan_sana', models.DateField()),
                ('qaytarilgan_sana', models.DateField()),
                ('qarz_berganning_ismi', models.CharField(max_length=25)),
                ('telefon_raqam', models.CharField(max_length=12)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qarzdorlik_mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot_nomi', models.CharField(max_length=50)),
                ('narxi', models.PositiveIntegerField()),
                ('soni', models.PositiveIntegerField()),
                ('olingan_sana', models.DateField()),
                ('qaytarilgan_sana', models.DateField()),
                ('qarz_berganning_ismi', models.CharField(max_length=25)),
                ('telefon_raqam', models.CharField(max_length=12)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('soni', models.PositiveIntegerField()),
                ('tannarxi', models.PositiveIntegerField()),
                ('qoyilgan_narx', models.PositiveIntegerField()),
                ('olib_kelingan_sana', models.DateField()),
                ('sotib_tugatish_sanas', models.DateField()),
                ('yaroqlik_muddati', models.DateField()),
                ('xarajat', models.PositiveIntegerField()),
                ('foyda', models.PositiveIntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kirim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot_nomi', models.CharField(max_length=50)),
                ('soni', models.PositiveIntegerField()),
                ('Tannarxi', models.PositiveIntegerField()),
                ('qoyilgan_narx', models.PositiveIntegerField()),
                ('olib_kelingan_sana', models.DateField()),
                ('sotib_tugaish_taminiy_sanasi', models.DateField(blank=True, null=True)),
                ('yaroqlilik_muddati', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foydalanuvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]