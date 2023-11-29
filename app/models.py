from django.db import models

from django.db import models

class Laptop(models.Model):
    nama_laptop = models.CharField(max_length=100)
    ram = models.IntegerField()
    memori_internal = models.IntegerField()
    layar = models.FloatField()
    harga = models.IntegerField()
    baterai = models.IntegerField(default=0.0)
    nilai_saw = models.FloatField(null=True, blank=True)

    # Bidang tambahan
    norm_ram = models.FloatField(null=True, blank=True)
    norm_memori_internal = models.FloatField(null=True, blank=True)
    norm_harga = models.FloatField(null=True, blank=True)
    norm_layar = models.FloatField(null=True, blank=True)
    norm_baterai = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nama_laptop

