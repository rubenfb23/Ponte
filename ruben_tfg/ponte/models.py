from django.db import models

TIPO_CHOICES = [
    ('Educativa', 'Educativa'),
    ('Personal', 'Personal'),
    ('Empresarial', 'Empresarial'),
]


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.BooleanField(blank=True)
    puerto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    estado = models.BooleanField(blank=True)
    sistema_operativo = models.CharField(max_length=20)
    servicios = models.ManyToManyField(Servicio, blank=True)
    ip_privada = models.CharField(max_length=20)
    mac = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Red(models.Model):
    id_red = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    estado = models.BooleanField(blank=True)
    ip = models.CharField(max_length=20)
    mascara = models.CharField(max_length=20)
    puerta_enlace = models.CharField(max_length=20)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    dispositivos = models.ManyToManyField(Dispositivo)

    def __str__(self):
        return self.nombre


class Ancla(models.Model):
    id_ancla = models.AutoField(primary_key=True)
    ip_publica = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.BooleanField(blank=True)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.BooleanField(blank=True)
    redes = models.ManyToManyField(Red)

    def __str__(self):
        return self.nombre
