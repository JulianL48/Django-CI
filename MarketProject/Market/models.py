from django.db import models

class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    caracteristica = models.TextField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=13)
    sector_fk = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=True, related_name='proveedores')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)  # Añadido valor por defecto
    creado = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True, related_name='productos')

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Factura(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, related_name='clientes')
    fecha_emision = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(auto_now_add=False)
    total = models.DecimalField(max_digits=13, decimal_places=2)

class Detalle_Factura(models.Model):
    factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE, null=True, blank=True, related_name='facturas')
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True, related_name='productos')
    precio_unitario = models.DecimalField(max_digits=13, decimal_places=2)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=13, decimal_places=2)