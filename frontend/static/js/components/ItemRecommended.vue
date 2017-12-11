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
                <div class="menu_input">
                    <div class="menu_input-active">1000Г</div>
                    <div class="menu_input-popup">
                        <div class="menu_input-popup_item">1000Г</div>
                        <div class="menu_input-popup_item">2000Г</div>
                        <div class="menu_input-popup_item">3000Г</div>
                    </div>
                </div>
                <div class="menu_count">
                    <button class="menu_count-minus">-</button>
                    <div class="menu_count-count">1</div>
                    <button class="menu_count-plus">+</button>
                </div>
            </div>
            <div class="menu__list_bottom-right">
                <div class="menu__list_price">{{ result.price }} руб.</div>
                <button class="menu__list_button">Заказать</button>
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
      }
    },
    methods:{
      get(){
        const self = this;

        axios.get('/api/goods/' + self.id + '/')
          .then(function (response) {
            self.result =  response.data
          })
      },
      postProductFair(id){
        const self = this;
        axios.post('/api/order_goods/', {
          "goods": id,
          "count": 1,
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
      animatePopup(){
        const newDiv = document.createElement('div');
        newDiv.classList.add('popup')
        newDiv.innerHTML = 'Товар добавлен в корзину';

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      },
    },
    created() {
      this.get()
    }
  }
</script>