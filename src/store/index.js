import Vue from 'vue'
import Vuex from 'vuex'
import {mutations} from './mutations.js'


Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        articles: [],
        tag: '',
    },
    mutations
})
export default store
