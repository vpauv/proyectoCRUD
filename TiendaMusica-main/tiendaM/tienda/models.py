from django.db import models

# Create your models here.
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
class Autor(models.Model):
    idAutor = models.AutoField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=50) 
    rfc = models.CharField(max_length=13, null=True, default="" )

    def __str__(self):
        texto = "{1} ({0})"
        return texto.format(self.nombre, self.idAutor)

class Genero(models.Model):
    idGen= models.AutoField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=50) 

    def __str__(self):
        texto = "{1} ({0})"
        return texto.format(self.nombre, self.idGen)

class Cancion(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    titulo = models.CharField(max_length=50, verbose_name="Titulo")
    portada = models.ImageField(upload_to= 'imagenes/', verbose_name="Portada")
    album = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    preview = models.FileField(upload_to= 'audios/', verbose_name="Preview", default="")

    def __str__(self):
        fila = "Titulo: "+ self.titulo + "-" + "Autor: " + self.autor.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)
        super().delete()

