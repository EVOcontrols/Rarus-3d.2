<template>
  <div
    class=" w-full h-full bg-[#eaeaea] dark:bg-[#070707]"
  >
    <Suspense>
      <div
        class=" w-full h-full flex flex-col justify-between"
      >
        <ImageSliderThree :next-slide-trigger="nextSlideTrigger" />
        <div
          class="flex flex-row justify-between items-center mt-16 z-[1]">
          <h1 class="text-xl leading-5 pl-8">
            <span class="text-black dark:text-white">
              FX3D
            </span>
            <span class="text-[#5B5F65] block">
              DESIGN
            </span>
          </h1>
          <button type="button" class="mr-10">
            <img
              src="@/assets/img/menu-lines.svg"
              class="h-2.5"
              alt="">
          </button>
        </div>
        <div class="flex flex-row justify-between items-center mb-40 z-[1]">
          <ThemeSwitcher class="ml-8" />
          <button
            @click="nextSlideTrigger = Math.random()"
            type="button"
            class="mr-7 p-4">
            <img
              src="@/assets/img/arrow-right.svg"
              class="h-5"
              alt="">
          </button>
        </div>
      </div>
    </Suspense>
  </div>
</template>

<script lang="ts" setup>
// import ImageSlider from '@/components/indexView/ImageSlider.vue';
// import ImageSliderTwo from '@/components/indexView/ImageSliderTwo.vue';
import ImageSliderThree from '@/components/indexView/ImageSliderThree.vue';
import ThemeSwitcher from '@/components/indexView/ThemeSwitcher.vue';
import { ref } from 'vue';

const nextSlideTrigger = ref(0);
</script>
