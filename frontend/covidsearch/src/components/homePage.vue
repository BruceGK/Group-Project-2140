<template>
  <n-radio-group v-model:value="searchMode" name="searchmode" @change="onSwitchSearchMode(searchMode)">
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

  <n-form :show-feedback="false" class="search-wrapper" v-if="searchMode === 'boolean'">
    <n-form-item v-for="(item, index) in addSelection" :key="index">
      <n-input-group>
      <n-button :disabled="index == 0" style="width: 10%" @click="onDeleteSelections(index)">
      <n-icon size="20"><Trash/></n-icon>
      </n-button>
      <n-select :style="{ width: '15%' }" :options="typeOptions" v-model:value="item.type"/>
      <!-- v-model:value="item.query" -->
      <n-input :style="{ width: '60%' }" v-model:value="item.query"/>
      <n-select :style="{ width: '15%' }" :options="fieldOptions" v-model:value="item.field"/>
    </n-input-group>
    </n-form-item>
    <n-button style="margin-top: 12px;" @click="onAddSelections" type="primary" circle>
      <n-icon size="40"><AddCircle24Filled/></n-icon>
    </n-button>
    <n-button strong secondary round type="success" @click="onSearch">Search</n-button>
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
  <n-pagination class="pagination" v-model:page="page" :page-count="pageCount" v-if="searchMode === 'boolean' && onClickSearch && pageCount > 0"/>
</template>

<script>
import service from "../utils/network"
import { ref } from "vue"
import { useMessage } from "naive-ui"
import { AddCircle24Filled } from '@vicons/fluent'
import { Trash } from '@vicons/fa'

export default {
  name: "homePage",
  props: {
    msg: String,
  },
  components: {
    AddCircle24Filled,
    Trash
  },
  setup() {
    const queryStr = ref("")
    const queryItems = ref([])
    const searchMode = ref("keyword")
    const searching = ref(false)
    const typeOptions = ref([
        { label: 'And', value: 'and' },
        { label: 'Or', value: 'or' },
        { label: 'Not', value: 'not' }
    ])
    const fieldOptions = ref([
      { label: 'Title', value: 'title'},
      { label: 'Abstract', value: 'abstract' },
      { label: 'Main_text', value: 'main_text'}
    ])
    const addSelection = ref([{type: 'and', query: '', field: 'title'}])
    const searchModeData = ref({})
    const pageCount = ref(0)
    const onClickSearch = ref(false)

    const onSwitchSearchMode = (curSearchMode) => {
      queryItems.value = []
      if (Object.keys(searchModeData.value).includes(curSearchMode)) {
        queryItems.value = searchModeData.value[curSearchMode]
      }
    }

    const onLoadQueryItems = (searchMode,currentRawObj) => {
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
      searchModeData.value[searchMode] = queryItems.value
    }
    const message = useMessage()

    const onDeleteSelections = (index) => {
      addSelection.value.splice(index, 1);
    }

    const onAddSelections = () => {
      addSelection.value.push({type: 'and', query: '', field: 'title'})
    }

    const onSearch = async () => {
      console.log(queryStr.value);
      if (searching.value || searchMode.value !== "boolean" && !queryStr.value) return
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
          console.log("boolean search hit", addSelection.value)
          // TODO...
          onClickSearch.value = true
          resp = await service({
            method: "post",
            url: "/boolean",
            data: {
                "queries": addSelection.value,
                "start": "1"
            },
            headers: {
              'Content-Type': 'application/json'
            }
          })
          if(resp.total.value >= 20) {
            pageCount.value = Math.round(resp.total.value / 20);
          }
        }

        console.log("resp",resp)
        // queryItems.value = resp.hits;
        onLoadQueryItems(searchMode.value,resp.hits)
        console.log("queryItems", queryItems.value)
      } catch (err) {
        console.log(err)
        if (err.response?.status == 400) {
          message.error(err.response.data)
        } else {
          message.error("Failed to fetch search result")
        }
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
      typeOptions,
      fieldOptions,
      onDeleteSelections,
      onAddSelections,
      addSelection,
      onSwitchSearchMode,
      searchModeData,
      pageCount,
      onClickSearch
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
  margin: 12px auto;
}

em {
  font-weight: bold;
}

.main_text em {
  color: #ea4335;
}
.pagination{
  display: flex;
  justify-content: center;
}
</style>
