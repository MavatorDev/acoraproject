from django.contrib import admin
from .models import Equipo
from .models import Partida
from .models import Ranking
from .models import Codigos
from .models import Comentarios

admin.site.register(Equipo)
admin.site.register(Partida)
admin.site.register(Ranking)
admin.site.register(Codigos)
admin.site.register(Comentarios)
