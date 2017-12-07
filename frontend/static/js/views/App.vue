<template>
  <div class="app" id="app">
    <header-block></header-block>
    <!--<transition name="loader"  >-->
      <!--<div class="loader" v-if="loader" >-->
        <!--<h1 class="loader_h">Пирог в процессе...</h1>-->
        <!--<div id="cooking">-->
          <!--<div class="bubble"></div>-->
          <!--<div class="bubble"></div>-->
          <!--<div class="bubble"></div>-->
          <!--<div class="bubble"></div>-->
          <!--<div class="bubble"></div>-->
          <!--<div id="area">-->
            <!--<div id="sides">-->
              <!--<div id="pan"></div>-->
              <!--<div id="handle"></div>-->
            <!--</div>-->
            <!--<div id="pancake">-->
              <!--<div id="pastry"></div>-->
            <!--</div>-->
          <!--</div>-->
        <!--</div>-->
      <!--</div>-->
    <!--</transition>-->
    <transition name="router" mode="out-in" >
      <router-view/>
    </transition>
    <footer-block></footer-block>
  </div>
</template>

<script>
  import headerBlock from '../components/Header.vue'
  import footerBlock from '../components/Footer.vue'

  export default {
    name: 'app',
    data(){
      return{
        loader: true
      }
    },
    components: {
      headerBlock,
      footerBlock
    },
    computed: {
      order(){
        return this.$route.name === 'order'
      }
    },
    methods:{
      loaderOk(){
        this.loader = false
      }
    },
    mounted(){
//      this.loaderOk()
    }
  }
</script>
