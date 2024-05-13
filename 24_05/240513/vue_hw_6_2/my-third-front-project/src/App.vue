<!-- App.vue -->
<template>
  <div>
    <!-- router-view는 현재 URL에 따라 해당하는 컴포넌트를 렌더링하는 역할을 합니다. -->
    <MainPage />
    <router-view />
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
});
</script>
