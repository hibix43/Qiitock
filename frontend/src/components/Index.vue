<template>
  <div id="login" v-if="results.login_url">
    <h1>Login!</h1>
    <a v-bind:href="results.login_url">ログイン・認証</a>
  </div>
  <div v-else>
    <h1>Logged</h1>
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
            vm.results = response.data
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
