from django.db import models

class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Brownie(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='brownies/', null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self): 
        return self.nombre