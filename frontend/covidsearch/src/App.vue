<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <n-icon color="#0e7a0d" size="112">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      viewBox="0 0 32 32"
    >
      <circle cx="15.5" cy="11.5" r="1.5" fill="currentColor"></circle>
      <circle cx="20.5" cy="15.5" r="1.5" fill="currentColor"></circle>
      <circle cx="16" cy="16" r="1" fill="currentColor"></circle>
      <circle cx="16.5" cy="20.5" r="1.5" fill="currentColor"></circle>
      <circle cx="11.5" cy="16.5" r="1.5" fill="currentColor"></circle>
      <path
        d="M28 13v2h-2.05a9.948 9.948 0 0 0-2.215-5.321l1.437-1.437l1.414 1.415L28 8.243L23.758 4l-1.414 1.414l1.414 1.414l-1.437 1.437A9.946 9.946 0 0 0 17 6.05V4h2V2h-6v2h2v2.05a9.946 9.946 0 0 0-5.32 2.215L8.241 6.828l1.414-1.414L8.242 4L4 8.243l1.414 1.414l1.414-1.415L8.265 9.68A9.948 9.948 0 0 0 6.051 15H4v-2H2v6h2v-2h2.05a9.948 9.948 0 0 0 2.215 5.321l-1.437 1.437l-1.414-1.415L4 23.757L8.242 28l1.414-1.414l-1.414-1.414l1.437-1.437A9.946 9.946 0 0 0 15 25.95V28h-2v2h6v-2h-2v-2.05a9.946 9.946 0 0 0 5.32-2.215l1.438 1.437l-1.414 1.414L23.758 28L28 23.757l-1.414-1.414l-1.414 1.415l-1.437-1.437A9.948 9.948 0 0 0 25.949 17H28v2h2v-6zM16 24a8 8 0 1 1 8-8a8.01 8.01 0 0 1-8 8z"
        fill="currentColor"
      ></path>
    </svg>
  </n-icon>
  <n-message-provider>
    <n-loading-bar-provider>
      <div class="page-title">CovidSearch</div>
      <router-view v-slot="{ Component }">
        <keep-alive>
          <component :is="Component" />
        </keep-alive>
      </router-view>
    </n-loading-bar-provider>
  </n-message-provider>
</template>

<script>
export default {
  name: "App",
  components: {},
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 12px;
}
.page-title {
  font-weight: bold;
  font-family: monospace;
  font-size: 42px;
  color: #0e7a0d;
}
</style>
