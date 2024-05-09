<template>
    <div class="child-container">
      <h3>자식 페이지입니다.</h3>
      <p>이름: {{ child.name }}</p>
      <p>나이: {{ child.age }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "ChildPage",
    props: {
      child: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  h3 {
    font-size: 20px;
    margin-bottom: 10px;
  }
  
  p {
    margin: 5px 0;
  }

  .child-container {
    display: inline-block;
    border: 2px solid #c6f877;
    padding: 10px 20px;
    border-radius: 5px;
    background-color: #504e4e80;
    width: 95%;
    }
  </style>
  