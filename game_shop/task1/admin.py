from django.contrib import admin
from .models import Buyer, Game, News

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(News)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 30
    readonly_fields = ('date',)