from django.contrib import admin

from .models import Post


# Декоратор @admin.register() выполняет те же действия, что и функция
# admin.site.register(): регистрирует декорируемый класс
# наследник ModelAdmin.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # slug генерируется автоматически из поля title с
    # помощью атрибута prepopulated_fields
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)  # поле выбора пользователя
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
