<template>
  <n-radio-group v-model:value="searchMode" name="searchmode">
    <n-radio-button value="keyword"> Keyword </n-radio-button>
    <n-radio-button value="ml"> Machine Learning </n-radio-button>
    <n-radio-button value="boolean"> Boolean </n-radio-button>
  </n-radio-group>

  <n-form class="search-wrapper" v-if="searchMode !== 'boolean'">
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
          :loading="searching"
        >
          Search
        </n-button>
      </n-input-group>
    </n-form-item>
  </n-form>

  <n-list class="search-results" bordered>
    <div v-for="query of queryItems" :key="query.id">
      <n-list-item>
        <router-link :to="'/detail/' + query.id">
          <div v-html="query.title"></div>
        </router-link>
        <div v-html="query.mainText" class="main_text"></div>
      </n-list-item>
    </div>
  </n-list>
</template>

<script>
import service from "../utils/network"
import { ref } from "vue"
export default {
  name: "homePage",
  props: {
    msg: String,
  },
  setup() {
    const queryStr = ref("")
    const queryItems = ref([])
    const searchMode = ref("keyword")
    const searching = ref(false)

    const onLoadQueryItems = (currentRawObj) => {
      let obj = { id: "", title: "", mainText: "" }
      for (const value of Object.values(currentRawObj)) {
        obj = {}
        obj.id = value._id
        obj.title = value.highlight?.title
          ? value.highlight.title[0]
          : value.fields.title[0]
        obj.mainText = value.highlight?.main_text
          ? value.highlight.main_text[0]
          : ""
        queryItems.value.push(obj)
      }
      // chekc if abstract hightlight, if not exist then chekc main text
    }

    const onSearch = async () => {
      // console.log(queryStr.value);
      if (searching.value) return
      queryItems.value = []
      searching.value = true
      try {
        let resp
        if (searchMode.value === "keyword") {
          resp = await service({
            method: "get",
            url: "/search",
            params: {
              q: queryStr.value,
            },
          })
        } else if (searchMode.value === "ml") {
          resp = await service({
            method: "get",
            url: "/mlsearch",
            params: {
              q: queryStr.value,
            },
          })
        } else if (searchMode.value === "boolean") {
          // TODO...
        }

        console.log(resp)
        // queryItems.value = resp.hits;
        onLoadQueryItems(resp.hits)
        console.log("queryItems", queryItems.value)
      } catch (err) {
        console.log(err)
      } finally {
        searching.value = false
      }
    }
    return {
      queryStr,
      onSearch,
      onLoadQueryItems,
      queryItems,
      searchMode,
      searching,
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.search-wrapper {
  width: 50%;
  display: block;
  margin: 0 auto;
}
.search-results {
  width: 65%;
  margin: 0 auto;
}

em {
  font-weight: bold;
}

.main_text em {
  color: red;
}
</style>
