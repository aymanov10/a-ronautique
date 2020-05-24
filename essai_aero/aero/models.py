from django.db import models

# Create your models here.


class Clients(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    tel = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return '%s %s %s %s %s' % (self.last_name, self.first_name, self.nationality, self.tel , self.email)


class Airports(models.Model):
    airport_id = models.IntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    IATA_airport = models.CharField(max_length=1000)
    ICAO_airport = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.name, self.city, self.country, self.IATA_airport, self.ICAO_airport,
                                            self.latitude, self.longitude, self.altitude)


class Airlines(models.Model):
    airline_id = models.FloatField(primary_key=True, max_length=1000)
    name = models.CharField(max_length=1000)
    alias = models.CharField(max_length=1000)
    IATA_airline = models.CharField(max_length=1000)
    ICAO_airline = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.alias, self.IATA_airline, self.ICAO_airline)


class Country(models.Model):
    name = models.CharField(primary_key=True, max_length=1000)
    iso_code = models.CharField(max_length=1000)
    dafif_code = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s %s' % (self.name, self.iso_code, self.dafif_code)


class Routes(models.Model):
    class Meta:
        unique_together = (('airline_id','source_airport_id','destination_airport_id'),)
    airline_id = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    source_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='+')
    destination_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='+')
    source_airport = models.CharField(max_length=1000)
    destination_airport = models.CharField(max_length=1000)
    stops = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s' % (self.source_airport, self.destination_airport)


class Vols(models.Model):
    airline = models.CharField(max_length=1000)
    departure_city = models.CharField(max_length=1000)
    departure_airport = models.CharField(max_length=1000)
    arrival_city = models.CharField(max_length=1000)
    arrival_airport = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s %s %s %s' % (self.airline,self.departure_city, self.departure_airport,
                                   self.arrival_city,self.arrival_airport)


class Voyages(models.Model):
    compagnie = models.CharField(max_length=1000)
    ville_depart = models.CharField(max_length=1000)
    aeroport_depart = models.CharField(max_length=1000)
    ville_arrive = models.CharField(max_length=1000)
    aeroport_arrive = models.CharField(max_length=1000)
    date = models.DateField(max_length=1000)
    price = models.IntegerField(default=0)
    places = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s %s %s' % (self.compagnie , self.ville_depart , self.aeroport_depart, self.ville_arrive,
                                   self.aeroport_arrive)


class Reservation(models.Model):
    reference_voyage = models.IntegerField(default=0)
    mail_client = models.EmailField(default="")


class Reclamation(models.Model):
    ref_voyage = models.IntegerField(default=0)
    email_client = models.EmailField(max_length=40)
    categorie = models.CharField(max_length=40)
    message = models.TextField()


class Statistics(models.Model):
    nom_pays = models.CharField(max_length=40)
    img = models.CharField(max_length=40)
    number = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)

