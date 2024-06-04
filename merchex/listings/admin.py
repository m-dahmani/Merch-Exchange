from django.contrib import admin
from .models import Band, Listing


# Register your models here.
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'sold', 'type', 'band')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)

