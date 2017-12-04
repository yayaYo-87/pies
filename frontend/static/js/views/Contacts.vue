<template>
    <div class="contacts">
        <div class="header__mini">
            <div class="header__mini_wrapper">
                <div class="header__mini_title">Контакты</div>
                <div class="header__mini_list">
                    <router-link :to="{ name: 'index' }" class="header__mini_item">Главная ></router-link>
                    <div class="header__mini_item header__mini_item-active">Контакты</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    data(){
      return{

      }
    }
  }
</script>