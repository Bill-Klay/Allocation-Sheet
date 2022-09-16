import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'
import LogIn from './components/LogIn.vue'
import HelloWorld from './components/HelloWorld.vue'
import NotFound from './components/404.vue'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(VueSession, { persist: true })

const routes = [
    { path: '/', redirect: '/login' }, // also can use alias: for this purpose, but that does not change the url
    { path: '/login', component: LogIn },
    { path: '/hello', component: HelloWorld },
    { path: '/:notfound(.*)', component: NotFound }
]

const router = new VueRouter({
    mode: 'history',
    routes
});

new Vue({
    vuetify,
    router,
    render: h => h(App)
}).$mount('#app')
