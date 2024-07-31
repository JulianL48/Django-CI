from django.db import models

class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    caracteristica = models.TextField()

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=13)
    sector_fk = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=True, related_name='proveedores')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marcas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True, related_name='productos')

    def __str__(self):
        return self.nombre
