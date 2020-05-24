# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:13:12 2020

@author: ua
"""
from aero.models import Voyages,Reservation,Clients


liste = [["Air Burkina","Dakar","Léopold Sédar Senghor International Airport","Bamako","Modibo Keita International Airport",
 "2020-08-14",250,45],
["Helvetic Airways","Larnaca","Larnaca International Airport","Zurich","Zürich Airport",
 "2020-08-11",250,43],
["Helvetic Airways","Geneva","Geneva Cointrin International Airport","Gran Canaria","Gran Canaria Airport",
 "2020-08-18",250,45],
["Helvetic Airways","Zurich","Zürich Airport","Bordeaux","Bordeaux-Mérignac Airport",
 "2020-08-25",250,45],
["Helvetic Airways","Zurich","Zürich Airport","Bristol","Bristol Airport",
 "2020-08-25",250,45],
["NextJet","Arvidsjaur","Arvidsjaur Airport","Lycksele","Lycksele Airport",
 "2020-08-15",250,45],
["Atlant-Soyuz Airlines","Accra","Kotoka International Airport","Dakar","Léopold Sédar Senghor International Airport",
 "2020-08-15",250,45],
["Atlant-Soyuz Airlines","Accra","Kotoka International Airport","Lagos","Murtala Muhammed International Airport",
 "2020-08-15",250,45],
["Atlant-Soyuz Airlines","Accra","Kotoka International Airport","Monrovia","Roberts International Airport",
 "2020-08-22",250,45],
["Atlant-Soyuz Airlines","Barcelona","Barcelona International Airport","Banjul","Banjul International Airport",
 "2020-08-15",250,45],
["Atlant-Soyuz Airlines","Banjul","Banjul International Airport","Barcelona","Barcelona International Airport",
 "2020-08-12",250,45],
["Atlant-Soyuz Airlines","Banjul","Banjul International Airport","Freetown","Lungi International Airport",
 "2020-08-05",250,45],
["Atlant-Soyuz Airlines","Conakry","Conakry International Airport","Bissau","Osvaldo Vieira International Airport",
 "2020-08-01",250,45],
["Atlant-Soyuz Airlines","Dakar","Léopold Sédar Senghor International Airport","Accra","Kotoka International Airport",
 "2020-08-10",250,45],
["Atlant-Soyuz Airlines","Dakar","Léopold Sédar Senghor International Airport","Banjul","Banjul International Airport",
 "2020-08-10",250,45],
["Atlant-Soyuz Airlines","Dakar","Léopold Sédar Senghor International Airport","Douala","Douala International Airport",
 "2020-08-22",250,45],
["Zip","Djibouti","Djibouti-Ambouli Airport","Dubai","Dubai International Airport",
 "2020-08-28",250,4],
["Zip","Djibouti","Djibouti-Ambouli Airport","Mogadishu","Aden Adde International Airport",
 "2020-08-25",250,45],
["Zip","Mogadishu","Aden Adde International Airport","Nairobi","Jomo Kenyatta International Airport",
 "2020-08-20",200,40],
["Air Arabia Maroc","Brussels","Brussels Airport","Casablanca","Mohammed V International Airport",
 "2020-08-10",200,40],
["Air Arabia Maroc","Casablanca","Mohammed V International Airport","London","London Gatwick Airport",
 "2020-08-10",200,40],
["Air Arabia Maroc","Casablanca","Mohammed V International Airport","Lyon","Lyon Saint-Exupéry Airport",
 "2020-08-10",200,40],
["Airlinair","Aurillac","Aurillac Airport","Paris","Paris-Orly Airport",
 "2020-08-20",200,40],
["Airlinair","Brest","Brest Bretagne Airport","Lyon","Lyon Saint-Exupéry Airport",
 "2020-08-20",200,40],
["Air France","Paris","Paris Charles de Gaulle International Airport","Nantes","Nantes Atlantique Airport",
 "2020-08-10",500,500],
["Air France","Paris","Paris-Orly Airport","Nantes","Nantes Atlantique Airport",
 "2020-08-10",1000,300],
["Alitalia","Paris","Paris Charles de Gaulle International Airport","Nantes","Nantes Atlantique Airport",
 "2020-08-10",200,10]]

for i in liste:
    q=Voyages(compagnie=i[0],ville_depart=i[1],aeroport_depart=i[2],ville_arrive=i[3],aeroport_arrive=i[4],date=i[5],
              price=i[6],places=i[7])
    q.save()
    print("fait")
    
    
liste_clients=[["francois","washington","france",478521456,"francois.was@gmail.com"],
["patrick","malongo","belgium",47852586,"malongo.patrick@gmail.com"],
["françois","dela","france",478521456,"dela@gmail.com"],
["carlos","tchebichev","russia",77478556,"tchebychev@gmail.com"],
["titia","hafidi","spain",478521456,"titia@yahoo.fr"],
["kaka","ricardo","brazil",26547806,"kaka.ricardo@yahoo.com"],
["carmen","chakir","togo",478521456,"chakir@hotmail.com"],
["michel","chfenj","togo",78521456,"chfenjgmail.com"],
["abdel","kawkawa","morocco",8965221456,"kawkawa@yahoo.fr"],
["soulaimane","lguirati","morocco",578526,"lguirati@wanadoo.fr"],
["bro","twachi","algeria",478521456,"twachi@gmail.com"],
["tsu","hu","china",14520785,"tsuhu@yahoo.fr"]]

for i in liste_clients:
    q=Clients(last_name=i[0],first_name=i[1],nationality=i[2],tel=i[3],email=i[4])
    q.save()
    print("done")
    
    
    
liste_reservation=[[59,"francois.was@gmail.com"],
[70,"tsuhu@yahoo.fr"],[60,"tsuhu@yahoo.fr"],[61,"tsuhu@yahoo.fr"],[74,"chakir@hotmail.com"],
[67,"twachi@gmail.com"],[51,"twachi@gmail.com"],[59,"twachi@gmail.com"],[75,"francois.was@gmail.com"],[71,"francois.was@gmail.com"],[70,"francois.was@gmail.com"],
[59,"tchebychev@gmail.com"],[60,"tchebychev@gmail.com"],[64,"tchebychev@gmail.com"],[74,"malongo.patrick@gmail.com"],[67,"malongo.patrick@gmail.com"],
[63,"tchebychev@gmail.com"],
[68,"malongo.patrick@gmail.com"],[67,"francois.was@gmail.com"],[71,"titia@yahoo.fr"],[62,"titia@yahoo.fr"],[69,"niang@yahoo.fr"],
[70,"twachi@gmail.com"],[69,"twachi@gmail.com"],[64,"twachi@gmail.com"],
[64,"kawkawa@yahoo.fr"],[63,"samey@gmail.com"],[68,"tom@gmail.com"],[59,"niang@yahoo.fr"],[64,"samey@gmail.com"],[66,"titi@yahoo.fr"],
[67,"niang@yahoo.fr"],[59,"titia@yahoo.fr"],[62,"francois.was@gmail.com"],[63,"niang@yahoo.fr"],[60,"kader@yahoo.fr"],[65,"kaka@yahoo.com"],[10,"carmen@hotmail.com"],[67,"samey@gmail.com"],
[68,"titia@yahoo.fr"],[68,"mike.nis@gmail.com"],[70,"niang@yahoo.fr"],[65,"denil@gmail.com"],[60,"niang@yahoo.fr"],
[70,"titia@yahoo.fr"],[59,"kaka@yahoo.com"],[62,"niang@yahoo.fr"],[64,"denil@gmail.com"],[62,"niang@yahoo.fr"],[59,"niang@yahoo.fr"],
[64,"samey@gmail.com"],[62,"kader@yahoo.fr"],[69,"niang@yahoo.fr"],[65,"niang@yahoo.fr"],[66,"kaka.ricardo@yahoo.com"],[67,"kaka.ricardo@yahoo.com"],[65,"kaka.ricardo@yahoo.com"],
[70,"titia@yahoo.fr"],[59,"kaka@yahoo.com"],[59,"den@gmail.com"],
[74,"titi@yahoo.fr"],[62,"francois.was@gmail.com"],[60,"carmen@hotmail.com"],[68,"tom@gmail.com"],[62,"carmen@hotmail.com"],[62,"carmen@hotmail.com"],
[65,"chfenjgmail.com"],[66,"chfenjgmail.com"],[68,"chfenjgmail.com"],[60,"chfenjgmail.com"]]
 
 
for i in liste_reservation:
    q=Reservation(reference_voyage=i[0],mail_client=i[1])
    q.save()
    print("done")
