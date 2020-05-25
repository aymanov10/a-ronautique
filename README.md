# a-ronautique
Projet base de données.
Notre trinôme est le suivant  : 
       * Aymane KAMAL SEMLALI 
       * Nacir BOUTRA 
       * Samuel BABA 
        
  
 Notre sujet d'étude porte sur les différentes relations entre les aéroports compagnies, vols ... Notre but est de concevoir une base de données qui gère une agence de voyages aérien ainsi que de créer une application web  qui va contenir un côté
    - Clients : qui sert à 
         * Réserver des vols tout en indiquant une ville de départ X et une autre d'arrivée Y et une date J et qui nous affichera un comparateur de prix des vols partant de X à Y le jour J.
         * Saisir des réclamations des clients qui ont déjà réservé leurs billets.
    - Personnesl : qui a pour but de
         * Ajouter les voyages .
         * Gérer les réservations des clients .
         * Gérer les reclamations des clients .
         * Faire des statistiques .
    
     
  
  
  -Nous récupérons des informations de la page https://openflights.org/data.html  
  -Nous avons téléchargé tous les fichiers csv sauf celui concernant la base de données des avions et nous les avons analysé et nettoyé dans excel avant leur utilisation
  - le dossier essai_aero/elements contient tous les fichiers csv que nous avons eu à utiliser
  - le fichier donnees.py contient tout le code nous ayant permi de peupler les tables Airports,Routes,Airlines... à partir des fichiers csv étant donné que ces informations ne proviennent pas de nous mais du site
  -le fichier forms.py contient la définition de certains formulaires que nous avons à utiliser 
  - Nous avons utilisé Bootstrap, charts.js et jqvmap pour la mise en forme
  - Pour les requêtes select nous avons les différentes listes 
  - Pour la recherche nous avons implémenté la recherche de vols et d'aéroport comme pourrez le voir
  - Pour les requêtes Delete nous avons inclu la possibilté de supprimer des voyages à partir de la liste des voyages
  - Pour les requêtes Update nous avons choisi de l'implémenter au niveau de la réservation des billets: lorsqu'on réserve un billet pour une destination précise,après réservation,le nombre de places est diminué de 1 automatiquement (on fait un update de la table) jusqu'à ce qu'il y ai 0 places et lorsqu'il y a 0 places,lorsque l'utilisateur lance la recherche,l'itinéraire est affichée mais avec un message disant qu'il n'y a plus de places et aussi le bouton réserver n'apparait pas (on ne peut pas réserver un vol s'il n'y a pas de places).
  
  - Pour pouvoir se connecter à l'interface administrateur:
  - assurez-vous d'avoir fait la migration du projet et d'utiliser postgres
  - saisissez manuellement l'adresse http://127.0.0.1:8000/page_ajout_client et ajoutez un utilisateur parce que si vous n'êtes pas enregistré dans la table "auth_user" vous ne pourrez pas accéder à l'interface administrateur.
  -Après avoir créé l'utilisateur vous pourrez vous connecter
  
  




