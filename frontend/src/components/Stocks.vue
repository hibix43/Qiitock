<template>
  <div id="stocks" v-if="stocks !== null">
    <h1>Stocks!</h1>
    <div v-for="stock in stocks" v-bind:key="stock.id">
      <!--td?-->
      <a v-bind:href="stock.url">{{ stock.title }}</a>
      <ul>
        <li v-for="(tag_name, index) in stock.tags" v-bind:key="index">
          {{ tag_name }}
        </li>
      </ul>
      <button v-on:click="toggleAgenda(stock)">Agenda</button>
      <div v-show="stock.show_agenda">
        <span v-html="stock.agenda"></span>
      </div>
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
      let vm = this
      axios
        .get('/stocks/' + vm.pageCounter)
        .then(
          function (response) {
            if (!response.data.Error) {
              for (let i = 0; i < response.data.length; i++) {
                const index = (vm.pageCounter - 1) * 20 + i
                // JSONデータを配列に格納
                vm.$set(vm.stocks, index, response.data[i])
                // 目次の表示トグル
                vm.$set(vm.stocks[index], 'show_agenda', false)
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
      let vm = this
      if (vm.pageCounter !== null) {
        vm.pageCounter++
        vm.getStocks()
      }
    },
    toggleAgenda: function (stock) {
      stock.show_agenda = !stock.show_agenda
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
