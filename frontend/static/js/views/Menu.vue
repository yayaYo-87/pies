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
    name: 'menu',
    data(){
      return{

      }
    }
  }
</script>