from django.contrib import admin
from todolist.models import Todo


class ChoiceInline(admin.TabularInline):
    model = Todo
    extra = 3


class TodoAdmin(admin.ModelAdmin):
    fields = ['todotype', 'priority', 'content', 'is_done', 'owner']
    list_display = fields
    search_fields = ['content']

admin.site.register(Todo, TodoAdmin)
# Register your models here.
