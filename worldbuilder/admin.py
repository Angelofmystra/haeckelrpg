from django.contrib import admin
from worldbuilder.models import Area, Room, Mob, Character, Equipment, Weapon, Shield, Armor, House, Noble


class WorldAdmin(admin.ModelAdmin):
    model = Area
    list_display = ["name", "desc"]
    search_fields = ["name"]

admin.site.register(Area, WorldAdmin)
admin.site.register(Room)
admin.site.register(Mob)
admin.site.register(Character)
admin.site.register(Equipment)
admin.site.register(Weapon)
admin.site.register(Shield)
admin.site.register(Armor)
admin.site.register(House)
admin.site.register(Noble)
# Register your models here.
