from django.shortcuts import render
from blood.models import *


def Home(request):
    return render(request,'carousel.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Gallery(request):
    return render(request,'gallery.html')

def admin_home(request):
    data = UserProfile.objects.all()
    order = Order.objects.all()
    donate = Blood_Donation.objects.filter(purpose="Blood Donor")
    req = Blood_Donation.objects.filter(purpose="Request for Blood")

    d = {'data':data.count(), 'order':order.count(), 'req':req.count(), 'donate':donate.count()}
    return render(request,'admin_home.html',d)
    