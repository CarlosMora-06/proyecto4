from django.db import models

# Create your models here.
class Autor (models.Model):
    nombre = models.CharField(max_length=100,null=False)
    nacionalidad = models.CharField(max_length=100, null=False)
    anio_nacimiento = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Autores"
        ordering = ["nombre"]

class Libro(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    isbn = models.CharField(max_length=100,null=False,unique=True)
    anio_publicacion = models.IntegerField(null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Libros"
        ordering = ["nombre"]


