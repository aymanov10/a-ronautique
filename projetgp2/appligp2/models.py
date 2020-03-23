from django.db import models

# Create your models here.

class Airports(models.Model):
    airport_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    IATA_airport = models.CharField(max_length=8)
    ICAO_airport = models.CharField(max_length=8)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    altitude = models.CharField(max_length=15)

class Airlines(models.Model): 
    airline_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    alias = models.CharField(max_length=40)
    IATA_airline = models.CharField(max_length=8)
    ICAO_airline = models.CharField(max_length=8)
    
class Country(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    iso_code= models.CharField(max_length=2)
    dafif_code = models.CharField(max_length=2)
    