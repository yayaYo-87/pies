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
                     :class="{'basket__item-active' : validation === 2 || validation === 3}"
                >
                    <img src="/static/img/basket2.png" alt="cover">
                </div>
                <div class="basket__item"
                     :class="{'basket__item-active' : validation === 3}"
                >
                    <img src="/static/img/basket3.png" alt="cover">
                </div>
            </div>
        </div>
        <basket-cart></basket-cart>
        <basket-info></basket-info>
        <basket-end></basket-end>
    </div>
</template>

<script>

  import basketCart from '../components/BasketCart.vue'
  import basketInfo from '../components/BasketInfo.vue'
  import basketEnd from '../components/BasketEnd.vue'

  export default {
    metaInfo () {
      return {
        title: 'Корзина',
        titleTemplate: '%s | Осетинские пироги',
        meta: [
          {
            name: 'description' ,
            content: 'Пекарня «Всё о пирогах» — это специализированная компания, выпекающая осетинские пироги по традиционной и оригинальной рецептуре, в полном соответствии с современными технологиями и установленными стандартами.'
          },
          {
            name: 'keywords',
            content: 'Пекарня «Всё о пирогах»  выпекающая осетинские пироги по традиционной и оригинальной рецептуре'
          },
        ]
      }
    },
    data(){
      return{

      }
    },
    components:{
      basketCart,
      basketInfo,
      basketEnd
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
    },
    created(){
      this.$store.commit('results', { type: 'validation', items: 1})
    },
    mounted(){
      this.$store.dispatch('loader', { value: false })
    }

  }
</script>