// views/StudentViews.vue
<template>
  <div>
    <h1>학생 목록</h1>
    <ul>
      <li v-for="student in students" :key="student.name" @click="goToStudentDetail(student.name)">
        {{ student.name }} 학생 정보 보기
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      students: [
        { name: '김하나' },
        { name: '김두리' },
        { name: '김서이' }
      ]
    };
  },
  methods: {
    goToStudentDetail(name) {
      this.$router.push({ name: 'StudentDetailView', params: { name: name } });
    }
  }
};
</script>
