<template>
    <div class="menu">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Меню</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item header__mini_item-active">Меню</div>
                </div>
            </div>
        </div>

        <div class="menu__wrapper">
            <div class="menu__left">
                <div class="menu__filter">
                    <div class="menu__filter_icon">
                        <img class="menu__filter_icon-left" src="/static/img/filter.png" alt="cover">
                        <img class="menu__filter_icon-right" src="/static/img/filter1.png" alt="cover">
                    </div>
                    <div class="menu__filter_count">
                        Показаны 1-9 из 12 товаров
                    </div>
                    <div class="menu__filter_select">
                        <select name="sel" id="sel">
                            <option >По умолчанию</option>
                        </select>
                    </div>
                </div>


                <div class="menu__list">
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
                                <div class="menu__list_hover-top">Быстрый просмотр</div>
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
                                <div class="menu__list_hover-top">Быстрый просмотр</div>
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
                                <div class="menu__list_hover-top">Быстрый просмотр</div>
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
                                <div class="menu__list_hover-top">Быстрый просмотр</div>
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
                                <div class="menu__list_hover-top">Быстрый просмотр</div>
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

                <div class="menu__pagination">
                    <div class="menu__pagination_item">&#171;</div>
                    <div class="menu__pagination_item menu__pagination_item-active">1</div>
                    <div class="menu__pagination_item">2</div>
                    <div class="menu__pagination_item">&#187;</div>
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
    name: 'menu',
    data(){
      return{

      }
    }
  }
</script>