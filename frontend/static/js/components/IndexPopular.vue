<template>
    <div class="index__popular">
        <div class="index__popular_title">
            <span class="index__popular_title-text">Самое популярное</span>
        </div>
        <div class="index__popular_wrapper">
            <div class="index__popular_items">
                <index-popular-item
                        v-for="(item, index) in result"
                        :key="index"
                        :item="item.goods"
                ></index-popular-item>
            </div>

        </div>
        <router-link :to="{ name: 'menu', params: {id: 'all'} }"
                     tag="button"
                     class="popular_button">Перейти в каталог</router-link>
    </div>
</template>

<script>
  import axios from 'axios'
  import indexPopularItem from '../components/IndexPopularItem.vue'

  export default {
    props: ['result'],
    name: 'indexPopular',
    data() {
      return{

      }
    },
    components:{
      indexPopularItem
    },
    methods:{
    }
  }
</script>