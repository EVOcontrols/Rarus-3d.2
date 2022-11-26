<template>
  <Swiper
    ref="swiperEl"
    class=" !absolute  top-0 bottom-0 left-0 right-0"
    @progress="progressHandler"
  >
    <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide>
    <swiper-slide>Slide 3</swiper-slide>
    <swiper-slide>Slide 4</swiper-slide>
    <img
      :src="images[index]?.src"
      class="absolute m-auto top-0 bottom-0 left-0 right-0 w-full"
      alt="">
  </Swiper>
</template>

<script setup lang="ts">
import { Swiper, SwiperSlide, useSwiper } from 'swiper/vue';

import 'swiper/css';
import { ref, watch } from 'vue';

const props = defineProps({
  nextSlideTrigger: {
    type: Number,
    required: true,
  },
});

const images = ref<HTMLImageElement[]>([]);

const index = ref(0);

const swiper = useSwiper();

watch(() => props.nextSlideTrigger, () => {
  swiper.value.slideNext();
});

async function loadImages() {
  new Array(73).fill(null).reduce((acc, v, i) => (
    acc.then(() => new Promise((res) => {
      const image = new Image();
      image.onload = () => {
        images.value.push(image);
        res(null);
      };
      image.src = `/slides/white/${10000 + i}.jpg`;
    }))
  ), Promise.resolve(null));
}

await loadImages();

function progressHandler(e: any, progress: number) {
  const newIndex = Math.round((72 * progress));
  if (newIndex > 72 || newIndex < 0) {
    console.log(newIndex);
    return;
  }
  index.value = newIndex;
}
</script>
