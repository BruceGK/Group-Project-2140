<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <homePage msg="Welcome to Your Vue.js App"/>
</template>

<script>
import homePage from './components/homePage.vue'

export default {
  name: 'App',
  components: {
    homePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
