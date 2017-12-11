<template>
    <div class="index__popular">
        <div class="index__popular_title">
            <span class="index__popular_title-text">Самое популярное</span>
        </div>
        <div class="index__popular_wrapper">
            <div class="index__popular_items">

                <div class="index__popular_item"
                     v-for="item in result">
                    <div class="popular_img">
                        <img :src="item.goods.cover" alt="cover" class="index__popular_img-cover">
                        <div class="popular_img-wrapper">
                            <router-link tag="div" :to="{ name: 'item', params: { id: 'all', item: item.goods.id } }"
                                         class="popular_img-top">Быстрый просмотр
                                <span>
                                    <img src="/static/img/lypa.png" alt="cover">
                                </span>
                            </router-link>
                            <div class="popular_img-bottom" @click="postProductFair(item.goods.id)">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                        </div>
                    </div>
                    <div class="popular_item-text">
                        <div class="popular_item-title">{{ item.goods.name }}</div>
                        <div class="popular_item-desc">{{ item.goods.shot_description }}</div>
                    </div>
                </div>
            </div>

        </div>
        <router-link :to="{ name: 'menu', params: {id: 'all'} }"
                     tag="button"
                     class="popular_button">Перейти в каталог</router-link>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    props: ['result'],
    name: 'indexPopular',
    data() {
      return{

      }
    },
    methods:{
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

    }
  }
</script>