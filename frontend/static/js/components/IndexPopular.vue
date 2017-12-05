<template>
    <div class="index__popular">
        <div class="index__popular_title">
            <span class="index__popular_title-text">Самое популярное</span>
        </div>
        <div class="index__popular_wrapper">
            <div class="index__popular_items">
                <div class="index__popular_item">
                    <div class="popular_img">
                        <img src="/static/img/popular211.png" alt="cover" class="index__popular_img-cover">
                        <div class="popular_img-wrapper">
                            <div class="popular_img-top">Быстрый просмотр <span><img src="/static/img/lypa.png" alt="cover"></span></div>
                            <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                        </div>
                    </div>
                    <div class="popular_item-text">
                        <div class="popular_item-title">LOREM IPSUM PIE</div>
                        <div class="popular_item-desc">dolor sit amet, consectetur adipiscing elit sed do eiusmod</div>
                    </div>
                </div><div class="index__popular_item">
                <div class="popular_img">
                    <img src="/static/img/popular211.png" alt="cover" class="index__popular_img-cover">
                    <div class="popular_img-wrapper">
                        <div class="popular_img-top">Быстрый просмотр <span><img src="/static/img/lypa.png" alt="cover"></span></div>
                        <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                    </div>
                </div>
                <div class="popular_item-text">
                    <div class="popular_item-title">LOREM IPSUM PIE</div>
                    <div class="popular_item-desc">dolor sit amet, consectetur adipiscing elit sed do eiusmod</div>
                </div>
            </div><div class="index__popular_item">
                <div class="popular_img">
                    <img src="/static/img/popular211.png" alt="cover" class="index__popular_img-cover">
                    <div class="popular_img-wrapper">
                        <div class="popular_img-top">Быстрый просмотр <span><img src="/static/img/lypa.png" alt="cover"></span></div>
                        <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                    </div>
                </div>
                <div class="popular_item-text">
                    <div class="popular_item-title">LOREM IPSUM PIE</div>
                    <div class="popular_item-desc">dolor sit amet, consectetur adipiscing elit sed do eiusmod</div>
                </div>
            </div><div class="index__popular_item">
                <div class="popular_img">
                    <img src="/static/img/popular211.png" alt="cover" class="index__popular_img-cover">
                    <div class="popular_img-wrapper">
                        <div class="popular_img-top">Быстрый просмотр <span><img src="/static/img/lypa.png" alt="cover"></span></div>
                        <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                    </div>
                </div>
                <div class="popular_item-text">
                    <div class="popular_item-title">LOREM IPSUM PIE</div>
                    <div class="popular_item-desc">dolor sit amet, consectetur adipiscing elit sed do eiusmod</div>
                </div>
            </div><div class="index__popular_item">
                <div class="popular_img">
                    <img src="/static/img/popular211.png" alt="cover" class="index__popular_img-cover">
                    <div class="popular_img-wrapper">
                        <div class="popular_img-top">Быстрый просмотр <span><img src="/static/img/lypa.png" alt="cover"></span></div>
                        <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                    </div>
                </div>
                <div class="popular_item-text">
                    <div class="popular_item-title">LOREM IPSUM PIE</div>
                    <div class="popular_item-desc">dolor sit amet, consectetur adipiscing elit sed do eiusmod</div>
                </div>
            </div><div class="index__popular_item">
                <div class="popular_img">
                    <img src="/static/img/popular211.png" alt="cover" class="index__popular_img-cover">
                    <div class="popular_img-wrapper">
                        <div class="popular_img-top">Быстрый просмотр <span><img src="/static/img/lypa.png" alt="cover"></span></div>
                        <div class="popular_img-bottom">Быстрый заказ <span><img src="/static/img/fire.png" alt="cover"></span></div>
                    </div>
                </div>
                <div class="popular_item-text">
                    <div class="popular_item-title">LOREM IPSUM PIE</div>
                    <div class="popular_item-desc">dolor sit amet, consectetur adipiscing elit sed do eiusmod</div>
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
    name: 'indexPopular',
    data() {
      return{

      }
    }
  }
</script>