<template>
  <div
    class=" w-full h-full bg-[#eaeaea] dark:bg-[#070707]"
  >
    <div
      class=" w-full h-full flex flex-col justify-between"
    >
      <Transition name="fade" mode="out-in">
        <div
          v-if="!allImagesAreLoaded"
          class=" absolute left-0 right-0 top-0 bottom-0 h-1 my-auto mx-8 rounded
                overflow-hidden bg-[#d5d5d5] dark:bg-[#232222]"
        >
          <div
            class=" h-full bg-[#070707] dark:bg-[#eaeaea] transition-[width]"
            :style="{
              width: `${imagesLoadingProgress * 100}%`,
            }"
          />
        </div>
        <ImageSlider
          v-else
          :images="images"
          :image-count="imageCount"
          :next-slide-trigger="nextSlideTrigger"
        />
      </Transition>
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
        <Transition name="fade">
          <button
            v-if="allImagesAreLoaded"
            type="button"
            class="mr-10">
            <img
              src="@/assets/img/menu-lines.svg"
              class="h-2.5"
              alt="">
          </button>
        </Transition>
      </div>
      <Transition name="fade">
        <div
          v-if="allImagesAreLoaded"
          class="flex flex-row justify-between items-center mb-40 z-[1]">
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
      </Transition>
    </div>
  </div>
</template>

<script lang="ts" setup>
import ImageSlider from '@/components/indexView/ImageSlider.vue';
import ThemeSwitcher from '@/components/indexView/ThemeSwitcher.vue';
import { computed, ref } from 'vue';

const nextSlideTrigger = ref(0);

const imageCount = 73;

const images = ref<{ dark: string[], light: string[] }>({
  dark: [],
  light: [],
});

const allImagesAreLoaded = ref(false);

const imagesLoadingProgress = computed(() => (
  (images.value.dark.length + images.value.light.length) / (imageCount * 2)
));

async function loadImages() {
  const promises: Promise<null>[] = [];
  (['dark', 'light'] as const).forEach((type) => {
    new Array(imageCount).fill(null).forEach((v, i) => {
      const promise = new Promise<null>((res) => {
        fetch(`/slides/full-size/${type}/${10000 + i}.jpg`)
          .then((response) => response.blob())
          .then((blob) => {
            images.value[type][i] = URL.createObjectURL(blob);
            res(null);
          });
      });
      promises.push(promise);
    });
  });
  await Promise.all(promises);
  allImagesAreLoaded.value = true;
}

loadImages();
</script>
