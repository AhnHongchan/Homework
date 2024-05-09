<template>
    <div class ="h2-box">
      <h2>부모 페이지입니다.</h2>
      <div v-for="(child, index) in children" :key="index">
        <ChildPage :child="child" />
      </div>
    </div>
  </template>
  
  <script>
  import ChildPage from "./ChildPage.vue";
  
  export default {
    name: "ParentPage",
    components: {
      ChildPage,
    },
    data() {
      return {
        children: [
          { name: "김하나", age: 30 },
          { name: "김두리", age: 20 },
          { name: "김서이", age: 10 },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .child-container {
    margin-bottom: 10px;
  }

  .h2-box {
    display: inline-block;
    border: 2px solid #7dad30;
    padding: 10px 20px;
    border-radius: 5px;
    background-color: #f0f0f080;
    width: 95%;
    }
  </style>