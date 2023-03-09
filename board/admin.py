from django.contrib import admin

from .models import Bb
from .models import Rubric
admin.site.register(Rubric)
class Bbadmin(admin.ModelAdmin):
    list_display = ('title','contentt','price', 'published', 'rubric')
    list_display_links = ('title','contentt')
    search_fields = ('title', 'contentt')
admin.site.register(Bb, Bbadmin)
