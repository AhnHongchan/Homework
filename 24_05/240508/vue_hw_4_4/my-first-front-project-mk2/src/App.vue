<template>
  <div id="app">
    <ColorChanger />
  </div>
</template>

<script>
import ColorChanger from './components/ColorChanger.vue';

export default {
  components: {
    ColorChanger
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
