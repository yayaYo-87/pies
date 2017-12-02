<template>
  <div class="footer">


  </div>
</template>

<script>
  export default {
    name: 'footer',
    data() {
      return {
      }
    },
    computed: {
      display() {
        return this.$route.name === 'order'
      }
    }
  }
</script>
