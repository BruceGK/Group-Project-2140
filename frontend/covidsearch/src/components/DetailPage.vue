<template>
  <div>
  <h1>Detail Page of the search result</h1>
    <n-divider />
    <n-h1>{{title}}</n-h1>
    <n-p>
    {{content}}
    </n-p>
    <button @click="GetDetail">Greet</button>
  </div>
</template>


<script>
import service from "../utils/network";
import {ref} from "vue";

export default {
  name: "DetailPage",
  props: {
    id: String
  },
  data() {
    return {
      title : "金瓶梅",
      content : "《金瓶梅》，中国明代长篇白话世情小说，一般认为是中国第一部文人独立创作的章回体长篇小说。" +
          "其成书时间大约在明代隆庆至万历年间，作者署名兰陵笑笑生。《金瓶梅》书名由书中三个女主人公潘金莲、李瓶儿、" +
          "庞春梅名字中各取一字合成。小说题材由《水浒传》中武松杀嫂一段演化而来，通过对兼有官僚、恶霸、" +
          "富商三种身份的市侩势力代表人物西门庆及其家庭罪恶生活的描述，再现了当时社会民间生活的面貌，" +
          "描绘了一个上至朝廷擅权专政的太师，下至地方官僚恶霸乃至市井地痞、流氓、帮闲所构成的鬼蜮世界，" +
          "揭露了明代中叶社会的黑暗和腐败，具有深刻的认识价值。"

    }
  },
  setup() {
    const queryStr = ref("");
    const GetDetail = async () => {
      console.log(queryStr.value);
      const resp = await service({
        method: "get",
        url: "https://2140.miguch.com/api/details/",
        params: {
          q: "banzkms3",
        },
      });
      console.log(resp);
    };
    return {
      queryStr,
      GetDetail,
    };
  },
}
</script>

<style scoped>

</style>