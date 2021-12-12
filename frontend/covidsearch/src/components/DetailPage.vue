<template>
  <div>
    <n-h1>{{title}}</n-h1>
    <n-divider />
    <n-tag type="success" v-for="author in authors" :key="author">
    {{author}}
    </n-tag>
    <n-p>
      {{content}}
    </n-p>

  </div>

</template>


<script>
import service from "../utils/network";
//import {ref} from "vue";
//    <n-button @click="GetDetail">点它</n-button>

export default {
  name: "DetailPage",
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