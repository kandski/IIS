from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Zlodej(AbstractUser):
    prezivka = models.CharField(max_length=30, primary_key=True, unique=True)
    meno = models.CharField(max_length=30)
    rc = models.CharField(max_length=11)
    zivy = models.BooleanField(default=True)
    odmena = models.IntegerField()
    fotka = models.CharField(max_length=300)


    def get_absolute_url(self):
        return reverse('zlodej:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.prezivka

class Skolenie(models.Model):
    level_skoleni = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    schvalene = models.BooleanField(default=False)
    poznamky = models.CharField(max_length=300)
    zlodej = models.ManyToManyField(Zlodej, through='BolNa')


class Rajon(models.Model):
    nazov_rajonu = models.CharField(max_length=40, primary_key=True)
    dlzka = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    sirka = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    pocet_obyvatelov = models.IntegerField()
    kapacita_zlodejov = models.IntegerField()
    bohatstvo = models.IntegerField()
    level_rajonu = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    zlodej = models.ManyToManyField(Zlodej, through='Eviduje')

    def __str__(self):
        return self.nazov_rajonu


class Vydriduch(models.Model):
    zlodej = models.OneToOneField(Zlodej, on_delete=models.CASCADE, primary_key=True)
    # prezivka = models.CharField(max_length=30, primary_key=True)
    peniaze = models.IntegerField()
    provizia = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.zlodej


class Lupeznik(models.Model):
    zlodej = models.OneToOneField(Zlodej, on_delete=models.CASCADE, primary_key=True)
    #     prezivka = models.CharField(max_length=30, primary_key=True)
    pocet_zabitych = models.PositiveIntegerField()

    def __str__(self):
        return self.zlodej


class TypZlocinu(models.Model):
    druh = models.CharField(max_length=20)
    skolenie = models.ManyToManyField(Skolenie, through='SkolenieZlocinu')

    def __str__(self):
        return self.druh


class Zlocin(models.Model):
    hodnota_korist = models.IntegerField()
    uspech = models.BooleanField(default=True)  # ano = true
    id_typu_zlocinu = models.ForeignKey(TypZlocinu, on_delete=models.CASCADE)
    zlodej = models.ManyToManyField(Zlodej, through='Urobil')

    def get_absolute_url(self):
        return reverse('zlodej:index')

    def __str__(self):
        return self.id.__str__() + '(' + self.id_typu_zlocinu.__str__() + ')'


class Povolenie(models.Model):
    doba_platnosti = models.PositiveIntegerField()
    nazov_rajonu = models.ForeignKey(Rajon, on_delete=models.CASCADE)
    id_zlocinu = models.ForeignKey(Zlocin, on_delete=models.CASCADE)
    zlodej = models.ManyToManyField(Zlodej, through='Dostal')


class TypVybavenia(models.Model):
    nazov = models.CharField(max_length=20)
    skolenie = models.ManyToManyField(Skolenie, through='SkolenieVybavenia')

    def __str__(self):
        return self.nazov


class Vybavenie(models.Model):
    meno = models.CharField(max_length=30)
    id_typu_vybavenia = models.ForeignKey(TypVybavenia, on_delete=models.CASCADE)
    zlodej = models.ManyToManyField(Zlodej, through='Vlastnil')


class Vlastnil(models.Model):
    prezivka = models.ForeignKey(Zlodej, on_delete=models.CASCADE)
    id_vybavenia = models.ForeignKey(Vybavenie, on_delete=models.CASCADE)
    od = models.DateField()
    do = models.DateField()


class Urobil(models.Model):
    id_zlocinu = models.ForeignKey(Zlocin, on_delete=models.CASCADE)
    prezivka = models.ForeignKey(Zlodej, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('zlodej:index')


class BolNa(models.Model):
    id_skolenia = models.ForeignKey(Skolenie, on_delete=models.CASCADE)
    prezivka = models.ForeignKey(Zlodej, on_delete=models.CASCADE)


class Eviduje(models.Model):
    prezivka = models.ForeignKey(Zlodej, on_delete=models.CASCADE)
    nazov_rajonu = models.ForeignKey(Rajon, on_delete=models.CASCADE)

    def __str__(self):
        return self.prezivka.prezivka


class Dostal(models.Model):
    prezivka = models.ForeignKey(Zlodej, on_delete=models.CASCADE)
    id_povolenia = models.ForeignKey(Povolenie, on_delete=models.CASCADE)


class SkolenieVybavenia(models.Model):
    id_skolenia = models.ForeignKey(Skolenie, on_delete=models.CASCADE)
    id_typu_vybavenia = models.ForeignKey(TypVybavenia, on_delete=models.CASCADE)


class SkolenieZlocinu(models.Model):
    id_skolenia = models.ForeignKey(Skolenie, on_delete=models.CASCADE)
    id_typu_zlocinu = models.ForeignKey(TypZlocinu, on_delete=models.CASCADE)
