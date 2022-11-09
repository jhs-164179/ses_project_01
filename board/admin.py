from django.contrib import admin

from .models import Board, Reply


class BoardAdmin(admin.ModelAdmin):
    search_fields =  ['title']

admin.site.register([Board, Reply])
