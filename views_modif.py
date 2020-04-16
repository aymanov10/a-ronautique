from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from appligp2.models import Airports,Airlines,Personnels, Clients, Voyages, Routes
from appligp2.forms import AirportForm , AirlinesForm, PersonnelsForm, ClientsForm, VoyagesForm , AjoutvoyagesForm, RoutesForm
from django.shortcuts import redirect


def Home(request):
    return render(request , 'Home.html')
    #return HttpResponse("Ceci est la page d'accueil de l'application mon appli de mon projet monprojet.\n")


def lire(request):
    aeroports = Airports.objects.filter(city ='Paris').values_list('airport_id') 
    #print(aeroports[0][0])
    return render(request,'aeroports.html',{                                          
            'aeroports': aeroports})
    #return HttpResponse(Airports.objects.all())
   

def airports(request):
    if request.method == 'POST' :
        form = AirportForm(request.POST)
        if form.is_valid():
            query = Airports.objects.all()
            #print(query)
            airport_id=form.cleaned_data['airport_id']
            print(airport_id)

            if  airport_id!=None:
                print(airport_id)
                print(query)
                query = query.filter(airport_id=airport_id)
            
            name = form.cleaned_data['name']
            if name != '' :
                query = query.filter(name=name)
            city = form.cleaned_data['city']
            
            if city != '' :
                print(city)
                query = query.filter(city=city)

               
            country = form.cleaned_data['country']
            if country != '' :
                query = query.filter(country=country)
            print(query)    
            IATA_airport = form.cleaned_data['IATA_airport']
            if IATA_airport != '':
                query = query.filter(IATA_airport=IATA_airport)
            ICAO_airport = form.cleaned_data['ICAO_airport']
            if ICAO_airport != '' :
                query = query.filter(ICAO_airport=ICAO_airport)
            '''
            latitude = form.cleaned_data['latitude']

            if isinstance(latitude , float)==True:
                query = query.filter(latitude=latitude)
            longitude = form.cleaned_data['longitude'] 
            print(longitude)
            if isinstance(longitude , float)==True :
                query = query.filter(longitude=longitude)
               
            altitude = form.cleaned_data['altitude']
            if isinstance(altitude , float)==True :
                query = query.filter(altitude=altitude)
            '''
            liste =  query  
            #return redirect('airports/')
            return render(request,'airports.html', {'liste' : liste, 'form' : form}) 
    else:
        form = AirportForm()
    return render(request,'airports.html',locals())

def airlines(request):
    if request.method == 'POST' :
        form = AirlinesForm(request.POST)
        if form.is_valid():
            query = Airlines.objects.all()
            
            airline_id = form.cleaned_data['airline_id']
            if airline_id != None :
                query = query.filter(airline_id=airline_id)
              
            name = form.cleaned_data['name']
            if name != '' :
                query = query.filter(name=name)
            alias = form.cleaned_data['alias']
            if alias != '' :
                query = query.filter(alias=alias)
            IATA_airline = form.cleaned_data['IATA_airline']
            if IATA_airline != '' :
                query = query.filter(IATA_airline=IATA_airline)
            ICAO_airline = form.cleaned_data['ICAO_airline']
            if ICAO_airline != '' :
                query = query.filter(ICAO_airline=ICAO_airline)
            liste =  query         
            return render(request,'airlines.html', {'liste' : liste, 'form' : form}) 
    else:
        form = AirlinesForm()
    return render(request,'airlines.html',locals())


def routes(request):
    if request.method == 'POST' :
        form = RoutesForm(request.POST)

        if form.is_valid():
           
            query = Routes.objects.all()
            #print(query)

            source_airport = form.cleaned_data['source_airport']
            if source_airport != '' :
                query = query.filter(source_airport=source_airport)
                print(query)

            destination_airport = form.cleaned_data['destination_airport']
            if destination_airport != '' :
                query = query.filter(destination_airport=destination_airport)
                #print(query)
            route_id = form.cleaned_data['route_id']

            if route_id != None :
                #print(route_id)
                query = query.filter(pk=route_id)
                print(query)
            
           
           
            airline_id = form.cleaned_data['airline_id']
            
            if airline_id != None :
                query = query.filter(airline_id_id=airline_id)

               
            source_airport_id = form.cleaned_data['source_airport_id']
            
            if source_airport_id!= None :
                query = query.filter(source_airport_id_id=source_airport_id)

               
            destination_airport_id = form.cleaned_data['destination_airport_id']
            if destination_airport_id != None :
                query = query.filter(destination_airport_id_id=destination_airport_id)
            
            liste =  query         
            return render(request,'routes.html', {'liste' : liste, 'form' : form}) 
    else:
        form = RoutesForm()
    return render(request,'routes.html',locals())


def statistiques(request):
        return HttpResponse("Ceci est la page des statistiques.\n")

    
    
            
def personnels(request):
    if request.method == 'POST' :
        form = PersonnelsForm(request.POST)
        if form.is_valid():
            query = Personnels.objects.all()
            nom_utilisateur = form.cleaned_data['nom_utilisateur']
            if nom_utilisateur != '' :
                query = query.filter(nom_utilisateur=nom_utilisateur)
            mot_de_passe = form.cleaned_data['mot_de_passe']
            if mot_de_passe != '' :
                query = query.filter(mot_de_passe=mot_de_passe)
            liste =  query         
            return render(request,'personnels.html', {'liste' : liste, 'form' : form}) 
    else:
        form = PersonnelsForm()
    return render(request,'personnels.html',locals())


def support(request):
    return render(request , 'support.html')
    
def ajout(request):
    if request.method == 'POST' :
        form = AjoutvoyagesForm(request.POST)
        if form.is_valid():
            routes_id = form.cleaned_data['routes_id']
            date = form.cleaned_data['date']
            Prix = form.cleaned_data['Prix']
            perssonels_id = form.cleaned_data['perssonels_id']
            Voyages.objects.create(date=date,Prix=Prix,perssonels_id=perssonels_id,routes_id=routes_id)           
            #return render(request,'formulaire_ajout_voyage.html', {'liste' : liste, 'form' : form}) 
            return redirect('v_enregistrer/')           
    else:
        form = AjoutvoyagesForm()
    return render(request,'formulaire_ajout_voyage.html',locals())
    
    #return HttpResponse("Ceci est la page d ajout de  voyage.\n")   
def v_enregistrer(request):
    return HttpResponse("vol enregistre.\n")
    

def clients(request):
    if request.method == 'POST' :
        form = ClientsForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            nationality = form.cleaned_data['nationality']
            tel = form.cleaned_data['tel']
            email = form.cleaned_data['email']
            Clients.objects.create(last_name=last_name,first_name=first_name,nationality=nationality,tel=tel,email=email)          
            return redirect('ticket/')           
    else:
        form = ClientsForm()
    return render(request,'formulaire_clients.html',locals())

def ticket(request):
    return HttpResponse("ticket reserve.\n")
    
       
def voyage(request):
    if request.method == 'POST' :
        form = VoyagesForm(request.POST)
        if form.is_valid():
            query = Voyages.objects.all()
            depart = form.cleaned_data['depart']
            query1 = Airports.objects.filter(city = depart).values_list('airport_id') 
            print(query1[0][0])
            arrivee = form.cleaned_data['arrivee']
            query2 = Airports.objects.filter(city = arrivee).values_list('airport_id')
            print(query2[0][0])
            #for i in range(len(query1)):
            #    for j in range(len(query2)):
            query3 = Routes.objects.filter(source_airport_id_id = query1[0][0] ,destination_airport_id_id = query2[2][0]).values_list('route_id','airline_id_id')
            #       if query3 != '' :
            print(query3[0][0],query3[0][1])
            query4 = Airlines.objects.filter(airline_id = query3[0][1])
            date = form.cleaned_data['date']
            query = query.filter(routes_id = query3[0][0], date = date )
            liste =  query 
            liste1 = query4
            #return HttpResponse("Ceci est la page des comparateurs.\n")   
            #return redirect('airports/')
            return render(request,'voyage.html', {'liste' : liste, 'liste1' : liste1, 'form' : form}) 
    else:
        form = VoyagesForm()
    return render(request,'voyage.html',locals())

            
            #return redirect('voyage/')   







    
'''            
    airport_id = 5
    aeroports = get_object_or_404(Airports,airport_id = airport_id)
    return render(request,'aeroport.html',{                                          
            'aeroports': aeroports})
'''       
        