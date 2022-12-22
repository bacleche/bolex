"""bolexgroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import bolex.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", bolex.views.home, name="home"),
    path("about", bolex.views.about, name="about"),
    path("services", bolex.views.services, name="services"),

    path("expertises/espacevert", bolex.views.espacevert, name="expertises/espacevert"),
    path("expertises/gestionbatiment", bolex.views.gestionbatiment, name="expertises/gestionbatiment"),
    path("expertises/groupeelectrogene", bolex.views.groupeelectrogene, name="expertises/groupeelectrogene"),
    path("expertises/installationelectrique", bolex.views.installationelectrique, name="expertises/installationelectrique"),
    path("expertises/amenagementinterieur", bolex.views.amenagementinterieur, name="expertises/amenagementinterieur"),
    path("expertises/tertiaire", bolex.views.tertiaire, name="expertises/tertiaire"),
    path("expertises/maintenanceclimatisation", bolex.views.maintenanceclimatisation, name="expertises/maintenanceclimatisation"),

    path("nous-decouvrir/flexibilite", bolex.views.flexibilite, name="nous-decouvrir/flexibilite"),
    path("nous-decouvrir/nettoyagelocaux", bolex.views.nettoyagelocaux, name="nous-decouvrir/nettoyagelocaux"),
    path("nous-decouvrir/securite", bolex.views.securite, name="nous-decouvrir/securite"),
    path("nous-decouvrir/expertise", bolex.views.expertise, name="nous-decouvrir/expertise"),
    path("nous-decouvrir/reseau", bolex.views.reseau, name="nous-decouvrir/reseau"),
    path("nous-decouvrir/innovation", bolex.views.innovation, name="nous-decouvrir/innovation"),

    path("plus-value", bolex.views.plusvalue, name="plus-value"),
    path("engagement", bolex.views.engagement, name="engagement"),
    path("contact", bolex.views.contact, name="contact"),


]
