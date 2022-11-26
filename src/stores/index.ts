import { ref } from 'vue';
import { defineStore } from 'pinia';

// eslint-disable-next-line import/prefer-default-export
export const useStore = defineStore('index', () => {
  let initialTheme: 'light' | 'dark' = (['light', 'dark'] as const).includes(localStorage.theme)
    ? localStorage.theme
    : undefined;
  if (!initialTheme) {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      initialTheme = 'dark';
    } else {
      initialTheme = 'light';
    }
  }
  const theme = ref<'dark' | 'light'>(initialTheme);

  function toggleTheme() {
    theme.value = theme.value === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', theme.value);
  }

  return {
    theme,
    toggleTheme,
  };
});
