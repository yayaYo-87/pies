<template>
    <div class="index__image">
        <div class="index__image_title">
            <span class="index__image_title-text">ПРИМЕРЫ НАШИХ БЛЮД</span>
        </div>
        <div class="index__image_wrapper">
            <div class="index__image_left">
                <div class="index__image_left-e1">Пришел,</div>
                <div class="index__image_left-e2">увидел,</div>
                <div class="index__image_left-e3">заказал!</div>
            </div>
            <div class="index__image_right">
                <div class="index__image_right-e1">У нас только </div>
                <div class="index__image_right-e2">самые лучшие</div>
                <div class="index__image_right-e3">ингредиенты</div>
            </div>

            <div class="index__image_item" v-for="item in result">
                <img :src="item.image" alt="cover">
            </div>


        </div>
        <div class="index__image_title index__image_title-bottom">
            <span class="index__image_title-text">ФАКТЫ О НАС</span>
            <div class="index__image_title-desc">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation</div>
            <div class="index__image_list">
                <div class="index__image_list-item">
                    <div class="index__image_list-img">
                        <img src="/static/img/img1.png" alt="">
                        <div class="index__image_list-count">167</div>
                    </div>
                    <div class="index__image_list-text">...разновидностей блюд в нашем меню</div>
                </div>
                <div class="index__image_list-item">
                    <div class="index__image_list-img">
                        <img src="/static/img/img2.png" alt="">
                        <div class="index__image_list-count">29784</div>
                    </div>
                    <div class="index__image_list-text">...человек уже выбрали нас</div>
                </div>

                <div class="index__image_list-item">
                    <div class="index__image_list-img">
                        <img src="/static/img/img3.png" alt="">
                        <div class="index__image_list-count">340</div>
                    </div>
                    <div class="index__image_list-text">...блюд было продано за прошлую неделю</div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
  export default {
    props: ['result'],
    data() {
      return {

      }
    }
  }
</script>