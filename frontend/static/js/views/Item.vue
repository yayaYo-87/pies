<template>
    <div class="item">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Меню</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item ">Меню ></div>
                    <div class="header__mini_item header__mini_item-active">LOREM IPSUM PIE</div>
                </div>
            </div>
        </div>
        <div class="menu__wrapper">
            <div class="menu__left">
                <div class="item__wrapper">
                    <div class="item__cover">
                        <img src="/static/img/list123.png" alt="cover">
                    </div>
                    <div class="item__text">
                        <div class="item__title">LOREM IPSUM PIE</div>
                        <div class="item__price">600 руб.</div>
                        <div class="item__list">
                            <ol class="item__list-ol">
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                                <li class="item__list-li">Первый пункт</li>
                            </ol>
                        </div>
                        <div class="item__button">
                            <div class="item__button_left">
                                <button class="item__button-sum">-</button>
                                <div class="item__button-text">1</div>
                                <button class="item__button-sum">+</button>
                            </div>
                            <div class="item__button_right">
                                <button class="item-button">Заказать</button>
                            </div>
                        </div>
                        <div class="item__teg">
                            <div class="item__teg-text"><span>Категория:</span> Пироги</div>
                            <div class="item__teg-text"><span>Теги:</span> <a href="#">Грибы</a>, <a href="#">Грибы</a></div>
                        </div>
                    </div>
                </div>
                <div class="item__desc">
                    <div class="item__desc-title">ОПИСАНИЕ</div>
                    <div class="item__desc-text">Что может быть лучше, чем аппетитный кусочек теста с сытной начинкой из нежной говядины и свежей ветчины под тонкой корочкой ароматного сыра? При одном взгляде на «Аппетитную» пиццу вам непременно захочется полакомиться ею, даже если вы совсем недавно перекусили.

                        Помимо двух видов мясапицца «Аппетитная», разумеется, содержит традиционную для этого блюда подборку овощей. Маринованные огурчики, желтые, красные и зеленые пеппероне, перемежающиеся ломтиками помидоров двух сортов сделали вкус итальянского блюда по-настоящему фантастическим.</div>
                </div>
                <div class="item__rec">
                    <div class="item__rec-title">Популярные товары
                        <div class="item__rec-prev"></div>
                        <div class="item__rec-next"></div>
                    </div>
                    <div class="item__rec_list">
                        <div class="menu__list_item">
                            <div class="menu__list_cover">
                                <img src="/static/img/list123.png" alt="cover">
                                <div class="menu__list_hover">
                                    <router-link :to="{ name:'item' }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                                    <div class="menu__list_hover-bottom">Быстрый заказ</div>
                                </div>
                            </div>
                            <div class="menu__list_desc">
                                <div class="menu__list_title">LOREM IPSUM PIE</div>
                            </div>
                            <div class="menu__list_price">600 руб.</div>
                            <button class="menu__list_button">Заказать</button>
                        </div>
                        <div class="menu__list_item">
                            <div class="menu__list_cover">
                                <img src="/static/img/list123.png" alt="cover">
                                <div class="menu__list_hover">
                                    <router-link :to="{ name:'item' }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                                    <div class="menu__list_hover-bottom">Быстрый заказ</div>
                                </div>
                            </div>
                            <div class="menu__list_desc">
                                <div class="menu__list_title">LOREM IPSUM PIE</div>
                            </div>
                            <div class="menu__list_price">600 руб.</div>
                            <button class="menu__list_button">Заказать</button>
                        </div>
                        <div class="menu__list_item">
                            <div class="menu__list_cover">
                                <img src="/static/img/list123.png" alt="cover">
                                <div class="menu__list_hover">
                                    <router-link :to="{ name:'item' }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                                    <div class="menu__list_hover-bottom">Быстрый заказ</div>
                                </div>
                            </div>
                            <div class="menu__list_desc">
                                <div class="menu__list_title">LOREM IPSUM PIE</div>
                            </div>
                            <div class="menu__list_price">600 руб.</div>
                            <button class="menu__list_button">Заказать</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="menu__right">
                <div class="menu__right-title">Поиск</div>
                <div class="menu__right_search">
                    <input type="text" placeholder="Введите название...">
                </div>
                <div class="menu__right-title">Категории</div>
                <div class="menu__right_list">
                    <div class="menu__right_item menu__right_item-active">Осетинские пироги</div>
                    <div class="menu__right_item">Рыбные пироги</div>
                    <div class="menu__right_item">Пицца</div>
                    <div class="menu__right_item">Постное меню</div>
                    <div class="menu__right_item">Вторые блюда</div>
                    <div class="menu__right_item">Домашняя выпечка</div>
                    <div class="menu__right_item">Напитки</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    name:'item',
    data() {
      return{

      }
    }
  }
</script>