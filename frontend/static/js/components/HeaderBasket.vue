<template>

    <div class="header__basket" @mouseenter="showPopup()" @mouseleave="showPopupFalse()" >
        <router-link :to="{ name: 'basket' }" tag="div" class="header__basket__img">
            <div class="header__basket__img-count"
                 v-if="basket.results && basket.results.length !== 0"
            >{{ basket.results.total_count }}</div>
        </router-link>
        <div v-if="basket.results && basket.results.length !== 0"
             class="header__basket-price">{{ basket.results.price }} <span class="rubl" > &#8399;</span></div>

        <div class="header__basket_wrapper">
            <transition name="popupBasket">
                <div class="basket-header__popup" v-show="popup">
                    <div class="basket-header__popup_false"
                         v-if="basket.results.cart_goods && basket.results.cart_goods.length === 0"
                    >
                        Для оформления заказа выберите продукт
                    </div>
                    <div class="basket-header__wrapper" v-if="basket.results && basket.results.length !== 0">

                        <div class="basket-header__item" v-for="cart in  basket.results.cart_goods">
                            <div class="basket-header__item-close" @click="switchItem(cart.id, 'deactivate')">+</div>
                            <div class="basket-header__item-img">
                                <img :src="cart.goods.cover" alt="cover">
                            </div>
                            <div class="basket-header__item-desc">{{cart.goods.name}}</div>
                            <div class="basket-header__item-price">{{cart.goods.price}} <span class="rubl" > &#8399;</span></div>
                            <div class="basket-header__item-active" v-if="!cart.active">
                                <button class="button button-green" @click="switchItem(cart.id , 'activate')">
                                        <span>
                                            Вернуть обратно
                                        </span>
                                </button>
                            </div>
                        </div>

                    </div>
                    <button class="header__basket_item-button">Оформить заказ</button>
                </div>
            </transition>
        </div>


    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        popup: false
      }
    },
    computed: {
      basket() {
        return this.$store.state.basket
      }
    },
    methods: {
      showPopup(){
        this.popup = true
      },
      showPopupFalse(){
        this.popup = false
      },
      get() {
        this.$store.dispatch('results')
      },
      switchItem(id, inc){
        axios.post('/api/order_goods/' + id + '/'+ inc +'/')
          .then((response) => {
            if (response.status === 200) {
              let self = this
              self.$store.dispatch('results')
            }
          })
      }

    },
    created(){
      this.get()
    }

  }
</script>