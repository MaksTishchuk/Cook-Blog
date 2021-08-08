from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInLIne(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'category', 'create_at']
    inlines = [RecipeInLIne]
    save_as = True
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'post', 'prep_time', 'cook_time']


# MPTTModelAdmin позволяет сделать сдвиг вправо в админке для подкатегорий для наглядности
admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
