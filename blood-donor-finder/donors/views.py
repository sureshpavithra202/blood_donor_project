from django.shortcuts import render, redirect
from .models import Donor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def donor_list(request):
    blood_group = request.GET.get("blood_group", "")
    city = request.GET.get("city", "")

    donors = Donor.objects.filter(available=True)

    if blood_group:
        donors = donors.filter(blood_group__iexact=blood_group)

    if city:
        donors = donors.filter(city__icontains=city)

    return render(
        request,
        "donors/donor_list.html",
        {"donors": donors}
    )

def add_donor(request):

    if request.method == "POST":
        Donor.objects.create(
            name=request.POST["name"],

blood_group=request.POST["blood_group"],
            phone=request.POST["phone"],
            city=request.POST["city"],

available=request.POST["available"] == "True"
        )
        return redirect("/donors/")

    return render(request, "donors/add_donor.html")

def edit_donor(request, id):
    donor = Donor.objects.get(id=id)

    if request.method == "POST":
        donor.name = request.POST["name"]
        donor.blood_group = request.POST["blood_group"]
        donor.phone = request.POST["phone"]
        donor.city = request.POST["city"]
        donor.available = request.POST["available"] == "True"
        donor.save()

        return redirect("/donors/")

    return render(request, "donors/edit_donor.html", {"donor": donor})

def delete_donor(request, id):
    donor = Donor.objects.get(id=id)
    donor.delete()
    return redirect("/donors/")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("/login/")

    return render(request, "donors/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/donors/")

    return render(request, "donors/login.html")

def user_logout(request):
    logout(request)
    return redirect("/login/")    