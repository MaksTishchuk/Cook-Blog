from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    """Регистрируем модель обратной связи в административной панели"""

    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name',)


class ImageAboutInLIne(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Регистрируем модель страницы о нас"""

    inlines = (ImageAboutInLIne, )


admin.site.register(ContactLink)
admin.site.register(Social)
