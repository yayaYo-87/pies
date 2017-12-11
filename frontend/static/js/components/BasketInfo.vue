<template>
    <div class="basket__wrapper" v-if="nextValid === 2">
        <div class="basket__info">
            <div class="basket__info_title">Ваши данные:</div>
            <div class="basket__info_input">
                <label for="name">Имя и Фамилия:</label>
                <input type="text" id="name" class="form_input" placeholder="Введите Имя и Фамилию..." v-model="firstName">
                <div class="valid" v-show="!validation.FirstName">*Введите корректное Имя</div>
            </div>
            <div class="basket__info_input">
                <label for="phone">Телефон:</label>
                <masked-input mask="\+\7(111)111-11-11" class="form_input" placeholder="Телефон" id="phone" type="tel" v-model="phone"/>
                <div class="valid" v-show="!validation.phone">*Введите корректный телефон</div>
            </div>
            <div class="basket__info_input">
                <label for="email">E-mail:</label>
                <input type="text" id="email" class="form_input" placeholder="Введите e-mail..." v-model="email">
                <div class="valid" v-show="!validation.email">*Введите корректный e-mail</div>
            </div>
            <div class="basket__info_input">
                <label for="address">Адрес:</label>
                <input type="text" id="address" class="form_input" placeholder="Введите адрес..." v-model="address">
                <div class="valid" v-show="!validation.address">*Введите корректный адрес</div>
            </div>
        </div>
        <button class="basket__button" :disabled="!isValid && buttonDisabled" @click="postOrder()" >Оформить заказ</button>
    </div>
</template>

<script>
  import axios from 'axios'
  import MaskedInput from 'vue-masked-input'
  export default {
    data() {
      return {
        buttonDisabled: true,
        email: '',
        firstName: '',
        phone: '',
        address: '',

        emailRE: /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
        telRE: /^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$/,
      }
    },
    components:{
      MaskedInput
    },
    methods: {
      next(value){
        this.$store.commit('results', { type: 'validation', items: value})
      },
      errorPopup(now){
        const newDiv = document.createElement('div')
        newDiv.classList.add('popup')
        newDiv.innerHTML = now

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      },
      postOrder() {
        let self = this;
        this.buttonDisabled = false;
        axios.post('/api/order/', {
          "total_count": self.basket.results.total_count,
          "address": self.address,
          "first_name": self.firstName,
          "email": self.email,
          "phone": self.phone,
          "total": self.basket.results.price,
        }).then(
          function (response) {
            self.$store.commit('results', { type: 'validation', items: 3})
            self.$store.dispatch('results');
          }, function (error) {
          }
        )
      }

    },
    computed: {
      basket() {
        return this.$store.state.basket
      },
      nextValid() {
        return this.$store.state.basket.validation
      },

      validation: function () {
        return {
          FirstName: !!this.firstName.trim(),
          address: !!this.address.trim(),
          phone: this.telRE.test(this.phone),
          email: this.emailRE.test(this.email),
        }
      },
      isValid: function () {
        let validation = this.validation;
        return Object.keys(validation).every(function (key) {
          return validation[key]
        });
      }
    }

  }
</script>