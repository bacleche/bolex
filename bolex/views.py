from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "bolex/index.html")


def about(request):
    return render(request, "bolex/about.html")


def services(request):
    return render(request, "bolex/services.html")


def espacevert(request):
    return render(request, "bolex/espacevert.html")

def gestionbatiment(request):
    return render(request, "bolex/gestionbatiment.html")

def groupeelectrogene(request):
    return render(request, "bolex/groupeelectrogene.html")

def installationelectrique(request):
    return render(request, "bolex/installationelectrique.html")

def amenagementinterieur(request):
    return render(request, "bolex/amenagementinterieur.html")

def maintenanceclimatisation(request):
    return render(request, "bolex/maintenanceclimatisation.html")

def tertiaire(request):
    return render(request, "bolex/tertiaire.html")


def flexibilite(request):
    return render(request, "bolex/flexibilite.html")



def nettoyagelocaux(request):
    return render(request, "bolex/nettoyagelocaux.html")


def securite(request):
    return render(request, "bolex/securite.html")


def expertise(request):
    return render(request, "bolex/expertise.html")


def reseau(request):
    return render(request, "bolex/reseau.html")


def innovation(request):
    return render(request, "bolex/innovation.html")


def plusvalue(request):
    return render(request, "bolex/plusvalue.html")


def engagement(request):
    return render(request, "bolex/engagement.html")


def contact(request):
    return render(request, "bolex/contact.html", context={"contact": 1})

