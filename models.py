from django.db import models

# Create your models here.


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


class Aircraft(models.Model):
    registration_number = models.CharField(primary_key=True, max_length=1000)
    amateur_built = models.CharField(max_length=1000)
    make = models.CharField(max_length=1000)
    model = models.CharField(max_length=1000)
    damage = models.CharField(max_length=1000)
    nb_of_engines = models.FloatField()
    engines_type = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.registration_number, self.amateur_built, self.make, self.model, self.damage,
                                      self.engines_type)


class Location(models.Model):
    acc_num = models.CharField(primary_key=True, max_length=1000)
    location = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    airport_code = models.CharField(max_length=1000)
    airport_name = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s %s %s %s' % (self.acc_num, self.location, self.country, self.airport_code, self.airport_name)


class Event(models.Model):
    event_id = models.CharField(primary_key=True, max_length=1000)
    date_event = models.DateField(max_length=1000)
    investigation_type = models.CharField(max_length=1000)
    accident_number = models.ForeignKey(Location, on_delete=models.CASCADE)
    injury_severity = models.CharField(max_length=1000)
    aircraft_category = models.CharField(max_length=1000,default=0)
    registration_number = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.event_id, self.investigation_type, self.injury_severity)


class Injuries(models.Model):
    acc_num = models.CharField(primary_key=True, max_length=1000)
    total_fatal_injuries = models.FloatField()
    total_serious_injuries = models.FloatField()
    total_minor_injuries = models.FloatField()
    total_uninjured = models.FloatField()

    def __str__(self):
        return self.acc_num



