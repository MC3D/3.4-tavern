from django.contrib import admin
from .models import Location, Lunch


class LocationInline(admin.TabularInline):
    model = Location
    extra = 3


class LunchAdmin(admin.ModelAdmin):
    inlines = [LocationInline]


admin.site.register(Location)
admin.site.register(Lunch, LunchAdmin)
