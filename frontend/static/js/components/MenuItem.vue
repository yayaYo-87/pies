<template>
    <div class="menu__list_item" >
        <div class="menu__list_cover">
            <img :src="itemProduct.cover" alt="cover">
            <div class="menu__list_hover">
                <router-link :to="{ name:'item', params: { id: $route.params.id, item: itemProduct.id } }"
                             class="menu__list_hover-top">Быстрый просмотр</router-link>
                <div @click="postProductFair(itemProduct.id)" class="menu__list_hover-bottom">Быстрый заказ</div>
            </div>
        </div>
        <div class="menu__list_desc">
            <div class="menu__list_title">{{ itemProduct.name }}</div>
        </div>
        <div class="menu__list_bottom">
            <div class="menu__list_bottom-left">
                <div class="menu_input" v-click-outside="popupClose">
                    <div class="menu_input-active"
                         :class="{ 'menu_input-active-true': popup === true }"
                         @click="popupActive">{{ weightActive }}г.</div>
                    <div class="menu_input-popup"
                         v-show="popup">
                        <div class="menu_input-popup_item"
                             :class="{ 'menu_input-popup_item-active' : index === weightActive}"
                             v-for="(weight, index) in itemProduct.goods_weight"
                             @click="pushPrice(weight)"
                        >{{ weight.weight }}г.</div>
                    </div>
                </div>
                <div class="menu_count">
                    <button class="menu_count-minus"
                            :disabled="count <= 1"
                            @click="countMinus"
                    >-</button>
                    <div class="menu_count-count">{{ count }}</div>
                    <button class="menu_count-plus" @click="countPlus">+</button>
                </div>
            </div>
            <div class="menu__list_bottom-right">
                <div class="menu__list_price">{{ price }} руб.</div>
                <button @click="postProduct(itemProduct.id)" class="menu__list_button">Заказать</button>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['itemProduct'],
    data() {
      return {
        popup: false,
        count: 1,
        weightActive: 0,
        weightId: 0,
        price: 0,
      }
    },
    methods:{
      pushPrice(item){
        this.popup = false;
        if(item.discount_price === 0) {
          this.price = item.price
          this.weightActive = item.weight
          this.weightId = item.id
        } else {
          this.price = item.discount_price
          this.weightActive = item.weight
          this.weightId = item.id
        }
      },
      countPlus(){
        this.count++
      },
      countMinus(){
        this.count--
      },
      popupActive(){
        this.popup = !this.popup
      },
      popupClose(){
        this.popup = false
      },
      postProductFair(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": self.count,
          "weight": self.weightId,
        }).then(
          function (response) {
            self.$store.dispatch('results');
            self.animatePopup();
            self.$router.push({name: 'basket' })
          },
          function (error) {
          }
        )
      },
      postProduct(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": self.count,
          "weight": self.weightId,
        }).then(
          function (response) {
            self.$store.dispatch('results');
            self.animatePopup();
          },
          function (error) {
          }
        )
      },
      animatePopup(){
        const newDiv = document.createElement('div');
        newDiv.classList.add('popup')
        newDiv.innerHTML = 'Товар добавлен в корзину';

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      }
    },
    mounted(){
      if(this.itemProduct.goods_weight[0].discount_price === 0) {
        this.price = this.itemProduct.goods_weight[0].price
        this.weightActive = this.itemProduct.goods_weight[0].weight
        this.weightId = this.itemProduct.goods_weight[0].id
      } else {
        this.price = this.itemProduct.goods_weight[0].discount_price
        this.weightActive = this.itemProduct.goods_weight[0].weight
        this.weightId = this.itemProduct.goods_weight[0].id
      }
    }
  }
</script>