<!-- views/OtherView.vue -->
<template>
  <MainPage>
  </MainPage>
  <hr>
  <div>
    <h1>이동한 페이지</h1>
    <!-- OtherView 고유의 내용 추가 -->
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import MainPage from '../components/MainPage.vue';

export default defineComponent({
  name: 'OtherView',
  components: {
    MainPage,
  },
});
</script>
