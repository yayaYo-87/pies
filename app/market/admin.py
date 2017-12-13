from django.contrib import admin
from django.utils.safestring import mark_safe

from app.market.models import Category, Tag, GoodsConsist, Goods, GoodsWeight


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['name', 'slug', 'sort_index', 'icon', 'image_img', 'icon_active', 'image_img_active']
    readonly_fields = ['image_img', 'image_img_active']

    def image_img(self, obj):
        if obj.icon:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.icon.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография иконки'
    image_img.allow_tags = True

    def image_img_active(self, obj):
        if obj.icon_active:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.icon_active.url))
        else:
            return '(Нет изображения)'

    image_img_active.short_description = 'Фотография активной иконки'
    image_img_active.allow_tags = True


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['name',]


class GoodsConsistInline(admin.TabularInline):
    model = GoodsConsist
    fields = ['text_item', 'sort_index']
    extra = 1
    suit_classes = 'suit-tab suit-tab-consist'


class GoodsWeightInline(admin.TabularInline):
    model = GoodsWeight
    fields = ['weight', 'price', 'discount_price', 'sort_index']
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


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
                    # 'price',
                    'title',
                    'description',
                    'shot_description',
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
    inlines = [GoodsConsistInline, GoodsWeightInline]
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
