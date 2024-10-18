from django.contrib import admin
from core.models import video, Tag

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('published_at','num_likes', 'num_views', 'author')
    list_display = ('title', 'is_published', 'published_at', 'num_likes', 'num_views', 'author')
    search_fields = ('title', 'description', 'tags__name')
    list_filter = ('is_published', 'tags')
    date_hierarchy = 'published_at'

    #salva o video definindo o usuário logado como autor
    def save_model(self,request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(video, VideoAdmin)
admin.site.register(Tag)
