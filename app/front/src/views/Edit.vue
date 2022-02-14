<template>
  <div class="container">
    <edit-form/>
  </div>
</template>

<script>
import EditForm from '@/components/edit/Edit'

export default {
  name: 'Edit',
  components: { EditForm },
  mounted () {
    this.fetchShipment()
  },
  methods: {
    fetchShipment () {
      const itemId = this.$route.params.id
      if (!itemId) {
        this.$store.dispatch('CLEAR_SHIPMENT').then(() => {}).catch(() => {})
        return
      }
      this.$store.dispatch('GET_SHIPMENT', itemId).then(() => {}).catch(() => {})
    }
  }
}
</script>
