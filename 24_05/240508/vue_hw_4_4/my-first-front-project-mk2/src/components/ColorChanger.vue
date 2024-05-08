<template>
    <div>
      <input type="text" v-model="colorClassInput" @input="changeColor">
      <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        colorClassInput: '',
        colorClass: ''
      };
    },
    methods: {
      changeColor() {
        if (['red', 'blue', 'green'].includes(this.colorClassInput)) {
          this.colorClass = this.colorClassInput;
        } else {
          this.colorClass = '';
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .red {
    color: red;
  }
  
  .blue {
    color: blue;
  }
  
  .green {
    color: green;
  }
  </style>
  