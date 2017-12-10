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
                <div class="basket__item basket__item-active" @click="next(1)">
                    <img src="/static/img/basket1.png" alt="cover">
                </div>
                <div class="basket__item"
                     :class="{'basket__item-active' : validation === 2}"
                >
                    <img src="/static/img/basket2.png" alt="cover">
                </div>
                <div class="basket__item">
                    <img src="/static/img/basket3.png" alt="cover">
                </div>
            </div>
        </div>
        <basket-cart ></basket-cart>
        <basket-info></basket-info>
    </div>
</template>

<script>

  import basketCart from '../components/BasketCart.vue'
  import basketInfo from '../components/BasketInfo.vue'

  export default {
    data(){
      return{

      }
    },
    components:{
      basketCart,
      basketInfo
    },
    methods:{
      next(value){
        this.$store.commit('results', { type: 'validation', items: value})
      }
    },
    computed: {
      validation() {
        return this.$store.state.basket.validation
      }

    }
  }
</script>