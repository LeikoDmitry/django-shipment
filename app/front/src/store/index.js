import { createStore } from 'vuex'
import axios from 'axios'
import API_URL from '@/common/config'

export default createStore({
  state: {
    shipments: [],
    shipment: {}
  },
  getters: {
    SHIPMENTS: state => {
      return state.shipments
    },
    SHIPMENT: state => {
      return state.shipment
    }
  },
  mutations: {
    SET_SHIPMENTS: (state, payload) => {
      state.shipments = payload.results
    },
    SET_SHIPMENT: (state, payload) => {
      state.shipment = payload
    },
    CLEAR_SHIPMENT: (state) => {
      state.shipment = {}
    }
  },
  actions: {
    GET_SHIPMENTS: async (context) => {
      const { data } = await axios.get(API_URL + 'shipments/')
      context.commit('SET_SHIPMENTS', data)
    },
    CLEAR_SHIPMENT: async (context) => {
      context.commit('CLEAR_SHIPMENT')
    },
    DELETE_SHIPMENT: async (context, itemId) => {
      await axios.delete(API_URL + 'shipments/' + itemId)
    },
    GET_SHIPMENT: async (context, itemId) => {
      const { data } = await axios.get(API_URL + 'shipments/' + itemId)
      context.commit('SET_SHIPMENT', data)
    },
    ADD_SHIPMENT: async (context, item) => {
      await axios.post(API_URL + 'shipments/', item)
    },
    UPDATE_SHIPMENT: async (context, item) => {
      await axios.put(API_URL + 'shipments/' + item.id + '/', item)
    }
  },
  modules: {}
})
