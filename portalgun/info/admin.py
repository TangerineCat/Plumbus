from django.contrib import admin

# Register your models here.

from .models import Identity, Team, Alignment

admin.site.register(Identity)
admin.site.register(Team)
admin.site.register(Alignment)