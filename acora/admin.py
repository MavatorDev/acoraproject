from django.contrib import admin
from .models import Equipo
from .models import Partida
from .models import Ranking
from .models import Pista

admin.site.register(Equipo)
admin.site.register(Partida)
admin.site.register(Ranking)
admin.site.register(Pista)
