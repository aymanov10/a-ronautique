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
from aero.models import Airports,Airlines,Country,Routes,Vols,Voyages,Reservation,Clients
"""
afin d'utiliser pandas notamment dans le terminal de PyCharm il serait utile de lancer les deux commandes suivantes
pip install wheel
pip install pandas
"""

import pandas as pd



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


"""
Pour peupler la table Vols dans laquelle on aura juste la compagnie,la ville de départ et la ville d'arrivée,
 ce qui nous sera indispensable pour la table voyages
 """
liste=[]
# essai

for i in Routes.objects.all():
    q1=i.airline_id.name
    q2=i.source_airport_id.name
    q3=i.destination_airport_id.name
    liste.append(["compagnie",q1,"depart",q2,"arrivée",q3])


# remplissage de Vols

for i in Routes.objects.all():
    q1 = i.airline_id.name
    q2 = i.source_airport_id.city
    q3 = i.source_airport_id.name
    q4 = i.destination_airport_id.city
    q5 = i.destination_airport_id.name
    k = Vols(airline=q1, departure_city=q2, departure_airport=q3, arrival_city=q4, arrival_airport=q5)
    k.save()
    print("yes")


# pour récupérer la liste de tous les pays

liste=[]
for i in Country.objects.all():
    liste.append((i.name.lower(),i.name))


""" LISTE DES PAYS OBTENUS --- APPLIQUER LA FONCTION SORTED() POUR TRIER PAR ORDRE ALPHABETIQUE
[('bhutan', 'Bhutan'), ('haiti', 'Haiti'),  ('aruba', 'Aruba'), ('antigua and barbuda', 'Antigua and Barbuda'), ('united arab emirates', 'United Arab Emirates'), ('afghanistan', 'Afghanistan'), ('algeria', 'Algeria'), ('azerbaijan', 'Azerbaijan'), ('albania', 'Albania'), ('armenia', 'Armenia'), ('angola', 'Angola'), ('argentina', 'Argentina'), ('australia', 'Australia'),
 ('ashmore and cartier islands', 'Ashmore and Cartier Islands'), ('austria', 'Austria'), ('anguilla', 'Anguilla'), ('antarctica', 'Antarctica'), ('bahrain', 'Bahrain'), ('barbados', 'Barbados'), ('botswana', 'Botswana'),
 ('bermuda', 'Bermuda'), ('belgium', 'Belgium'), ('bahamas', 'Bahamas'), ('belize', 'Belize'), ('bosnia and herzegovina', 'Bosnia and Herzegovina'), ('bolivia', 'Bolivia'), ('myanmar', 'Myanmar'),
 ('benin', 'Benin'), ('belarus', 'Belarus'), ('solomon islands', 'Solomon Islands'), ('navassa island', 'Navassa Island'), ('brazil', 'Brazil'), ('clipperton island', 'Clipperton Island'), ('bulgaria', 'Bulgaria'),
 ('brunei darussalam', 'Brunei Darussalam'), ('burundi', 'Burundi'), ('canada', 'Canada'), ('cambodia', 'Cambodia'), ('chad', 'Chad'), ('sri lanka', 'Sri Lanka'), ('dr congo', 'DR Congo'),
 ('congo republic', 'Congo Republic'), ('china', 'China'), ('chile', 'Chile'), ('cayman islands', 'Cayman Islands'), ('cameroon', 'Cameroon'), ('comoros', 'Comoros'), ('colombia', 'Colombia'),
 ('northern mariana islands', 'Northern Mariana Islands'), ('coral sea islands', 'Coral Sea Islands'), ('costa rica', 'Costa Rica'), ('central african republic', 'Central African Republic'), ('cuba', 'Cuba'), ('cabo verde', 'Cabo Verde'),
 ('cook islands', 'Cook Islands'), ('cyprus', 'Cyprus'), ('denmark', 'Denmark'), ('djibouti', 'Djibouti'), ('dominica', 'Dominica'), ('dominican republic', 'Dominican Republic'), ('ecuador', 'Ecuador'), ('egypt', 'Egypt'),
 ('ireland', 'Ireland'),('equatorial guinea', 'Equatorial Guinea'), ('estonia', 'Estonia'), ('eritrea', 'Eritrea'), ('el salvador', 'El Salvador'), ('ethiopia', 'Ethiopia'), ('europa island', 'Europa Island'),
 ('czech republic', 'Czech Republic'), ('french guiana', 'French Guiana'), ('finland', 'Finland'), ('fiji', 'Fiji'), ('"micronesia', '"Micronesia'), ('faeroe islands', 'Faeroe Islands'),
 ('french polynesia', 'French Polynesia'), ('baker island', 'Baker Island'), ('france', 'France'), ('french southern territories', 'French Southern Territories'), ('gambia', 'Gambia'), ('gabon', 'Gabon'), ('georgia', 'Georgia'),
 ('ghana', 'Ghana'), ('grenada', 'Grenada'), ('guernsey', 'Guernsey'), ('greenland', 'Greenland'), ('germany', 'Germany'), ('glorioso islands', 'Glorioso Islands'), ('guadeloupe', 'Guadeloupe'), ('guam', 'Guam'),
 ('greece', 'Greece'), ('guatemala', 'Guatemala'), ('guinea', 'Guinea'), ('guyana', 'Guyana'), ('heard and mcdonald islands', 'Heard and McDonald Islands'), ('honduras', 'Honduras'), ('howland island', 'Howland Island'),
 ('croatia', 'Croatia'), ('hungary', 'Hungary'), ('iceland', 'Iceland'), ('indonesia', 'Indonesia'), ('isle of man', 'Isle of Man'), ('india', 'India'), ('iran', 'Iran'), ('israel', 'Israel'), ('italy', 'Italy'),
 ("cote d'ivoire", "Cote d'Ivoire"), ('iraq', 'Iraq'), ('japan', 'Japan'), ('jersey', 'Jersey'), ('jamaica', 'Jamaica'), ('jan mayen', 'Jan Mayen'), ('jordan', 'Jordan'), ('johnston atoll', 'Johnston Atoll'),
 ('juan de nova island', 'Juan de Nova Island'), ('kenya', 'Kenya'), ('kyrgyz republic', 'Kyrgyz Republic'), ('north korea', 'North Korea'), ('kingman reef', 'Kingman Reef'), ('kiribati', 'Kiribati'),
 ('south korea', 'South Korea'), ('christmas island', 'Christmas Island'), ('kuwait', 'Kuwait'), ('american samoa', 'American Samoa'), ('bangladesh', 'Bangladesh'), ('bouvet island', 'Bouvet Island'),
 ('cocos (keeling) islands', 'Cocos (Keeling) Islands'), ('jarvis island', 'Jarvis Island'), ('falkland islands', 'Falkland Islands'), ('gibraltar', 'Gibraltar'), ('hong kong', 'Hong Kong'),
 ('british indian ocean territory', 'British Indian Ocean Territory'), ('kazakhstan', 'Kazakhstan'), ('laos', 'Laos'), ('lebanon', 'Lebanon'), ('latvia', 'Latvia'), ('lithuania', 'Lithuania'), ('liberia', 'Liberia'), ('slovakia', 'Slovakia'),
 ('palmyra atoll', 'Palmyra Atoll'), ('lesotho', 'Lesotho'), ('luxembourg', 'Luxembourg'), ('libya', 'Libya'), ('madagascar', 'Madagascar'), ('martinique', 'Martinique'), ('macao', 'Macao'), ('moldova', 'Moldova'),
 ('mayotte', 'Mayotte'), ('mongolia', 'Mongolia'), ('montserrat', 'Montserrat'), ('malawi', 'Malawi'), ('montenegro', 'Montenegro'), ('macedonia', 'Macedonia'), ('mali', 'Mali'), ('monaco', 'Monaco'),
 ('morocco', 'Morocco'), ('mauritius', 'Mauritius'), ('midway islands', 'Midway Islands'), ('mauritania', 'Mauritania'), ('malta', 'Malta'), ('oman', 'Oman'), ('maldives', 'Maldives'), ('mexico', 'Mexico'),
 ('malaysia', 'Malaysia'), ('mozambique', 'Mozambique'), ('new caledonia', 'New Caledonia'), ('niue', 'Niue'), ('norfolk island', 'Norfolk Island'), ('niger', 'Niger'), ('vanuatu', 'Vanuatu'), ('nigeria', 'Nigeria'),
 ('netherlands','Netherlands'), ('norway', 'Norway'), ('nepal', 'Nepal'), ('nauru', 'Nauru'), ('suriname', 'Suriname'), ('netherlands antilles', 'Netherlands Antilles'), ('nicaragua', 'Nicaragua'),
 ('new zealand', 'New Zealand'), ('paraguay', 'Paraguay'), ('pitcairn', 'Pitcairn'), ('peru', 'Peru'), ('paracel islands', 'Paracel Islands'), ('spratly islands', 'Spratly Islands'), ('pakistan', 'Pakistan'), ('poland', 'Poland'),
 ('panama', 'Panama'), ('portugal', 'Portugal'), ('papua new guinea', 'Papua New Guinea'), ('palau', 'Palau'), ('guinea-bissau', 'Guinea-Bissau'), ('qatar', 'Qatar'), ('serbia', 'Serbia'), ('reunion', 'Reunion'),
 ('marshall islands', 'Marshall Islands'), ('romania', 'Romania'), ('philippines', 'Philippines'), ('puerto rico', 'Puerto Rico'), ('russia', 'Russia'), ('rwanda', 'Rwanda'), ('saudi arabia', 'Saudi Arabia'),
 ('st. pierre and miquelon', 'St. Pierre and Miquelon'), ('st. kitts and nevis', 'St. Kitts and Nevis'), ('seychelles', 'Seychelles'), ('south africa', 'South Africa'), ('senegal', 'Senegal'),
 ('st. helena', 'St. Helena'), ('slovenia', 'Slovenia'), ('sierra leone', 'Sierra Leone'), ('singapore', 'Singapore'), ('somalia', 'Somalia'), ('spain', 'Spain'), ('south sudan', 'South Sudan'), ('st. lucia', 'St. Lucia'),
 ('sudan', 'Sudan'), ('svalbard and jan mayen islands', 'Svalbard and Jan Mayen Islands'), ('sweden', 'Sweden'), ('south georgia and south sandwich is.', 'South Georgia and South Sandwich Is.'), ('syria', 'Syria'),
 ('switzerland', 'Switzerland'), ('trinidad and tobago', 'Trinidad and Tobago'), ('tromelin island', 'Tromelin Island'), ('thailand', 'Thailand'), ('tajikistan', 'Tajikistan'),
 ('turks and caicos islands', 'Turks and Caicos Islands'), ('tokelau', 'Tokelau'), ('tonga', 'Tonga'), ('togo', 'Togo'), ('sao tome and principe', 'Sao Tome and Principe'), ('tunisia', 'Tunisia'), ('timor-leste', 'Timor-Leste'), ('turkey', 'Turkey'),
 ('tuvalu', 'Tuvalu'), ('taiwan', 'Taiwan'), ('turkmenistan', 'Turkmenistan'), ('tanzania', 'Tanzania'), ('uganda', 'Uganda'), ('united kingdom', 'United Kingdom'), ('ukraine', 'Ukraine'),
 ('united states', 'UnitedStates'), ('burkina faso', 'Burkina Faso'), ('uruguay', 'Uruguay'), ('uzbekistan', 'Uzbekistan'), ('st. vincent and the grenadines', 'St. Vincent and the Grenadines'), ('venezuela', 'Venezuela'),
 ('british virgin islands', 'British Virgin Islands'), ('vietnam', 'Vietnam'), ('united states virgin islands', 'United States Virgin Islands'), ('namibia', 'Namibia'), ('palestine', 'Palestine'),
 ('wallis and futuna islands', 'Wallis and Futuna Islands'), ('western sahara', 'Western Sahara'), ('wake island', 'Wake Island'), ('samoa', 'Samoa'), ('eswatini', 'Eswatini'), ('yemen', 'Yemen'), ('zambia', 'Zambia'),
 ('zimbabwe', 'Zimbabwe')]
 
 """
