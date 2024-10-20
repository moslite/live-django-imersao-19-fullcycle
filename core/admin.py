from django.contrib import admin
from django.forms.models import ModelForm
from django.http.request import HttpRequest
from core.models import Video, Tag

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('num_likes', 'num_views', 'published_at', 'author')
    list_display = ('title', 'is_published', 'published_at', 'num_likes', 'num_views')
    # lookup
    search_fields = ('title', 'description', 'tags__name')
    list_filter = ('is_published', 'tags')
    date_hierarchy = 'published_at'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)