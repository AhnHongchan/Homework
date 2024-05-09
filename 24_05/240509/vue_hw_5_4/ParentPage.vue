<template>
    <div class="h2-box">
      <h2>부모 페이지입니다.</h2>
      <div v-for="(child, index) in children" :key="index">
        <ChildPage :child="child" @giveMeAllowance="updateBalance(child)" />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import ChildPage from './ChildPage.vue';
  
  const children = ref([
    { name: '김하나', age: 30, balance: 100000 },
    { name: '김두리', age: 20, balance: 10000 },
    { name: '김서이', age: 10, balance: 1000 },
  ]);
  
  const updateBalance = (child) => {
    child.balance += 2000;
  };
  </script>
  
  
<style>
    .h2-box {
        display: inline-block;
        border: 2px solid #7dad30;
        padding: 10px 20px;
        border-radius: 5px;
        background-color: #f0f0f080;
        width: 95%;
    }
</style>