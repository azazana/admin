from django.contrib import admin
from . import models

class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

admin.site.register(models.Custemer)
admin.site.register(models.Movie,MovieAdmin)


