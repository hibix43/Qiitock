<template>
  <div id="stocks" v-if="stocks !== null">
    <h1>Stocks!</h1>
    <ul>
      <li v-for="stock in stocks" v-bind:key="stock.id">
        <a v-bind:href="stock.url">{{ stock.title }}</a>
      </li>
    </ul>
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
  },
  mounted: function () {
    this.getStocks()
  }
}
</script>

<style>
#stocks {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
