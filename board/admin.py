from django.contrib import admin

from .models import Bb
class Bbadmin(admin.ModelAdmin):
    list_display = ('title','contentt','price', 'published')
    list_display_links = ('title','contentt')
    search_fields = ('title', 'contentt')
admin.site.register(Bb, Bbadmin)
