from django.contrib import admin
from .models import MagazineInfo, MagazineContent

# Customize the admin interface for MagazineInfo
class MagazineInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'category')  
    search_fields = ('title', 'category')  # Allows searching in Admin Panel
    list_filter = ('category',)

# Customize the admin interface for MagazineContent
class MagazineContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'magazine', 'content', 'vector_representation')
    search_fields = ('magazine__title', 'content')  # Allows searching by magazine title and content in Admin panel
    list_filter = ('magazine',)

# Register the models with their respective admin classes
admin.site.register(MagazineInfo, MagazineInfoAdmin)
admin.site.register(MagazineContent, MagazineContentAdmin)
