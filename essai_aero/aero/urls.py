
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home_general,name='welcome'),
    path('debut',views.maison,name='retour_maison'),
    path('aeroports/',views.airport_list,name='liste_des_aeroports'),
    path('voyages', views.voyage,name="ajout_voyage"),
    path('vols', views.rechercheVoyage,name="liste_des_voyages_client"),
    path('reclamation/',views.reclaim,name="page_des_reclamations"),
    path('list_of_airports/',views.airport_list),
    path('reservation_page/<int:id>',views.reservation,name='reservation'),
    path('index_admin/',views.home_admin,name='dahsboard_admin'),
    # path('liste_des_voyages',views.voyages_liste,name='liste_des_voyages'),
    path('liste_des_voyages_admin',views.voyages_liste,name='liste_des_voyages'),
    path('liste_des_reservations',views.reservations_liste,name='liste_des_reservations'),
    path('page_de_connexion',views.login_view,name='login_page'),
    path('page_ajout_client',views.register_user,name='register_page'),
    path('airports/', views.airports, name='airports'),
    path('liste_vols_dispo/',views.vols_liste,name='liste_des_vols'),
    path('liste_des_compagnies/',views.airlines_liste,name="liste_des_compagnies"),
    path('liste_des_clients',views.clients_liste,name="liste_des_clients"),
    path('recherche_vol',views.rechercheVol,name='recherche_de_vol'),
    path('liste_des_reclamations',views.reclamation_liste,name="liste_des_reclamations"),
    path('supression_voyage/<int:id>',views.delete_voyage,name='supprimer_voyage')

]