import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'
import LogIn from './components/LogIn.vue'
import HelloWorld from './components/HelloWorld.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

const routes = [
    { path: '/', redirect: '/login' }, // also can use alias: for this purpose, but that does not change the url
    { path: '/login', component: LogIn },
    { path: '/hello', component: HelloWorld }
]

const router = new VueRouter({
    routes
});

new Vue({
    vuetify,
    router,
    render: h => h(App)
}).$mount('#app')
