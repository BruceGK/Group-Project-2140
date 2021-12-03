<template>
  <n-form class="search-wrapper">
    <n-form-item>
      <n-input-group>
        <n-input
          v-model:value="queryStr"
          class="search-input"
        />
        <n-button
          attr-type="submit"
          @click="onSearch"
          class="search-btn"
          type="primary"
          ghost
        >
          Search
        </n-button>
      </n-input-group>
    </n-form-item>
  </n-form>
</template>

<script>
import service from "../utils/network";
import { ref } from "vue";
export default {
  name: "homePage",
  props: {
    msg: String,
  },
  setup() {
    const queryStr = ref("");
    const onSearch = async () => {
      console.log(queryStr.value);
      const resp = await service({
        method: "get",
        url: "/search",
        params: {
          q: queryStr.value,
        },
      });
      console.log(resp);
    };
    return {
      queryStr,
      onSearch,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search-wrapper {
  width: 50%;
  display: block;
  margin: 0 auto;
}
</style>
