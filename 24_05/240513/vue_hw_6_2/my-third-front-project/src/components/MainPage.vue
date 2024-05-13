<!-- components/MainPage.vue -->
<template>
  <div>
    <h1>router 연습하기</h1>
    <router-link to="/">첫 페이지</router-link>
    <router-link to="/other">이동한 페이지</router-link>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MainPage',
});
</script>
