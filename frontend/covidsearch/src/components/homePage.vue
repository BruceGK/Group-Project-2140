<template>
    <n-input-group>
      <n-input :style="{ width: '50%' }" />
      <n-button type="primary" ghost>Search</n-button>
    </n-input-group>
</template>

<script>
export default {
  name: 'homePage',
  props: {
    msg: String
  }

  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
