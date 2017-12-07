<template>
    <div class="index">
        <div class="index__wrapper" v-if="result.length !== 0">
            <index-slider
                    v-if="result.discount_mains.length !== 0"
                    :result="result.discount_mains"
            ></index-slider>
            <index-menu></index-menu>
            <index-popular
                    v-if="result.popular_goods.length !== 0"
                    :result="result.popular_goods"
            ></index-popular>
            <index-about
                    v-if="result.main_about.length !== 0"
                    :result="result.main_about"
            ></index-about>
            <index-order
                    v-if="result.rapid_goods.length !== 0"
                    :result="result.rapid_goods"
            ></index-order>
            <index-image
                    v-if="result.main_images.length !== 0"
                    :result="result.main_images"
            ></index-image>
            <index-end></index-end>
        </div>
    </div>
</template>

<script>
  import indexSlider from '../components/IndexSlider.vue'
  import indexMenu   from '../components/IndexMenu.vue'
  import indexPopular from '../components/IndexPopular.vue'
  import indexAbout from '../components/IndexAbout.vue'
  import indexOrder from '../components/IndexOrdering.vue'
  import indexImage from '../components/IndexImage.vue'
  import indexEnd from '../components/IndexEnd.vue'
  import axios from 'axios'

  export default {
    name: 'index',
    data() {
      return {
        result: []
      }
    },
    components: {
      indexMenu,
      indexPopular,
      indexAbout,
      indexSlider,
      indexOrder,
      indexImage,
      indexEnd
    },
    methods:{
      get(){
        const self = this;
        axios.get('/api/main_page/')
          .then(function (response) {
            self.result =  response.data[0]
          })
      }
    },
    created(){
      this.get()
    }
  }
</script>