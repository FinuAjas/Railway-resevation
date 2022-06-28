from django.shortcuts import redirect, render
from . models import *
from django.contrib.auth.decorators import login_required


def home(request):
    From = From_Station.objects.all()
    To = To_Station.objects.all()
    context = {
        'from':From,
        'to':To,
    }
    return render(request,'home.html',context)

def searchtrains(request):
    From = request.GET['from']
    To = request.GET['to']
    routes = Train_Route.objects.filter(From=From,To=To)
    context = {
        'routes':routes,
    }
    return render(request,'search.html',context)

@login_required(login_url='userlogin')
def booktrains(request,code):
    route = Train_Route.objects.get(code=code)
    context = {
        'route':route,
    }
    return render(request,'booking.html',context)


@login_required(login_url='userlogin')
def confirmbooking(request):
    if request.method == 'POST':
        route = Train_Route.objects.get(name=request.POST['route'])
        user = User.objects.get(username=request.user)
        address = request.POST['address']
        number = request.POST['number']
        booking = Booking()
        booking.user = user
        booking.route = route
        booking.useraddress = address
        booking.userphonenumber = number
        booking.pnr_number = f"{user}{route.code}"
        booking.save()
        context = {
            'user' : user,
            'route': route,
            'time' : route.time,
            'address':address,
            'number':number,
            'pnrnumber':booking.pnr_number,
        }
        return render(request,'bookingconfirm.html',context)

@login_required(login_url='userlogin')
def allbookings(request):
    bookings = Booking.objects.filter(user = request.user)
    return render(request, 'allbooking.html',{'bookings':bookings})

@login_required(login_url='userlogin')
def cancelbooking(request,pk):
    booking = Booking.objects.filter(id = pk)
    booking.delete()
    return redirect(allbookings)
