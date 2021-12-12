<template>
  <div class = "title">
    <n-button  size="large" type="primary" @click = "GoHome" secondary strong>
      <template #icon>
        <n-icon>
          <SearchSharp />
        </n-icon>
      </template>
      Home Page
    </n-button>
    <n-h1>{{title}}</n-h1>
  </div>
  <div class = "main">
    <n-list bordered>
      <template #header title="Authors">
        <div>
           <n-tag type="success" v-for="author in authors" :key="author">
          {{author}}
        </n-tag>

        </div>
         <n-divider />
        <div><n-button type="info"  @click="Golink" dashed>Take me to Article Page</n-button></div>


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
      <n-back-top :right="100" />
      <n-scrollbar style="max-height: 800px;">
      {{content}}
      </n-scrollbar>
    </n-list-item>
  </n-list>

  </div>

</template>


<script>
import { SearchSharp } from '@vicons/ionicons5'
import service from "../utils/network";
//import {ref} from "vue";
//    <n-button @click="GetDetail">点它</n-button>
import {computed } from 'vue'
export default {
  name: "DetailPage",
  components:{
    SearchSharp
  },

  data() {
    return {
      id : computed(() => this.$route.params.id),
      title: "",
      content: "",
      authors: [],
      abstract : "",
      url: ""
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
     this.url = resp.url
   },
    GoHome(){
     this.$router.push({
			path: '/'
		});
    },
    Golink(){
     window.open(this.url);
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
.main{
  margin-right: 100px;
  margin-left: 100px;
}

.title{

  margin-right: 50px;
  margin-left: 50px;
}
</style>