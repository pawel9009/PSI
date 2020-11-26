from django.contrib import admin
from .models import Pracownicy
from .models import Klient
from .models import Adopcja
from .models import Zwiarzak


admin.site.register(Pracownicy)
admin.site.register(Klient)
admin.site.register(Adopcja)
admin.site.register(Zwiarzak)


# Register your models here.
