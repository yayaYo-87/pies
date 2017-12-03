from django.contrib import admin
from django.utils.safestring import mark_safe

from app.market.models import Category, Tag, GoodsConsist, Goods


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['name', 'slug', 'sort_index']


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['name',]


class GoodsConsistInline(admin.TabularInline):
    model = GoodsConsist
    fields = ['text_item', 'sort_index']
    extra = 1
    suit_classes = 'suit-tab suit-tab-consist'


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    model = Goods
    # form = GoodsForm
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                    'articul',
                    'category',
                    'price',
                    'description',
                    'cover',
                    'image_img',
                    'tag',
                    'sort_index',
                    'popularity_index',
                    'is_active',
                    'is_main',
                )
            }
        ),
        (
            'Рекомендованные товары и состав',
            {
                'classes': ('suit-tab', 'suit-tab-consist',),
                'fields': (
                    'related_goods',
                )
            }
        ),
        (
            'Meta tags',
            {
                'classes': ('suit-tab', 'suit-tab-tags',),
                'fields': (
                    'meta_title',
                    'meta_description',
                    'meta_keywords',
                )
            }
        )
    ]
    filter_horizontal = ['related_goods', 'tag', 'category']
    inlines = [GoodsConsistInline, ]
    readonly_fields = ['image_img', ]

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True
    suit_form_tabs = (
        ('general', 'Основные'),
        ('consist', 'Рекомендованные товары и состав'),
        ('tags', 'Meta tags')
    )
    list_filter = ['category', 'is_active',]
    search_fields = ['name',]