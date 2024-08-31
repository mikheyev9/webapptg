<script lang="ts">

import { defineComponent, ref, computed, onMounted } from 'vue';
import { VueScrollPicker } from 'vue-scroll-picker';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default defineComponent({
  components: {
    VueScrollPicker,
  },
  setup() {
    const router = useRouter();

    const currentYear = ref(new Date().getFullYear().toString());
    const currentMonth = ref("1");
    const currentDay = ref("1");
    const errorMessage = ref<string | null>(null);
    const telegramWebApp = window.Telegram.WebApp;
    const apiUrl = import.meta.env.VITE_API_URL;
    const isLoading = ref(false)

    const years = computed(() => {
      const currYear = new Date().getFullYear();
      const startYear = 1900;
      return Array.from({ length: currYear - startYear + 1 }, (_, index) => ({
        name: (startYear + index).toString(),
        value: (startYear + index).toString()
      })).reverse();
    });

    const months = computed(() => [
      { name: 'Январь', value: '1' },
      { name: 'Февраль', value: '2' },
      { name: 'Март', value: '3' },
      { name: 'Апрель', value: '4' },
      { name: 'Май', value: '5' },
      { name: 'Июнь', value: '6' },
      { name: 'Июль', value: '7' },
      { name: 'Август', value: '8' },
      { name: 'Сентябрь', value: '9' },
      { name: 'Октябрь', value: '10' },
      { name: 'Ноябрь', value: '11' },
      { name: 'Декабрь', value: '12' },
    ]);

    const days = computed(() => {
      const lastDay = new Date(parseInt(currentYear.value), parseInt(currentMonth.value), 0).getDate();
      return Array.from({ length: lastDay }, (_, index) => ({
        name: (index + 1).toString(),
        value: (index + 1).toString()
      }));
    });

    const generateRandomUsername = (firstName: string) => {
      const randomNum = Math.floor(Math.random() * 10000);
      return `${firstName.toLowerCase()}_${randomNum}`;
    };

    onMounted(() => {
      telegramWebApp.ready();

      const startParam = window.Telegram.WebApp.initDataUnsafe.start_param;

      if (startParam) {
        const username = startParam;
        router.push({
          path: '/profile',
          query: { username },
        });
      } else {
        console.log('Параметр start_param отсутствует');
      }

      if (telegramWebApp.themeParams.bg_color) {
        document.body.style.backgroundColor = telegramWebApp.themeParams.bg_color;
      }

      if (!telegramWebApp.isExpanded) {
        telegramWebApp.expand();
      }

      if (!telegramWebApp.initDataUnsafe || !telegramWebApp.initDataUnsafe.user) {
        errorMessage.value = 'Не удалось получить данные пользователя из Telegram. Проверьте, что ваше приложение запущено в Telegram.';
      }

    });

    const submitDate = async () => {
      const selectedDate = new Date(parseInt(currentYear.value), parseInt(currentMonth.value) - 1, parseInt(currentDay.value));

      try {
        isLoading.value = true; // Включаем спиннер
        const telegramUser = telegramWebApp.initDataUnsafe?.user;

        if (!telegramUser) {
          errorMessage.value = 'Не удалось получить данные пользователя из Telegram. Проверьте, что ваше приложение запущено в Telegram.';
          console.log('Telegram WebApp initDataUnsafe:', telegramWebApp.initDataUnsafe);
          return;
        }

        let username = telegramUser.username;
        if (!username) {
          // Генерация никнейма на основе имени пользователя и случайного числа
          username = generateRandomUsername(telegramUser.first_name);
          console.log('Сгенерированный никнейм:', username);
        }

        await axios.post(`${apiUrl}/api/users/`, {
          first_name: telegramUser.first_name,
          last_name: telegramUser.last_name,
          username: username,
          birth_date: selectedDate.toISOString(),
        });

        router.push({
          path: '/profile',
          query: { username: username }
        });
      } catch (error) {
        console.error('Ошибка при отправке данных:', error);
        errorMessage.value = 'Ошибка при отправке данных.';
      } finally {
        isLoading.value = false; // Отключаем спиннер
      }
    };

    return {
      currentYear,
      currentMonth,
      currentDay,
      years,
      months,
      days,
      submitDate,
      errorMessage,
      isLoading
    };
  },
});

</script>

<template>

  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50">
    <h1 class="text-3xl text-center font-extrabold mb-4 text-indigo-600">Введите свою дату рождения</h1>
    <div class="picker-group flex flex-row justify-center items-center w-full max-w-lg space-x-4 mb-4">
      <VueScrollPicker
          :options="days"
          v-model="currentDay"
          class="flex-1 text-center bg-white rounded-lg shadow-md"
          style="height: 60vh; font-size: 2.5rem;"
          active-style="color: black; font-size: 2.5rem;"
          inactive-style="color: black; font-size: 2.5rem;"
      />
      <VueScrollPicker
          :options="months"
          v-model="currentMonth"
          class="flex-1 text-center bg-white rounded-lg shadow-md"
          style="height: 60vh; font-size: 1.5rem;"
          active-style="color: black; font-size: 2rem;"
          inactive-style="color: black; font-size: 1.5rem;"
      />
      <VueScrollPicker
          :options="years"
          v-model="currentYear"
          class="flex-1 text-center bg-white rounded-lg shadow-md"
          style="height: 60vh; font-size: 2.5rem;"
          active-style="color: black; font-size: 2.5rem;"
          inactive-style="color: black; font-size: 2.5rem;"
      />
    </div>
    <div class="text-center mt-4">
      <button @click="submitDate" :disabled="isLoading" class="px-8 py-3 bg-indigo-500 text-white font-semibold rounded-lg hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed">
        <div v-if="isLoading" class="w-6 h-6 border-4 border-t-4 border-gray-200 border-t-white rounded-full animate-spin mx-auto"></div>
        <span v-else>Продолжить</span>
      </button>
    </div>
    <p v-if="errorMessage" class="text-red-500 text-center mt-4">{{ errorMessage }}</p>
  </div>
</template>

<style scoped>

.picker-group {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 100%; /* Убрано, чтобы не занимало всю высоту экрана */
}
.picker-group .VueScrollPicker {
  font-size: 2.5rem; /* Уменьшен размер шрифта */
}
.btn {
  padding: 10px 20px;
  background-color: #4f46e5;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn:hover {
  background-color: #4338ca;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 120px;
}
</style>
