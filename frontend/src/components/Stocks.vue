<template>
  <div id="stocks" v-if="stocks.length > 0">
    <div id="headline">
      <h1>Qiitock</h1>
      <div class="search">
        <input type="text" v-model="searchWords" placeholder="Search title or tag ..."/>
        <button v-on:click="resetSearch()">Reset</button>
      </div>
    </div>
    <div id="main">
      <div v-for="stock in filteredStocks" v-bind:key="stock.id" class="stock">
        <h2>{{ stock.title }}</h2>
        <div class="tag-buttons">
          <div v-for="(tagName, index) in stock.tags" v-bind:key="index">
            <button v-on:click="searchStocksByTag(tagName)">{{ tagName }}</button>
          </div>
        </div>
        <div class="link-buttons">
          <button v-on:click="toggleAgenda(stock)" class="agenda-button">{{ stock.agendaText }}</button>
          <a v-bind:href="stock.url" target="_blank" class="qiita-link">Qiitaで読む</a>
          <div v-show="stock.showAgenda">
            <span v-html="stock.agenda" class="agenda-list"></span>
            <button v-on:click="toggleAgenda(stock)" class="agenda-button">{{ stock.agendaText }}</button>
          </div>
        </div>
      </div>
      <div v-if="pageCounter !== null" id="more-show">
        <button v-on:click="getMoreStocks">もっとみる</button>
      </div>
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
      error: '',
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
            if (response.data.error) {
              vm.error = response.data.error.error_msg
            } else if (response.data.stocks) {
              const stocks = response.data.stocks
              for (let i = 0; i < stocks.length; i++) {
                const index = (vm.pageCounter - 1) * 20 + i
                // JSONデータを配列に格納
                vm.$set(vm.stocks, index, stocks[i])
                // 目次の表示トグル
                vm.$set(vm.stocks[index], 'showAgenda', false)
                vm.$set(vm.stocks[index], 'agendaText', 'アジェンダを開く')
              }
              // これ以上のストックは存在しない
              if (response.data.length < 20) {
                vm.pageCounter = null
              }
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
      stock.agendaText = stock.showAgenda ? 'アジェンダを閉じる' : 'アジェンダを開く'
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
    },
    resetSearch: function () {
      this.searchWords = ''
    }
  },
  created: function () {
    this.getStocks()
  }
}
</script>

<style>
#container {
  background-color: #59ABE3;
}
#stocks {
  width: 100%;
}
#headline {
  width: 100%;
  text-align: center;
  padding: 64px 0;
  background-color: #59ABE3;
}
#headline h1 {
  margin-bottom: 32px;
  font-size: 3rem;
  color:#FFFFFF;
}
#headline .search input {
  padding: 10px;
  font-size: 1.3em;
  font-family: Arial, sans-serif;
  color: #aaa;
  border: 1px solid #ccc;
  margin: 0 0 20px;
  width: 300px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-box-shadow: inset 0 0 4px rgba(0,0,0,0.2);
  -webkit-box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2);
}
#headline .search button,
#more-show button {
  padding: 8px 32px;
  border: 2px solid #59ABE3;
  background-color: #FFFFFF;
  color: #59ABE3;
  border-radius: 5px;
  font-size: 1.3em;
  font-weight: 600;
}
#main {
  background-color: #59ABE3;
}
#main .stock {
  max-width: 690px;
  margin: -1px auto 16px auto;
  padding: 64px;
  color: #2c3e50;
  background-color: #FFFFFF;
  border-radius:5px;
  -moz-box-shadow:0 2px 2px 0 rgba(0,0,0,0.2);
  -webkit-box-shadow:0 2px 2px 0 rgba(0,0,0,0.2);
  box-shadow:0 2px 2px 0 rgba(0,0,0,0.2);
}
#main .stock:first-child {
  margin-top: -32px;
}
#main .stock .tag-buttons {
  text-align: right;
}
#main .stock .tag-buttons div {
  display: inline-block;
}
#main .stock .tag-buttons button {
  padding: 8px;
  font-size: 1rem;
  font-weight: 500;
  border: 0;
  background-color: #FFFFFF;
  color: #999999;
}
#main .stock .link-buttons .qiita-link,
#main .stock .link-buttons .agenda-button{
    padding: 8px;
    font-size: .8em;
    font-weight: 100;
    border-style: none;
    background: #59ABE3;
    border-radius: 3px;
    color: #FFFFFF;
}
#main .stock .link-buttons .qiita-link {
    text-decoration: none;
    line-height: normal;
    display: inline-block;
}
#main .stock .link-buttons .agenda-list ul{
  word-break: break-all;
  padding-inline-start: 8px;
}
#more-show {
  text-align: center;
  padding: 24px 0 64px 0;
}
</style>
