<template>
    <div class="menu__right">
        <div class="menu__right-title">Категории</div>
        <div class="menu__right_list">
            <router-link
                    tag="div"
                    :to="{ name: 'menu', params: { id: item.slug } }"
                    class="menu__right_item"
                    v-for="(item, index) in result"
                    :key="index"
                    :class="{ 'menu__right_item-active' : $route.params.id === item.slug }"
            >{{ item.name }}</router-link>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return{
        result: []
      }
    },
    methods: {
      get(){
        const self = this
        axios.get('/api/category/')
          .then(function (response) {
            self.result = response.data.results
          })
      }
    },
    created(){
      this.get()
    }
  }
</script>