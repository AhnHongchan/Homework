<!-- components/MainPage.vue -->
<template>
  <div>
    <h1>router 연습하기</h1>
    <router-link to="/">some</router-link>
     | <router-link to="/other">other</router-link>
     | <router-link to ="/students">students</router-link>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MainPage',
});
</script>
