<template>
    <div class="menu__list_item">
        <div class="menu__list_cover">
            <img :src="result.cover" alt="cover">
            <div class="menu__list_hover">
                <router-link :to="{ name:'item', params: { item: id } }" class="menu__list_hover-top">Быстрый просмотр</router-link>
                <div class="menu__list_hover-bottom" @click="postProductFair(id)">Быстрый заказ</div>
            </div>
        </div>
        <div class="menu__list_desc">
            <div class="menu__list_title">{{ result.name }}</div>
        </div>
        <div class="menu__list_bottom">
            <div class="menu__list_bottom-left">
                <div class="menu_input" v-click-outside="popupClose">
                    <div class="menu_input-active"
                         :class="{ 'menu_input-active-true': popup === true }"
                         @click="popupActive">{{ weightActive }}</div>
                    <div class="menu_input-popup"
                         v-show="popup">
                        <div class="menu_input-popup_item"
                             :class="{ 'menu_input-popup_item-active' : index === weightActive}"
                             v-for="(weight, index) in result.goods_weight"
                             @click="pushPrice(weight)"
                        >{{ weight.weight }}</div>
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
                <button @click="postProduct(result.id)" class="menu__list_button">Заказать</button>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['id'],
    data(){
      return{
        result: [],
        popup: false,
        count: 1,
        weightActive: 0,
        weightId: 0,
        price: 0,
      }
    },
    methods:{
      get(){
        const self = this;

        axios.get('/api/goods/' + self.id + '/')
          .then(function (response) {
            self.result =  response.data;
            if(self.result.goods_weight[0].discount_price === 0) {
              self.price = self.result.goods_weight[0].price;
              self.weightActive = self.result.goods_weight[0].weight;
              self.weightId = self.result.goods_weight[0].id
            } else {
              self.price = self.result.goods_weight[0].discount_price;
              self.weightActive = self.result.goods_weight[0].weight;
              self.weightId = self.result.goods_weight[0].id
            }
          })
      },
      animatePopup(){
        const newDiv = document.createElement('div');
        newDiv.classList.add('popup')
        newDiv.innerHTML = 'Товар добавлен в корзину';

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      },
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
    },
    created() {
      this.get()
    },
    mounted(){

    }

  }
</script>