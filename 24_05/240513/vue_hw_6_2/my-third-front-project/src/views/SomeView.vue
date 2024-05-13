<!-- views/SomeView.vue -->
<template>
  <MainPage>
  </MainPage>
  <hr>
  <div>
    <h1>첫 페이지</h1>
    <!-- SomeView 고유의 내용 추가 -->
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import MainPage from '../components/MainPage.vue';

export default defineComponent({
  name: 'SomeView',
  components: {
    MainPage,
  },
});
</script>
