<template>
  <div id="stocks" v-if="stocks !== null">
    <h1>Stocks!</h1>
    <div v-for="stock in stocks" v-bind:key="stock.id">
      <!--td?-->
      <a v-bind:href="stock.url">{{ stock.title }}</a>
      <div v-for="(tag_name, index) in stock.tags" v-bind:key="index">
        <li>{{ tag_name }}</li>
      </div>
      <p>目次を見る</p>
    </div>
    <div v-if="pageCounter !== null">
      <button v-on:click="getMore">もっとみる</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  el: '#stocks',
  data: function () {
    return {
      stocks: [],
      pageCounter: 1
    }
  },
  methods: {
    getStocks: function () {
      var vm = this
      axios
        .get('/stocks/' + vm.pageCounter)
        .then(
          function (response) {
            if (!response.data.Error) {
              for (let i = 0; i < response.data.length; i++) {
                vm.$set(vm.stocks, (vm.pageCounter - 1) * 20 + i, response.data[i])
              }
              if (response.data.length < 20) {
                vm.pageCounter = null
              }
              console.log(response.data)
              console.log(vm.stocks)
            }
          }
        )
    },
    getMore: function () {
      var vm = this
      if (vm.pageCounter !== null) {
        vm.pageCounter++
        vm.getStocks()
      }
    }
  },
  created: function () {
    this.getStocks()
  }
}
</script>

<style>
#stocks {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 690px;
  margin: 60px auto;
}
</style>
