<template>
    <div class="basket">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Корзина</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item header__mini_item-active">Корзина</div>
                </div>
            </div>
        </div>
        <div class="basket__header">
            <div class="basket_items">
                <div class="basket__item basket__item-active">
                    <img src="/static/img/basket1.png" alt="cover">
                </div>
                <div class="basket__item">
                    <img src="/static/img/basket2.png" alt="cover">
                </div>
                <div class="basket__item">
                    <img src="/static/img/basket3.png" alt="cover">
                </div>
            </div>
        </div>
        <div class="basket__wrapper">
            <div class="basket__error">
                <div class="basket__error-text">Ваша корзина пуста :(</div>
                <button class="basket__button">Вернуться в меню</button>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    data(){
      return{

      }
    }
  }
</script>