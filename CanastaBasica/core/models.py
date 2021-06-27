from django.db import models
#from django.forms import model_to_dict
# from config.settings import MEDIA_URL, STATIC_URL
# from core.erp.choices import gender_choices
#from core.models import BaseModel

# Create your models here.

class Departaments(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    #  def toJSON(self):
    #     item = model_to_dict(self)
    #     return item

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    # def toJSON(self):
    #     item = model_to_dict(self)
    #     item['full_name'] = '{} / {}'.format(self.name, self.cat.name)
    #     return item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Encuest(models.Model):
    dep = models.ForeignKey(Departaments, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.dep.name
    
    class Meta:
        verbose_name = 'Detalle de encuesta'
        verbose_name_plural = 'Detalle de encuestas'
        ordering = ['id']
