

from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from aero.models import Airports,Airlines,Vols ,Reservation,Clients,Routes,Reclamation,Voyages,Country,Statistics
from aero.forms import AirportForm , AirlinesForm, ClientsForm,ReservationForm,ReclamationForm,RechercheVolForm,VoyagesForm,VolForm

from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login


def home_general(request):
    return render(request,"aero/accueil.html")



############################### Partie Clients #######################


def rechercheVoyage(request):
    if request.method == 'POST':
        form = VolForm(request.POST)
        if form.is_valid():
            query = Voyages.objects.all()
            depart = form.cleaned_data['ville_depart']
            if depart != '':
                query = query.filter(ville_depart=depart)
            arrive = form.cleaned_data['ville_arrive']
            if arrive != '':
                query = query.filter(ville_arrive=arrive)
            date_depart = form.cleaned_data['date']
            if date_depart != '':
                query = query.filter(date=date_depart)
            liste = query
            return render(request, 'aero/voyages.html', {'liste': liste, 'form': form})
    else:
        form = VolForm()
    return render(request, 'aero/voyages.html', locals())


def reservation(request, id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            mail = form.cleaned_data['email']
            query = Clients.objects.filter(email=mail)
            if len(query) == 0:

                k1 = form.save()
                k1.save()

                q1 = Clients.objects.get(email=mail)
                q2 = Reservation(reference_voyage=id,mail_client=q1.email)
                q2.save()
                form2 = Voyages.objects.get(pk=id)
                form2.places = form2.places - 1
                form2.save()
                return redirect('liste_des_voyages_client')
            else:

                q = Clients.objects.get(email=mail)
                w = Reservation(reference_voyage=id,mail_client=q.email)
                w.save()
                form3 = Voyages.objects.get(pk=id)
                form3.places = form3.places - 1
                form3.save()
                return redirect('liste_des_voyages_client')
    else:
        form = ReservationForm()
    return render(request, 'aero/reservation.html',{'form': form})


def reclaim(request):
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['ref_voyage']
            email = form.cleaned_data['email_client']
            query = Reservation.objects.filter(reference_voyage=numero,mail_client=email)
            if len(query)!=0:
                form.save()
                form=ReclamationForm()
                return render(request,'aero/reclamation.html',{ 'form': form})

    else:
        form = ReclamationForm()
    return render(request,'aero/reclamation.html',locals())
            

######################## Partie Authentification  #######################
    


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dahsboard_admin")
            else:
                msg = 'Données incorrectes'
        else:
            msg = 'Erreur lors de la validation du formulaire'

    return render(request, "aero/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Administrateur créé'
            success = True

        
        else:
            msg = 'Informations pas correctes'
    else:
        form = SignUpForm()

    return render(request, "aero/register.html", {"form": form, "msg": msg, "success": success})



######################## Partie Personnels  #######################


def airport_list(request):
    context = {'airports_list': Airports.objects.all()}
    return render(request,"aero/airports_list.html",context)



def vols_liste(request):
    context = {'les_vols': Vols.objects.all()}
    return render(request, "aero/listes_des_vols.html", context)


def voyages_liste(request):
    context = {'les_voyages': Voyages.objects.all()}
    return render(request, "aero/liste_des_voyages.html", context)


def reservations_liste(request):
    context = {'les_reservations': Reservation.objects.all()}
    return render(request, "aero/liste_des_reservations.html", context)

def airlines_liste(request):
    context ={'les_compagnies': Airlines.objects.all()}
    return render(request,"aero/liste_des_compagnies.html",context)


def clients_liste(request):
    context= {'les_clients': Clients.objects.all()}
    return render(request,"aero/liste_des_clients.html",context)


def reclamation_liste(request):
    context= {'les_reclamations': Reclamation.objects.all()}
    return render(request,"aero/liste_reclamations.html",context)


def home_admin(request):
    codes = []
    liste_img=[]
    liste_pays=[]
    nombre_pays= []
    liste=[]
    liste_reservation=[0,0,0,0,0,0,0,0,0,0,0,0]
    liste_voyages=[0,0,0,0,0,0,0,0,0,0,0,0]
    total = len(Clients.objects.all())

    for i in Reservation.objects.all():
        q=Voyages.objects.get(pk=i.reference_voyage)
        liste_reservation[q.date.month-1] += 1

    for i in Voyages.objects.all():
        q=i.date.month
        liste_voyages[q-1] += 1

    for i in Clients.objects.values('nationality').distinct():
        # q1= Statistics.objects.get(nom_pays=i['nationality'].title())
        if i['nationality']=="cote d'ivoire":
            le_nom="Cote d'Ivoire"
            q2 = Country.objects.get(name=le_nom)
        else:
            q2 = Country.objects.get(name=i['nationality'].title())
        nom= q2.name
        image = q2.iso_code.lower()
        num = len(Clients.objects.filter(nationality=nom.lower()))
        pourcent = (num/total)*100
        if len(Statistics.objects.filter(nom_pays=i['nationality'].title())) == 0 :
            k = Statistics(nom_pays=nom,img=image,number=num,percentage=pourcent)
            k.save()
        else:
            q1 = Statistics.objects.get(nom_pays=i['nationality'].title())
            q1.number = num
            q1.percentage = pourcent
            q1.save()

        codes.append(q2.iso_code)



    """"
    for i in Clients.objects.values('nationality').distinct():
        dico=dict()
        q = Country.objects.get(name=i['nationality'].title())
        q2= Clients.objects.filter(nationality=q.name.lower())
        dico['image'] = q.iso_code.lower()
        dico['pays']=q.name
        dico['nombre']=len(q2)
        liste.append(dico)
        codes.append(q.iso_code)
        
        """
    liste_pays_pluriel=[]
    for i in Reservation.objects.all():
        q1 = Voyages.objects.get(pk=i.reference_voyage)
        q_interm= q1.aeroport_arrive
        q2 = q1.ville_arrive
        q3 = Airports.objects.get(name=q_interm,city=q2)
        q4 = q3.country
        liste_pays_pluriel.append(q4)
    liste_dico=[]
    for i in liste_pays_pluriel:
        if {"pays": i, "num": liste_pays_pluriel.count(i)} not in liste_dico:
            liste_dico.append({"pays": i, "num": liste_pays_pluriel.count(i)})

    liste_dico=sorted(liste_dico,key=lambda d:d["num"])
    pays_prefere=[]
    nombre=[]
    for i in liste_dico:
        pays_prefere.append(i["pays"])
        nombre.append(i["num"])



    context = {'variable': 'id',
               'liste_codes': codes,
               'courbe_voyages': liste_voyages,
               'courbe_reservation': liste_reservation,
               'pays_pref': pays_prefere[-10:],
               'effectif' : nombre[-10:],
               'liste' : Statistics.objects.all()
               }
    return render(request,"aero/admin_dashboard.html",context)


def maison(request):
    return redirect(airport_list)


def airports(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            query = Airports.objects.all()
            name = form.cleaned_data['name']
            if name != '':
                query = query.filter(name=name)
            city = form.cleaned_data['city']
            if city != '':
                query = query.filter(city=city)
            country = form.cleaned_data['country']
            if country != '':
                query = query.filter(country=country)
            IATA_airport = form.cleaned_data['IATA_airport']
            if IATA_airport != '':
                query = query.filter(IATA_airport=IATA_airport)
            ICAO_airport = form.cleaned_data['ICAO_airport']
            if ICAO_airport != '':
                query = query.filter(ICAO_airport=ICAO_airport)
            latitude = form.cleaned_data['latitude']
            if latitude != '':
                query = query.filter(latitude=latitude)
            longitude = form.cleaned_data['longitude']
            if longitude != '':
                query = query.filter(longitude=longitude)
            altitude = form.cleaned_data['altitude']
            if altitude != '':
                query = query.filter(altitude=altitude)
            liste = query
            return render(request, 'aero/airports.html', {'liste': liste, 'form': form})
    else:
        form = AirportForm()
    return render(request, 'aero/airports.html', locals())


def rechercheVol(request):
    if request.method == 'POST':
        form = RechercheVolForm(request.POST)
        if form.is_valid():
            query = Vols.objects.all()
            compagnie = form.cleaned_data['airline']
            if compagnie != '':
                query = query.filter(airline=compagnie)
            ville_depart = form.cleaned_data['departure_city']
            if ville_depart != '':
                query = query.filter(departure_city=ville_depart)
            aeroport_depart = form.cleaned_data['departure_airport']
            if aeroport_depart != '':
                query = query.filter(departure_airport=aeroport_depart)
            ville_arrive = form.cleaned_data['arrival_city']
            if ville_arrive != '':
                query = query.filter(arrival_city=ville_arrive)
            aeroport_arrive = form.cleaned_data['arrival_airport']
            if aeroport_arrive != '':
                query = query.filter(arrival_airport=aeroport_arrive)
            liste = query
            return render(request, 'aero/recherche_vol.html', {'liste': liste, 'form': form})
    else:
        form = RechercheVolForm()
    return render(request, 'aero/recherche_vol.html', locals())


def voyage(request):
    if request.method == "GET":
        form = VoyagesForm()
        return render(request, "aero/ajout_voyages.html", {'form': form})
    else:
        form = VoyagesForm(request.POST)
        if form.is_valid():
            if Vols.objects.get(airline=form.cleaned_data['compagnie'], departure_city=form.cleaned_data['ville_depart'],
                                departure_airport=form.cleaned_data['aeroport_depart'],arrival_city=form.cleaned_data['ville_arrive'],
                                arrival_airport=form.cleaned_data['aeroport_arrive']) in Vols.objects.all():
                form.save()
            return redirect('ajout_voyage')


def delete_voyage(request,id):
    voyage = Voyages.objects.get(pk=id)
    voyage.delete()
    return redirect('liste_des_voyages')