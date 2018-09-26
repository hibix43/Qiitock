import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Stocks from '@/components/Stocks'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: {
        Login,
        Stocks
      }
    }
  ]
})
