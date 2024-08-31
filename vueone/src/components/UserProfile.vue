<template>

  <div class="profile-container">
    <div v-if="isLoading" class="spinner"></div>
    <div v-else>
      <h2>Профиль пользователя</h2>
      <p><strong>Имя:</strong> {{ user.first_name }}</p>
      <p><strong>Фамилия:</strong> {{ user.last_name }}</p>
      <p><strong>Юзернейм:</strong> {{ user.username }}</p>
      <p><strong>До дня рождения:</strong> {{ timeUntilBirthday }}</p>

      <button @click="shareProfile" class="btn btn-primary">Поделиться</button>
    </div>
  </div>

</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

export default defineComponent({
  setup() {
    const isLoading = ref(true);
    const route = useRoute();
    const user = ref({
      first_name: '',
      last_name: '',
      username: '',
    });
    const timeUntilBirthday = ref('');
    const apiUrl = import.meta.env.VITE_API_URL;

    const fetchUserData = async () => {
      const username = route.query.username as string;

      try {
        const response = await axios.get(`${apiUrl}/api/users/${username}/`);
        user.value = response.data;
        timeUntilBirthday.value = `${response.data.time_until_birthday.days} дней,
                                   ${response.data.time_until_birthday.hours} часов,
                                   ${response.data.time_until_birthday.minutes} минут`;
      } catch (error) {
        console.error('Ошибка при получении данных пользователя:', error);
      } finally {
        isLoading.value = false; // Отключаем состояние загрузки после получения данных
      }
    };


    const generateInlineQuery = (username: string) => {
      return `profile=${username}`;
    };

    const shareProfile = () => {
      const username = user.value.username;
      const inlineQuery = generateInlineQuery(username);
      try {
        // Пробуем отправить inline-запрос через Telegram WebApp
        Telegram.WebApp.switchInlineQuery(inlineQuery, ['users', 'groups', 'channels']);
      } catch (error) {
        // Если возникает ошибка, выполняем альтернативное действие
        const shareUrl = `${window.location.origin}/profile?username=${username}`;
        navigator.clipboard.writeText(shareUrl)
            .then(() => {
              alert('Ссылка скопирована в буфер обмена');
            })
            .catch(err => {
              console.error('Ошибка копирования ссылки:', err);
            });
        // Логирование ошибки для других возможных случаев
        console.error('Ошибка при попытке поделиться профилем:', error);
      }
    };


    onMounted(() => {
      fetchUserData();
    });

    return {
      user,
      timeUntilBirthday,
      shareProfile,
      isLoading
    };
  },
});
</script>

<style scoped>
.profile-container {
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 10px;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-top-color: #007bff;
  animation: spin 1s infinite linear;
  margin: 50px auto;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

.btn:hover {
  background-color: #0056b3;
}
</style>
