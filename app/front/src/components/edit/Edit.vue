<template>
  <div class="row mt-5">
    <h3 class="mb-5">Create/Edit</h3>
    <div class="alert alert-warning" v-if="errors.length">
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>
    <form @submit="addUpdateItem">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input v-model="SHIPMENT.title" type="text" class="form-control" id="title">
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="SHIPMENT.description" class="form-control" id="description" rows="3"></textarea>
      </div>
      <div class="mb-3">
        <label for="date_created" class="form-label">Date Shipment</label>
        <input v-model="SHIPMENT.date_shipment" id="date_created" type="date" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
  name: 'EditForm',
  data () {
    return {
      errors: []
    }
  },
  computed: {
    ...mapGetters(['SHIPMENT'])
  },
  methods: {
    addUpdateItem (e) {
      if (this.SHIPMENT.title && this.SHIPMENT.description && this.SHIPMENT.date_shipment) {
        if (this.SHIPMENT.id) {
          this.$store.dispatch('UPDATE_SHIPMENT', this.SHIPMENT).then(() => {}).catch(() => {})
        } else {
          this.$store.dispatch('ADD_SHIPMENT', this.SHIPMENT).then(() => {}).catch(() => {})
        }
        return this.$router.push({ name: 'Home' })
      }

      this.errors = []

      if (!this.SHIPMENT.title) {
        this.errors.push('Title can\'t be empty')
      }
      if (!this.SHIPMENT.description) {
        this.errors.push('Description can\'t be empty')
      }
      if (!this.SHIPMENT.date_shipment) {
        this.errors.push('Date shipment can`t be empty')
      }
      e.preventDefault()
    }
  }
}
</script>
