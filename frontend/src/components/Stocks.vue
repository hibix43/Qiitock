<template>
  <div id="stocks" v-if="stocks !== null">
    <h1>Stocks!</h1>
    <input type="text" v-model="searchWords" placeholder="Search title or tag.."/>
    <div v-for="stock in filteredStocks" v-bind:key="stock.id">
      <!--td?-->
      <h2>{{ stock.title }}</h2>
      <a v-bind:href="stock.url" target="_blank">Qiitaで読む</a>
      <button v-on:click="toggleAgenda(stock)">アジェンダを見る</button>
      <div v-for="(tagName, index) in stock.tags" v-bind:key="index">
        <button v-on:click="searchStocksByTag(tagName)">{{ tagName }}</button>
      </div>
     <div v-show="stock.showAgenda">
        <span v-html="stock.agenda"></span>
        <button v-on:click="toggleAgenda(stock)">アジェンダを閉じる</button>
      </div>
    </div>
    <div v-if="pageCounter !== null">
      <button v-on:click="getMoreStocks">もっとみる</button>
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
      pageCounter: 1,
      searchWords: ''
    }
  },
  computed: {
    filteredStocks: function () {
      // 検索指定がなければすべて
      if (this.searchWords === '') {
        return this.stocks
      } else {
        // 検索
        return this.searchStocks()
      }
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
                vm.$set(vm.stocks[index], 'showAgenda', false)
              }
              // これ以上のストックは存在しない
              if (response.data.length < 20) {
                vm.pageCounter = null
              }
              console.log(response.data)
              console.log(vm.stocks)
            }
          }
        )
    },
    getMoreStocks: function () {
      let vm = this
      if (vm.pageCounter !== null) {
        vm.pageCounter++
        vm.getStocks()
      }
    },
    toggleAgenda: function (stock) {
      stock.showAgenda = !stock.showAgenda
    },
    searchStocks: function () {
      // 検索結果
      let stocks = []
      // 検索ワードを整形
      let searchWords = this.arangeSearchWords()
      // 各投稿に関して
      for (let s of this.stocks) {
        // 検索ワードが含まれるか
        for (let word of searchWords) {
          if (s.title.toLowerCase().indexOf(word) !== -1 ||
              s.tags.some(tag => tag.toLowerCase().indexOf(word) !== -1)) {
            // ヒット
            stocks.push(s)
          }
        }
      }
      console.log(stocks)
      return stocks
    },
    arangeSearchWords: function () {
      let words = []
      // 大文字・小文字両方
      for (let word of this.searchWords.split(' ')) {
        words.push(word.toLowerCase())
      }
      return words
    },
    searchStocksByTag: function (tag) {
      this.searchWords = tag
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
