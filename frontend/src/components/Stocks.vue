<template>
  <div id="stocks" v-if="stocks !== null">
    <h1>Stocks!</h1>
    <div v-for="(stock, tag) in stocks" v-bind:key="stock.id">
      <h2>{{ tag }}</h2>
      <ul>
        <li v-for="item in stock" v-bind:key="item.id">
          <a v-bind:href="item.url">{{ item.title }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  el: '#stocks',
  data: function () {
    return {
      stocks: null
    }
  },
  methods: {
    getStocks: function () {
      var vm = this
      axios
        .get('/stocks')
        .then(
          function (response) {
            if (!response.data.Error) {
              vm.stocks = response.data
            }
          }
        )
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
