from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('searchtrains/',views.searchtrains,name='searchtrains'),
    path('booktrains/<str:code>/',views.booktrains,name='booktrains'),
    path('confirmbooking/',views.confirmbooking,name='confirmbooking'),
    path('allbookings/',views.allbookings,name='allbookings'),
    path('cancelbooking/<int:pk>/',views.cancelbooking,name='cancelbooking'),
]