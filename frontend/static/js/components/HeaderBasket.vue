<template>
    <div class="header__basket" @mouseenter="showPopup()" @mouseleave="showPopupFalse()">
        <router-link :to="{ name: 'basket' }" tag="div" class="header__basket__img">
            <div class="header__basket__img-count">2</div>
        </router-link>
        <div class="header__basket-price">1212 <span class="rubl" > &#8399;</span></div>

        <div class="header__basket_wrapper">
            <transition name="popupBasket">
                <div class="basket-header__popup" v-show="popup">
                    <div class="basket-header__popup_false"
                    >
                        Для оформления заказа выберите продукт
                    </div>
                    <!--<div class="basket-header__wrapper"-->
                         <!--v-show="this.$store.state.basketPopup.results.results &&-->
                         <!--this.$store.state.basketPopup.results.results[0].cart_crocs.length !== 0 ||-->
                         <!--this.$store.state.basketPopup.results.results &&-->
                         <!--this.$store.state.basketPopup.results.results[0].cart_jibbitz.length !== 0">-->
                        <!--<div class="basket-header__items" >-->
                            <!--<div class="basket-header__item" v-for="item in items.cart_crocs">-->
                                <!--<div class="basket-header__item-close" @click="switchItem(item.id, 'crocs', 'deactivate')">+</div>-->
                                <!--<div class="basket-header__item-img" @click="routerLink(item.crocs.category, item.crocs.type.id, item.crocs.id )">-->
                                    <!--<img :src='item.color.cover' alt="crocs">-->
                                <!--</div>-->
                                <!--<div class="basket-header__item_info">-->
                                    <!--<div class="basket-header__item_info-name">{{ item.crocs.name }}</div>-->
                                    <!--<div class="basket-header__item_info-call">-->
                                        <!--<div class="basket-header__item_info-call_name">{{ item.color.name }}</div>-->
                                        <!--<div class="basket-header__item_info-call_name">{{ item.size.ru_size }}</div>-->
                                        <!--<div class="basket-header__item_info-call_name">{{ item.count }}</div>-->
                                    <!--</div>-->
                                <!--</div>-->
                                <!--<div class="basket-header__item_price">-->
                                    <!--<div class="basket-header__item_price-discount" v-show="item.color.discount_price">{{ item.color.discount_price }} <span class="ruble">₽</span></div>-->
                                    <!--<div class="basket-header__item_price-current" :class="{'price_active' : item.color.discount_price}" >{{ item.crocs.price }} <span class="ruble">₽</span></div>-->
                                <!--</div>-->

                                <!--<div class="basket-header__item-active" v-if="!item.active">-->
                                    <!--<button class="button button-green" @click="switchItem(item.id, 'crocs', 'activate')">-->
                                        <!--<span>-->
                                            <!--Вернуть обратно-->
                                        <!--</span>-->
                                    <!--</button>-->
                                <!--</div>-->
                            <!--</div>-->
                        <!--</div>-->
                        <!--<div class="basket-header__total">-->
                            <!--<div class="basket-header__total-name">Итого:</div>-->
                            <!--<div class="basket-header__total-price">{{ items.price }} <span class="ruble">₽</span></div>-->
                        <!--</div>-->
                        <!--<button  class="button button-green"-->
                                 <!--@click="orderLink()">-->
                            <!--<span>-->
                                <!--Оформить заказ-->
                            <!--</span>-->
                        <!--</button>-->
                    <!--</div>-->
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
        popup: true
      }
    },
    computed: {
      items() {
        return this.$store.state.basketPopup.results.results && this.$store.state.basketPopup.results.results.length !== 0  ? this.$store.state.basketPopup.results.results[0] : ''
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
      switchItem(id, order, inc){
        axios.post('/api/order_' + order + '/' + id + '/'+ inc +'/')
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