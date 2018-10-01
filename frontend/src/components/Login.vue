<template>
  <div id="login" v-if="login_url">
    <h1>Login!</h1>
    <a v-bind:href="login_url">ログイン・認証</a>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  el: '#login',
  data: function () {
    return {
      login_url: null,
      error: ''
    }
  },
  methods: {
    getLoginURL: function () {
      var vm = this
      axios
        .get('/login')
        .then(
          function (response) {
            if (response.data.error) {
              vm.error = response.data.error.error_msg
            } else if (response.data.login_data) {
              vm.login_url = response.data.login_data.login_url
            }
          }
        )
    }
  },
  created: function () {
    this.getLoginURL()
    console.log(this)
  }
}
</script>

<style>
#login {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
