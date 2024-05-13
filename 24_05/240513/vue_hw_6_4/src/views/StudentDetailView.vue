// views/StudentDetailView.vue
<template>
  <div>
    <h1>학생 상세 정보</h1>
    <p>이름: {{ studentName }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      studentName: ''
    };
  },
  created() {
    this.studentName = this.$route.params.name;
  }
};
</script>
