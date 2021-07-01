from django.test import TestCase

# Create your tests here.
from core.models import Encuest
from CanastaBasica.wsgi import *


#Listar

querry = Encuest.objects-all()
print(querry)