from django.db import models
from django.contrib.auth.models import User

class Foydalanuvchi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Mahsulot(models.Model):
    nomi = models.CharField(max_length=50)
    soni = models.PositiveIntegerField()
    tannarxi = models.PositiveIntegerField()
    qoyilgan_narx = models.PositiveIntegerField()
    olib_kelingan_sana = models.DateField()
    sotib_tugatish_sanas = models.DateField()
    yaroqlik_muddati = models.DateField()
    xarajat = models.PositiveIntegerField()
    foyda = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Qarzdorlik_sotuvchi(models.Model):
    mahsulot_nomi = models.CharField(max_length=50)
    narxi = models.PositiveIntegerField()
    soni = models.PositiveIntegerField()
    olingan_sana = models.DateField()
    qaytarilgan_sana = models.DateField()
    qarz_berganning_ismi = models.CharField(max_length=25)
    telefon_raqam = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Qarzdorlik_mijoz(models.Model):
    mahsulot_nomi = models.CharField(max_length=50)
    narxi = models.PositiveIntegerField()
    soni = models.PositiveIntegerField()
    olingan_sana = models.DateField()
    qaytarilgan_sana = models.DateField()
    qarz_berganning_ismi = models.CharField(max_length=25)
    telefon_raqam = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Kirim(models.Model):
    mahsulot_nomi = models.CharField(max_length=50)
    soni = models.PositiveIntegerField()
    Tannarxi = models.PositiveIntegerField()
    qoyilgan_narx = models.PositiveIntegerField()
    olib_kelingan_sana = models.DateField()
    sotib_tugaish_taminiy_sanasi= models.DateField(blank=True, null=True)
    yaroqlilik_muddati = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


# Create your models here.
