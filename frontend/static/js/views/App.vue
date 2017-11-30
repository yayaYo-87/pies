<template>
  <div class="app" id="app">
    <router-view/>
    qweqwe
  </div>
</template>

<script>

  export default {
    name: 'app',
    components: {

    },
    computed: {
      order(){
        return this.$route.name === 'order'
      }
    }
  }
</script>
