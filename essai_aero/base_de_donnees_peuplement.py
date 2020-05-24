# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:19:20 2020

@author: samue
"""
from aero.models import Voyages,Reservation,Clients


liste = [["Air Burkina","Dakar","Léopold Sédar Senghor International Airport","Bamako","Modibo Keita International Airport",
 "2020-05-14",250,45],
["Helvetic Airways","Larnaca","Larnaca International Airport","Zurich","Zürich Airport",
 "2020-09-11",250,43],
["Helvetic Airways","Geneva","Geneva Cointrin International Airport","Gran Canaria","Gran Canaria Airport",
 "2020-11-18",250,45],
["Helvetic Airways","Zurich","Zürich Airport","Bordeaux","Bordeaux-Mérignac Airport",
 "2020-12-25",250,45],
["Helvetic Airways","Zurich","Zürich Airport","Bristol","Bristol Airport",
 "2020-10-25",250,45],
["NextJet","Arvidsjaur","Arvidsjaur Airport","Lycksele","Lycksele Airport",
 "2020-02-15",250,45],
["Atlant-Soyuz Airlines","Accra","Kotoka International Airport","Dakar","Léopold Sédar Senghor International Airport",
 "2020-07-15",250,45],
["Atlant-Soyuz Airlines","Accra","Kotoka International Airport","Lagos","Murtala Muhammed International Airport",
 "2020-08-15",250,45],
["Atlant-Soyuz Airlines","Accra","Kotoka International Airport","Monrovia","Roberts International Airport",
 "2020-06-22",250,45],
["Atlant-Soyuz Airlines","Barcelona","Barcelona International Airport","Banjul","Banjul International Airport",
 "2020-07-15",250,45],
["Atlant-Soyuz Airlines","Banjul","Banjul International Airport","Barcelona","Barcelona International Airport",
 "2020-04-12",250,45],
["Atlant-Soyuz Airlines","Banjul","Banjul International Airport","Freetown","Lungi International Airport",
 "2020-10-05",250,45],
["Atlant-Soyuz Airlines","Conakry","Conakry International Airport","Bissau","Osvaldo Vieira International Airport",
 "2020-05-01",250,45],
["Atlant-Soyuz Airlines","Dakar","Léopold Sédar Senghor International Airport","Accra","Kotoka International Airport",
 "2020-09-10",250,45],
["Atlant-Soyuz Airlines","Dakar","Léopold Sédar Senghor International Airport","Banjul","Banjul International Airport",
 "2020-03-10",250,45],
["Atlant-Soyuz Airlines","Dakar","Léopold Sédar Senghor International Airport","Douala","Douala International Airport",
 "2020-06-22",250,45],
["Zip","Djibouti","Djibouti-Ambouli Airport","Dubai","Dubai International Airport",
 "2020-04-28",250,4],
["Zip","Djibouti","Djibouti-Ambouli Airport","Mogadishu","Aden Adde International Airport",
 "2020-11-25",250,45],
["Zip","Mogadishu","Aden Adde International Airport","Nairobi","Jomo Kenyatta International Airport",
 "2020-04-20",200,40],
["Air Arabia Maroc","Brussels","Brussels Airport","Casablanca","Mohammed V International Airport",
 "2020-01-10",200,40],
["Air Arabia Maroc","Casablanca","Mohammed V International Airport","London","London Gatwick Airport",
 "2020-02-10",200,40],
["Air Arabia Maroc","Casablanca","Mohammed V International Airport","Lyon","Lyon Saint-Exupéry Airport",
 "2020-02-10",200,40],
["Airlinair","Aurillac","Aurillac Airport","Paris","Paris-Orly Airport",
 "2020-04-20",200,40],
["Airlinair","Brest","Brest Bretagne Airport","Lyon","Lyon Saint-Exupéry Airport",
 "2020-04-20",200,40],
["Air France","Paris","Paris Charles de Gaulle International Airport","Nantes","Nantes Atlantique Airport",
 "2020-06-10",500,500],
["Air France","Paris","Paris-Orly Airport","Nantes","Nantes Atlantique Airport",
 "2020-06-10",1000,300],
["Alitalia","Paris","Paris Charles de Gaulle International Airport","Nantes","Nantes Atlantique Airport",
 "2020-06-10",200,10]]

for i in liste:
    q=Voyages(compagnie=i[0],ville_depart=i[1],aeroport_depart=i[2],ville_arrive=i[3],aeroport_arrive=i[4],date=i[5],
              price=i[6],places=i[7])
    q.save()
    print("fait")


 

liste_clients=[["denszel","washington","france",478521456,"den@gmail.com"],
["vin","diezel","belgium",47852586,"diezel@gmail.com"],
["françois","mitterand","france",478521456,"denil@gmail.com"],
["carlos","samey","russia",77478556,"samey@gmail.com"],
["titiane","bawara","spain",478521456,"titi@yahoo.fr"],
["kaka","lucas","brazil",26547806,"kaka@yahoo.com"],
["carmen","gnonfam","togo",478521456,"carmen@hotmail.com"],
["michel","ninsao","togo",78521456,"mike.nis@gmail.com"],
["abdel","kader","morocco",8965221456,"kader@yahoo.fr"],
["prisicilia","badassou","morocco",578526,"bds@wanadoo.fr"],
["brown","thomson","algeria",478521456,"tom@gmail.com"],
["niang","chou","china",14520785,"niang@yahoo.fr"]]

for i in liste_clients:
    q=Clients(last_name=i[0],first_name=i[1],nationality=i[2],tel=i[3],email=i[4])
    q.save()
    print("done")

liste_reservation=[[3,"den@gmail.com"],
[12,"mike.nis@gmail.com"],[24,"mike.nis@gmail.com"],[22,"mike.nis@gmail.com"],[20,"bds@wanadoo.fr"],
[5,"den@gmail.com"],[10,"den@gmail.com"],[15,"kader@yahoo.fr"],[3,"den@gmail.com"],[22,"den@gmail.com"],[6,"den@gmail.com"],
[19,"samey@gmail.com"],[20,"bds@wanadoo.fr"],[24,"niang@yahoo.fr"],[3,"kader@yahoo.fr"],[23,"kader@yahoo.fr"],
[23,"niang@yahoo.fr"],
[18,"bds@wanadoo.fr"],[17,"den@gmail.com"],[21,"titi@yahoo.fr"],[22,"titi@yahoo.fr"],[19,"niang@yahoo.fr"],
[20,"kader@yahoo.fr"],[19,"kader@yahoo.fr"],[14,"mike.nis@gmail.com"],
[14,"kader@yahoo.fr"],[23,"samey@gmail.com"],[18,"tom@gmail.com"],[9,"niang@yahoo.fr"],[14,"samey@gmail.com"],[16,"titi@yahoo.fr"],
[17,"niang@yahoo.fr"],[19,"samey@gmail.com"],[22,"den@gmail.com"],[23,"niang@yahoo.fr"],[20,"kader@yahoo.fr"],[15,"kaka@yahoo.com"],[10,"carmen@hotmail.com"],[7,"samey@gmail.com"],
[8,"tom@gmail.com"],[8,"mike.nis@gmail.com"],[10,"niang@yahoo.fr"],[15,"denil@gmail.com"],[20,"niang@yahoo.fr"],
[20,"kaka@yahoo.com"],[19,"kaka@yahoo.com"],[22,"niang@yahoo.fr"],[4,"denil@gmail.com"],[2,"niang@yahoo.fr"],[19,"niang@yahoo.fr"],
[24,"samey@gmail.com"],[22,"kader@yahoo.fr"],[9,"niang@yahoo.fr"],[5,"niang@yahoo.fr"],[6,"kaka@yahoo.com"],[7,"kaka@yahoo.com"],[15,"tom@gmail.com"],
[20,"kaka@yahoo.com"],[9,"kaka@yahoo.com"],[9,"den@gmail.com"],
[14,"titi@yahoo.fr"],[22,"kader@yahoo.fr"],[20,"carmen@hotmail.com"],[18,"tom@gmail.com"],[22,"carmen@hotmail.com"],[22,"carmen@hotmail.com"],
[15,"kader@yahoo.fr"],[16,"titi@yahoo.fr"],[8,"samey@gmail.com"],[20,"den@gmail.com"]]
 
 
for i in liste_reservation:
    q=Reservation(reference_voyage=i[0],mail_client=i[1])
    q.save()
    print("done")
