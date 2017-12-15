<template>
    <div class="basket__wrapper" v-if="validation === 1">
        <div class="basket__error" v-if="basket.results.cart_goods && basket.results.cart_goods.length === 0">
            <div class="basket__error-text">Ваша корзина пуста :(</div>
            <router-link
                    tag="button"
                    :to="{ name: 'menu', params: {id: 'all'} }" class="basket__button">Вернуться в меню</router-link>
        </div>
        <div class="basket_info" v-if="basket.results.cart_goods && basket.results.cart_goods.length !== 0">
            <table class="basket_table">
                <tr class="basket_tr">
                    <th class="basket_w"></th>
                    <th>Наименование</th>
                    <th class="basket_width">Цена</th>
                    <th class="basket_width">Количество</th>
                    <th class="basket_width">Итого</th>
                </tr>
                <tr v-for="cart in  basket.results.cart_goods">

                    <td>
                        <div class="basket_table-active">
                            <div class="basket_table-close" @click="switchItem(cart.id, 'deactivate')">+</div>
                            <div class="basket_table-button" v-if="!cart.active">
                                <button class="basket-header_button" @click="switchItem(cart.id , 'activate')">
                                    Вернуть обратно
                                </button>
                            </div>
                        </div>
                    </td>
                    <td>
                        <div class="basket_table-flex">
                            <div class="basket_table-img">
                                <img :src="cart.goods.cover" alt="cover">
                            </div>
                            <div class="basket_table-text">{{cart.goods.name}}</div>
                        </div>
                    </td>
                    <td v-if="cart.weight.discount_price === 0">{{cart.weight.price}} <span class="rubl" > &#8399;</span></td>
                    <td v-else>{{cart.weight.discount_price}} <span class="rubl" > &#8399;</span></td>
                    <td>
                        <button class="basket_table_minus"

                                :disabled="cart.count === 1 || buttonDisabled"
                                @click="switchItem(cart.id,'dec')">-</button>

                        {{ cart.count }}
                        <button :disabled="buttonDisabled"
                                class="basket_table_plus"
                                @click="switchItem(cart.id,'inc')">+</button>
                    </td>
                    <td>{{cart.price}} <span class="rubl" > &#8399;</span></td>
                </tr>
            </table>
            <div class="basket__total">
                <div class="basket__total-wrapper">
                    <div class="basket__total_text">К оплате:</div>
                    <div class="basket__total_count">
                        <div class="basket__total-title">Итого</div>
                        <div class="basket__total-title">{{ basket.results.price }} <span class="rubl" > &#8399;</span></div>
                    </div>
                    <button class="basket__button" @click="next(2)" >Оформить заказ</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        buttonDisabled: false
      }
    },
    methods: {
      switchItem(id, inc){
        let self = this;
        this.buttonDisabled = true;
        axios.post('/api/order_goods/' + id + '/'+ inc +'/')
          .then((response) => {
            if (response.status === 200) {
              self.buttonDisabled = false;
              self.$store.dispatch('results')
            }
          })
      },
      next(value){
        if(this.basket.results.price === 0){
            this.errorPopup('Добавьте товар!')
        } else{
          this.$store.commit('results', { type: 'validation', items: value})
        }
      },
      errorPopup(now){
        const newDiv = document.createElement('div')
        newDiv.classList.add('popup')
        newDiv.innerHTML = now

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      }
    },
    computed: {
      basket() {
        return this.$store.state.basket
      },
      validation() {
        return this.$store.state.basket.validation
      }
    }

  }
</script>