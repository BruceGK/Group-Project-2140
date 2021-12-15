<template>
  <n-spin :show="loading">
    <div class="title">
      <router-link to="/" style="text-decoration: none">
        <n-button size="large" type="primary" secondary strong>
          <template #icon>
            <n-icon>
              <SearchSharp />
            </n-icon>
          </template>
          Home Page
        </n-button>
      </router-link>
      <n-h1>{{ title }}</n-h1>
    </div>
    <div class="main">
      <n-list bordered>
        <template #header title="Authors">
          <div>
            <n-tag class="authors" type="success" v-for="author in authors" :key="author">
              {{ author }}
            </n-tag>
          </div>
          <n-divider />
          <div v-if="url">
            <a style="text-decoration: none" :href="url" target="_blank">
              <n-button type="info" dashed>Take me to Article Page</n-button>
            </a>
          </div>
        </template>
        <template #footer>
          MIT License <br />
          Copyright (c) 2021 Mingtao Chen, Xiaoxin He, Chenhao Huang <br />
        </template>
        <n-list-item>
          <n-thing title="Abstract">
            <!-- <n-ellipsis expand-trigger="click" line-clamp="2" :tooltip="false"> -->
              {{ abstract }}
            <!-- </n-ellipsis> -->
          </n-thing>
        </n-list-item>
        <n-list-item>
          <n-thing title="Main" />
          <n-back-top :right="100" />
          <n-scrollbar style="max-height: 800px">
            {{ content }}
          </n-scrollbar>
        </n-list-item>
      </n-list>
    </div>
  </n-spin>
</template>

<script>
import { SearchSharp } from "@vicons/ionicons5"
import service from "../utils/network"
//import {ref} from "vue";
//    <n-button @click="GetDetail">点它</n-button>
import { computed } from "vue"
import { useLoadingBar, useMessage } from "naive-ui"
export default {
  name: "DetailPage",
  components: {
    SearchSharp,
  },

  data() {
    return {
      id: computed(() => this.$route.params.id),
      title: "",
      content: "",
      authors: [],
      abstract: "",
      url: "",
      loading: false,
    }
  },

  methods: {
    async GetDetail() {
      // `this` will refer to the component instance
      //console.log(this.$data.id);
      this.loadingBar.start()
      this.loading = true
      try {
        let link = "details/".concat(this.id)
        const resp = await service({
          method: "get",
          url: link,
        })
        console.log(resp)
        this.title = resp.data.title
        this.content = resp.data.main_text
        this.authors = resp.authors.split(";")
        this.abstract = resp.data.abstract
        this.url = resp.url
        this.loadingBar.finish()
      } catch (err) {
        console.log(err)
        this.loadingBar.error()
        if (err.response?.status == 400) {
          this.message.error(err.response.data)
        } else {
          this.message.error("Failed to fetch detail data")
        }
      } finally {
        this.loading = false
      }
    },
    GoHome() {
      this.$router.push({
        path: "/",
      })
    },
    Golink() {
      window.open(this.url)
    },
  },
  setup() {
    const loadingBar = useLoadingBar()
    const message = useMessage()
    return {
      loadingBar,
      message,
    }
  },
  activated() {
    this.GetDetail()
  },
}
</script>

<style scoped>
.main {
  margin-right: 100px;
  margin-left: 100px;
}

.authors {
  margin: 0 2px;
}

.title {
  margin-right: 50px;
  margin-left: 50px;
}
</style>
