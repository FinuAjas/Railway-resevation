from django.contrib import admin
from . models import *

admin.site.register(From_Station)
admin.site.register(To_Station)
admin.site.register(Train_Route)
admin.site.register(Train)
admin.site.register(Booking)