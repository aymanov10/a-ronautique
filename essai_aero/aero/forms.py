# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:19:04 2020

@author: ua
"""

from django import forms
from .models import Clients,Reclamation,Vols,Voyages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES=sorted([('bhutan', 'Bhutan'), ('haiti', 'Haiti'), ('aruba', 'Aruba'), ('antigua and barbuda', 'Antigua and Barbuda'), ('united arab emirates', 'United Arab Emirates'), ('afghanistan', 'Afghanistan'), ('algeria', 'Algeria'), ('azerbaijan', 'Azerbaijan'), ('albania', 'Albania'), ('armenia', 'Armenia'), ('angola', 'Angola'), ('argentina', 'Argentina'), ('australia', 'Australia'),
 ('ashmore and cartier islands', 'Ashmore and Cartier Islands'), ('austria', 'Austria'), ('anguilla', 'Anguilla'), ('antarctica', 'Antarctica'), ('bahrain', 'Bahrain'), ('barbados', 'Barbados'), ('botswana', 'Botswana'),
 ('bermuda', 'Bermuda'), ('belgium', 'Belgium'), ('bahamas', 'Bahamas'), ('belize', 'Belize'), ('bosnia and herzegovina', 'Bosnia and Herzegovina'), ('bolivia', 'Bolivia'), ('myanmar', 'Myanmar'),
 ('benin', 'Benin'), ('belarus', 'Belarus'), ('solomon islands', 'Solomon Islands'), ('navassa island', 'Navassa Island'), ('brazil', 'Brazil'), ('clipperton island', 'Clipperton Island'), ('bulgaria', 'Bulgaria'),
 ('brunei darussalam', 'Brunei Darussalam'), ('burundi', 'Burundi'), ('canada', 'Canada'), ('cambodia', 'Cambodia'), ('chad', 'Chad'), ('sri lanka', 'Sri Lanka'), ('dr congo', 'DR Congo'),
 ('congo republic', 'Congo Republic'), ('china', 'China'), ('chile', 'Chile'), ('cayman islands', 'Cayman Islands'), ('cameroon', 'Cameroon'), ('comoros', 'Comoros'), ('colombia', 'Colombia'),
 ('northern mariana islands', 'Northern Mariana Islands'), ('coral sea islands', 'Coral Sea Islands'), ('costa rica', 'Costa Rica'), ('central african republic', 'Central African Republic'), ('cuba', 'Cuba'), ('cabo verde', 'Cabo Verde'),
 ('cook islands', 'Cook Islands'), ('cyprus', 'Cyprus'), ('denmark', 'Denmark'), ('djibouti', 'Djibouti'), ('dominica', 'Dominica'), ('dominican republic', 'Dominican Republic'), ('ecuador', 'Ecuador'), ('egypt', 'Egypt'),
 ('ireland', 'Ireland'),('equatorial guinea', 'Equatorial Guinea'), ('estonia', 'Estonia'), ('eritrea', 'Eritrea'), ('el salvador', 'El Salvador'), ('ethiopia', 'Ethiopia'), ('europa island', 'Europa Island'),
 ('czech republic', 'Czech Republic'), ('french guiana', 'French Guiana'), ('finland', 'Finland'), ('fiji', 'Fiji'), ('faeroe islands', 'Faeroe Islands'),
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
 ('zimbabwe', 'Zimbabwe')])


class AirportForm(forms.Form):
    name = forms.CharField(max_length=50,required = False)
    city = forms.CharField(max_length=50,required = False)
    country = forms.CharField(max_length=50,required = False)
    IATA_airport = forms.CharField(max_length=8,required = False)
    ICAO_airport = forms.CharField(max_length=8,required = False)
    latitude = forms.CharField(max_length=50,required = False)
    longitude = forms.CharField(max_length=50,required = False)
    altitude = forms.CharField(max_length=15,required = False)
    

class AirlinesForm(forms.Form):
    name = forms.CharField(max_length=40,required = False)
    alias = forms.CharField(max_length=40,required = False)
    IATA_airline = forms.CharField(max_length=8,required = False)
    ICAO_airline = forms.CharField(max_length=8,required = False)
    

class ClientsForm(forms.Form):    
    last_name = forms.CharField(max_length=40,required = True)
    first_name = forms.CharField(max_length=40,required = True)
    nationality= forms.CharField(max_length=40,required = True)
    tel = forms.CharField(max_length=25,required = True)
    email = forms.EmailField(required = True)


class PersonnelsForm(forms.Form):
    nom_utilisateur = forms.CharField(max_length=40,required = True)
    mot_de_passe = forms.CharField(max_length=40,required = True)


class VoyagesForm(forms.ModelForm):
    class Meta:
        model = Voyages
        fields = ('compagnie','ville_depart','aeroport_depart','ville_arrive','aeroport_arrive','date','price','places')
        labels = {
            'compagnie': 'Compagnie',
            'ville_depart': 'Ville de départ',
            'aeroport_depart': 'Aéroport de départ',
            'ville_arrive': 'Ville de destination',
            'aeroport_arrive': 'Aéroport d\'arrivée',
            'date': 'Date ',
            'price': 'Prix',
            'places' : 'Nombre de places disponibles'
        }

        widgets = {
            'date': forms.SelectDateWidget(),
        }



class VolForm(forms.ModelForm):
    class Meta:
        model = Voyages
        fields = ('ville_depart','ville_arrive','date')
        labels = {
            'ville_depart': 'Ville de départ',
            'ville_arrive': 'Ville d\'arrivée',
            'date': 'Jour de départ',
        }

        widgets = {
            'date': forms.SelectDateWidget(),
        }


class ReservationForm(forms.ModelForm):
    nationality = forms.CharField( widget=forms.Select(choices=CHOICES))

    class Meta:
        model = Clients
        fields = ('last_name','first_name','nationality','tel','email')
        labels = {
            'last_name': 'Nom',
            'first_name': 'Prénom',
            'nationality': 'Nationalité',
            'tel': 'Téléphone',
            'email': 'Adresse mail',
        }


CHOIX= [('probleme de connexion','Problème de connexion'),
        ('remboursement d\'un vol annule','Remboursement d\'un vol annulé'),
        ('autres plaintes/demandes','Autres plaintes/demandes')]


class ReclamationForm(forms.ModelForm):
    categorie = forms.CharField(widget=forms.Select(choices=CHOIX))

    class Meta:
        model = Reclamation
        fields = ('ref_voyage','email_client','categorie','message')
        labels = {
            'ref_voyage' : 'Référence voyage',
            'email_client' : 'Email',
            'categorie' : 'Objet du message',
            'message' : 'Votre message '
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Nom d'utilisateur",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Mot de passe",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Nom d'utilisateur",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Mot de passe",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirmation de mot de passe",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RechercheVolForm(forms.ModelForm):
    airline = forms.CharField(required=False)
    departure_city = forms.CharField(required=False)
    departure_airport = forms.CharField(required=False)
    arrival_city = forms.CharField(required=False)
    arrival_airport = forms.CharField(required=False)

    class Meta:
        model = Vols
        fields = ('airline','departure_city','departure_airport','arrival_city','arrival_airport')
        labels = {
            'airline' : 'Compagnie',
            'departure_city' : 'Ville de départ',
            'departure_airport' : 'Aéroport de départ',
            'arrival_city' : 'Ville d\'arrivée',
            'arrival_airport' : 'Aéroport d\'arrivée'
        }










