<template>
  <div class="app" id="app">
    <header-block></header-block>
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
        const loader = document.getElementById('loader')


        window.addEventListener('load', function() {
          loader.style.opacity = 0;
          setTimeout(function () {
            document.body.removeChild(loader)
          }, 1000)
        });

      },
    },
    mounted(){
      this.loaderOk()
    }
  }
</script>
