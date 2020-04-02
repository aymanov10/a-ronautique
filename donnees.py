""""
Ce fichier est un fichier contenant le code que j'ai écris pour peupler la base de données.Je ne l'ai pas lancé directement.
jai fait un "python manage.py shell" et j'ai copié et collé ces portions de code
j'ai mis sous un format csv les données recueillies .

Si vous utilisez PyCharm (ce qui serait l'idéal) créer une base de données postgresql et tester la connection à la base de données,puis après avoir fait:*
-python manage.py makemigrations nom_de_lapplication
-python manage.py sqlmigrate nom_de_lapplication 0001
-pyhton manage.py migrate nom_de_lapplication
pour la création des tables
-python manage.py shell et ensuite lancer dans l'ordre les commandes ci-dessous
"""
from aero.models import Aircraft,Airports,Airlines,Event,Location,Injuries,Country,Routes
"""
afin d'utiliser pandas notamment dans le terminal de PyCharm il serait utile de lancer les deux commandes suivantes
pip install wheel
pip install pandas
"""

import pandas as pd

# la table aircraft
data=pd.read_csv("elements/aviation.csv")
for i in range(len(data)):
    k=Aircraft(registration_number=data['RegistrationNumber'][i],amateur_built=data['AmateurBuilt'][i],make=data['Make'][i],
               model=data['Model'][i],damage=data['AircraftDamage'][i],nb_of_engines=data['NumberOfEngines'][i],engines_type=data['EngineType'][i])
    k.save()
    print("ok")


#table location

for i in range(len(data)):
    k = Location(acc_num=data['AccidentNumber'][i],location=data['Location'][i],country=data['Country'][i],
                 latitude=data['Latitude'][i], longitude=data['Longitude'][i], airport_code=data['AirportCode'][i],
                 airport_name=data['AirportName'][i])
    k.save()
    print("ok")

#table Event
import datetime
for i in range(len(data)):
    q1=Location.objects.get(pk=data['AccidentNumber'][i])
    q2=Aircraft.objects.get(pk=data['RegistrationNumber'][i])
    k = Event(event_id=data['EventId'][i], date_event=datetime.datetime.strptime(data['EventDate'][i],'%m/%d/%Y').date(),
              investigation_type=data['InvestigationType'][i],accident_number=q1,
              injury_severity=data['InjurySeverity'][i], aircraft_category=data['AircraftCategory'][i],
              registration_number=q2)
    k.save()
    print("ok")


#table Injuries

for i in range(len(data)):
    k = Injuries(acc_num=data['AccidentNumber'][i], total_fatal_injuries=data['TotalFatalInjuries'][i],
                 total_serious_injuries=data['TotalSeriousInjuries'][i], total_minor_injuries=data['TotalMinorInjuries'][i],
                 total_uninjured=data['TotalUninjured'][i])
    k.save()
    print("ok")





#table Country
with open("elements/countries.csv","r",encoding="utf-8") as f:
    for line in f.readlines():
        found=line.split(sep=",")
        k=Country(name=found[0],iso_code=found[1],dafif_code=found[2])
        k.save()
        print("yes")


#table Airports
airport_data=pd.read_csv("elements/airports.csv")
for i in range(len(airport_data)):
    k = Airports(airport_id=airport_data['Id'][i], name=airport_data['Name'][i], city=airport_data['City'][i],
                 country=airport_data['Country'][i],
                 IATA_airport=airport_data['IATA'][i], ICAO_airport=airport_data['ICAO'][i],
                 latitude=airport_data['Latitude'][i], longitude=airport_data['Longitude'][i],
                 altitude=airport_data['Altitude'][i])
    k.save()
    print("yes")


#table Airlines
airline_data=pd.read_csv("elements/airlines.csv")
for i in range(len(airline_data)):
    k = Airlines(airline_id=airline_data['AirlineId'][i], name=airline_data['Name'][i], alias=airline_data['Alias'][i],
                 IATA_airline=airline_data['IATA'][i], ICAO_airline=airline_data['ICAO'][i])
    k.save()
    print("yes")

#table Routes
route_data=pd.read_csv("elements/routes.csv")
for i in range(len(route_data)):
    try:
        q1 = Airlines.objects.get(pk=route_data['AirlineId'][i])
        q2 = Airports.objects.get(pk=route_data['SourceId'][i])
        q3 = Airports.objects.get(pk=route_data['DestinationId'][i])
        k = Routes(airline_id=q1, source_airport_id=q2, destination_airport_id=q3,source_airport=route_data['Source'][i],
                   destination_airport=route_data['Destination'][i], stops=route_data['Stops'][i])
        k.save()
        print("yes")
    except:
        print("unavalaible")

