<template>
    <div class="child-container">
      <h3>자식 페이지입니다.</h3>
      <p>이름: {{ child.name }}</p>
      <p>나이: {{ child.age }}</p>
      <p>용돈: {{ child.balance }}</p>
      <button @click="requestAllowance">용돈 더 주세요</button>
    </div>
</template>
  
<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  child: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['giveMeAllowance']);

const requestAllowance = () => {
  emit('giveMeAllowance');
};
</script>


<style>
  .child-container {
    display: inline-block;
    border: 2px solid #c6f877;
    padding: 10px 20px;
    border-radius: 5px;
    background-color: #504e4e80;
    width: 95%;
    }
</style>
  