<template>
  <n-form class="search-wrapper">
    <n-form-item>
      <n-input-group>
        <n-input
          v-model:value="queryStr"
          class="search-input"
          placeholder="search anything you want!"
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

    <n-list bordered>
      <div v-for="query of queryItems" :key="query.id">
       <n-list-item>
          <router-link :to="'/detail/' + query.id">
          <div v-html="query.title"></div>
          </router-link>
       </n-list-item>
      </div>
    </n-list>

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
    const queryItems = ref([]);

    const onLoadQueryItems = (currentRawObj) => {
      let obj = {id: "", title: ""}
      for(const value of Object.values(currentRawObj)) {
        obj = {}
        obj.id = value._id
        obj.title = value.highlight?.title ? value.highlight.title[0] : value.fields.title[0]
        queryItems.value.push(obj)
      }
      // chekc if abstract hightlight, if not exist then chekc main text
    }
    
    const onSearch = async () => {
      // console.log(queryStr.value);
      queryItems.value = [];
      const resp = await service({
        method: "get",
        url: "/search",
        params: {
          q: queryStr.value,
        },
      });
      console.log(resp);
      // queryItems.value = resp.hits;
      onLoadQueryItems(resp.hits);
      console.log("queryItems",queryItems.value)
    };
    return {
      queryStr,
      onSearch,
      onLoadQueryItems,
      queryItems,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.search-wrapper {
  width: 50%;
  display: block;
  margin: 0 auto;
}

em {
  font-weight: bold;
}
</style>
