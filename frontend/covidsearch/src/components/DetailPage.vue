<template>
  <div>
    <n-button  size="large" type="primary" @click = "GoHome" secondary strong>
      <template #icon>
        <n-icon>
          <SearchSharp />
        </n-icon>
      </template>
      Home Page
    </n-button>
  </div>
  <div>
    <n-h1>{{title}}</n-h1>
    <n-list bordered>
      <template #header>
        <n-tag type="success" v-for="author in authors" :key="author">
          {{author}}
        </n-tag>
    </template>
    <template #footer>
      MIT License <br />
      Copyright (c) 2021 Mingtao Chen, Xiaoxin He, Chenhao Huang <br />
    </template>
    <n-list-item>

      <n-thing title="Abstract" >
        <n-ellipsis expand-trigger="click" line-clamp="2" :tooltip="false">
        {{abstract}}
        </n-ellipsis>
      </n-thing>
    </n-list-item>
    <n-list-item>
      <n-thing title="Main" />
      <n-ellipsis expand-trigger="click" line-clamp="2" :tooltip="false">
      {{content}}
      </n-ellipsis>
    </n-list-item>
  </n-list>

  </div>

</template>


<script>
import { SearchSharp } from '@vicons/ionicons5'
import service from "../utils/network";
//import {ref} from "vue";
//    <n-button @click="GetDetail">点它</n-button>

export default {
  name: "DetailPage",
  components:{
    SearchSharp
  },
  data() {
    return {
      id : this.$route.params.id,
      title: "",
      content: "",
      authors: [],
      abstract : ""
    }
  },
  methods:{
   async GetDetail() {
     // `this` will refer to the component instance
     //console.log(this.$data.id);
     let link = "details/".concat(this.id);
     const resp = await service({
       method: "get",
       url: link
     });
     console.log(resp);
     this.title = resp.data.title;
     this.content = resp.data.main_text;
     this.authors = resp.authors.split(";");
     this.abstract = resp.data.abstract
   },
    GoHome(){
     this.$router.push({
			path: '/'
		});
    }

  },
  setup() {

  },
  beforeMount(){
    this.GetDetail()
 },
}
</script>

<style scoped>

</style>