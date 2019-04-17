from django.contrib import admin
from .models import Equipo
from .models import Partida
from .models import Ranking

admin.site.register(Equipo)
admin.site.register(Partida)
admin.site.register(Ranking)
