<template>
  <div id="login" v-if="login_url">
    <h1>Welcome to Qiitock !</h1>
    <a v-bind:href="login_url" class="button">Qiitaアカウントにログインする</a>
    <div class="description">
      <h2>Qiitockとは</h2>
      <p>プログラマのための問題共有サイト<a href="https://qiita.com">Qiita</a></p>
      <p>数ある投稿のなかから、あなたが</p>
      <p>役立つ記事だ。もう一度、読むはずだ。</p>
      <p>そう感じてストックした良質な記事。</p>
      <p>Qiitockは、そんなあなたのストックを</p>
      <p>振り返りやすくするWebサービスです。</p>
    </div>
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
  text-align: center;
  width: 100%;
  padding: 0;
  padding-top: 64px;
}
#login h1 {
  margin-bottom: 64px;
  font-size: 3rem;
  color: #59ABE3;
}
#login .button {
  padding: 16px 64px;
  background: #59ABE3;
  border: 2px solid #59ABE3;
  border-radius: 4px;
}
#login > a, #login > a:hover, #login > a:visited {
  text-decoration: none;
  font-weight: bold;
  color: #FFFFFF;
}
#login .description {
  text-align: center;
  padding: 32px;
  color: #2c3e50;
}
#login .description a,
#login .description a:hover,
#login .description a:visited {
  text-decoration: none;
  font-weight: bold;
  color: #59ABE3;
}

#login .description p {
  margin: 16px 0;
}
</style>
