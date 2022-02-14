<template>
  <div class="row mt-5">
    <table class="table table-striped">
      <thead>
      <tr>
        <th>#ID</th>
        <th>Title</th>
        <th>Description</th>
        <th>Shipment</th>
        <th>Created</th>
        <td>Actions</td>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in listItems" :key="item.id">
        <td class="align-middle">{{item.id}}</td>
        <td class="align-middle">{{item.title}}</td>
        <td class="align-middle">{{item.description}}</td>
        <td class="align-middle">{{this.format(item.date_shipment)}}</td>
        <td class="align-middle">{{this.format(item.date_created)}}</td>
        <td class="align-middle">
          <div class="mt-2">
            <router-link :to="{name: 'EditDetails', params: {id: item.id}}" class="btn btn-primary">Edit</router-link>
          </div>
          <div class="mt-2">
            <a href="#" @click.prevent="deleteItem(item)" class="btn btn-danger">Delete</a>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'HomeList',
  computed: {
    ...mapGetters(['SHIPMENTS']),
    listItems () {
      return this.SHIPMENTS
    }
  },
  mounted () {
    this.fetchShipments()
  },
  methods: {
    fetchShipments () {
      this.$store.dispatch('GET_SHIPMENTS')
    },
    format (date) {
      return new Date(date).toLocaleDateString()
    },
    deleteItem (item) {
      this.$store.dispatch('DELETE_SHIPMENT', item.id).then(() => { this.fetchShipments() })
    }
  }
}
</script>
