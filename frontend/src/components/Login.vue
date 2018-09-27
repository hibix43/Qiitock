<template>
  <div id="login" v-if="results !== null">
    <h1>Login!</h1>
    <a v-bind:href="results">ログイン・認証</a>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  el: '#login',
  data: function () {
    return {
      results: null
    }
  },
  methods: {
    getLoginURL: function () {
      var vm = this
      axios
        .get('/login')
        .then(
          function (response) {
            if (response.data.login_url) {
              vm.results = response.data.login_url
            }
          }
        )
    }
  },
  created: function () {
    this.getLoginURL()
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
