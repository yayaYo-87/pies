import nested_admin
from django.contrib import admin
from django.utils.safestring import mark_safe

from app.mainpage.models import ExampleImage, MainPage, GoodsPopular, GoodsRapid, MainAboutUs, DiscountSlider, \
    DiscountSliderGoods


class GoodsPopularInline(admin.TabularInline):
    model = GoodsPopular
    fields = ['goods', 'sort_index']
    extra = 1
    max_num = 6
    suit_classes = 'suit-tab suit-tab-popular'


class GoodsRapidInline(admin.TabularInline):
    model = GoodsRapid
    fields = ['goods', 'sort_index']
    extra = 1
    suit_classes = 'suit-tab suit-tab-popular'


class MainAboutUsInline(admin.StackedInline):
    model = MainAboutUs
    fields = ['text_item', 'image', 'image_img', 'sort_index']
    extra = 1
    suit_classes = 'suit-tab suit-tab-about'
    readonly_fields = ['image_img',]

    def image_img(self, obj):
        if obj.image:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография'
    image_img.allow_tags = True


class DiscountSliderGoodsInline(nested_admin.NestedTabularInline):
    model = DiscountSliderGoods
    fields = ['goods', 'sort_index']
    extra = 2
    max_num = 2


class DiscountSliderInline(nested_admin.NestedStackedInline):
    model = DiscountSlider
    fields = ['name', 'icon', 'image_img', 'icon_active', 'image_img_active', 'discount', 'sort_index']
    extra = 1
    max_num = 4
    suit_classes = 'suit-tab suit-tab-discount'
    readonly_fields = ['image_img', 'image_img_active']
    inlines = [DiscountSliderGoodsInline, ]

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


class ExampleImageInline(admin.StackedInline):
    model = ExampleImage
    fields = ['image', 'sorting', 'image_img',]
    readonly_fields = ['image_img']
    extra = 1
    suit_classes = 'suit-tab suit-tab-general'


@admin.register(MainPage)
class MainPageAdmin(nested_admin.NestedModelAdmin):
    model = MainPage
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                )
            }
        ),
    ]
    inlines = [ExampleImageInline, GoodsPopularInline, GoodsRapidInline, MainAboutUsInline, DiscountSliderInline]
    suit_form_tabs = (
        ('general', 'Основные'),
        ('discount', 'Слайдер скидки'),
        ('about', 'Слайдер "О нас"'),
        ('popular', 'Слайдер популярных и "Прямо сейчаас"'),
    )