<template>
  <div class="header">
    <div class="header__top">
      <div class="header__phone">
        <a class="header__phone-number" href="tel:+7(495)589-36-93">+7 (495) 589-36-93</a>
        <a class="header__phone-number" href="tel:+7(903)724-03-10">+7 (903) 724-03-10</a>
        <a class="header__phone-number" href="tel:+7(495)724-03-10">+7 (495) 724-03-10</a>
        <div class="header__phone-text">пн-сб: с 9:00 до 21:00 </br> вс: с 10:00 до 21:00</div>
      </div>
      <div class="header__title">
        <router-link tag="h1"  :to="{ name: 'index' }">Всё о пирогах</router-link>
          <div class="header__items">
            <router-link
                    :to="{ name: 'index' }"
                    class="header__item">Главная</router-link>
            <router-link
                    :class="{ 'router-link-exact-active': $route.name === 'menu' }"
                    :to="{ name: 'menu', params: {id: 'all'} }" class="header__item">Меню</router-link>
            <router-link :to="{ name: 'about' }" class="header__item">О нас</router-link>
            <router-link :to="{ name: 'discount' }" class="header__item">Скидки</router-link>
            <router-link :to="{ name: 'shipping' }" class="header__item">Доставка</router-link>
            <!--<router-link :to="{ name: 'comment' }" class="header__item">Отзывы</router-link>-->
            <router-link :to="{ name: 'contacts' }" class="header__item">Контакты</router-link>
          </div>
      </div>
        <basket-header></basket-header>
    </div>
  </div>
</template>

<script>
  import basketHeader from './HeaderBasket.vue'

  export default {
    name: 'header',
    data () {
      return {
      }
    },
    components:{
      basketHeader
    }
  }
</script>


