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
                            <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
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
  export default {
    props: ['result'],
    name: 'indexPopular',
    data() {
      return{

      }
    }
  }
</script>