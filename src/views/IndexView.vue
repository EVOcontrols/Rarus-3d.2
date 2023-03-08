<template>
  <div class="w-full h-full bg-[#eaeaea] dark:bg-[#070707]">
    <div class="w-full h-full flex flex-col justify-between">
      <div
        class="absolute top-0 left-0 h-full w-full overflow-y-auto snap-y snap-mandatory flex flex-col"
        ref="scrollEl"
        @touchstart="touchStartHandler"
        @touchend="touchendHandler"
      >
        <div
          v-for="p in pages"
          :key="p"
          class="relative h-full w-full shrink-0 snap-center"
        >
          <Transition
            name="fade"
            mode="out-in"
          >
            <div
              v-if="imagesLoadingStatus.get(p) !== 'loaded'"
              class="absolute left-0 right-0 top-0 bottom-0 h-1 my-auto mx-8 rounded overflow-hidden bg-[#d5d5d5] dark:bg-[#232222]"
            >
              <div
                class="h-full bg-[#070707] dark:bg-[#eaeaea] transition-[width]"
                :style="{
                  width: `${imagesLoadingProgress[p] * 100}%`,
                }"
              />
            </div>
            <ImageSlider
              v-else
              :images="images[p]"
              :image-count="imageCount[p]"
              :next-slide-trigger="nextSlideTrigger"
              :page-num="p"
            />
          </Transition>
        </div>
      </div>
      <div class="flex flex-row justify-between items-center mt-8 z-[1]">
        <h1 class="text-xl leading-5 pl-8">
          <span class="text-black dark:text-white"> FX3D </span>
          <span class="text-[#5B5F65] block"> DESIGN </span>
        </h1>
        <Transition name="fade">
          <button
            v-show="[...imagesLoadingStatus.values()].some((s) => s === 'loaded')"
            type="button"
            class="mr-10"
          >
            <img
              src="@/assets/img/menu-lines.svg"
              class="h-2.5"
              alt=""
            />
          </button>
        </Transition>
      </div>
      <Transition name="fade">
        <button
          v-if="imagesLoadingStatus.get(currentPage) === 'loaded'"
          @click="nextSlideTrigger = Math.random()"
          type="button"
          class="p-4 absolute bottom-[1.31rem] z-[1] right-7"
        >
          <img
            src="@/assets/img/arrow-right.svg"
            class="h-5"
            alt=""
          />
        </button>
      </Transition>
      <Transition name="fade">
        <ThemeSwitcher
          v-if="imagesLoadingStatus.get(currentPage) === 'loaded'"
          class="absolute left-8 bottom-8"
        />
      </Transition>
    </div>
  </div>
</template>

<script lang="ts" setup>
import ImageSlider from '@/components/indexView/ImageSlider.vue';
import ThemeSwitcher from '@/components/indexView/ThemeSwitcher.vue';
import { computed, ref, watch } from 'vue';

const nextSlideTrigger = ref(0);

const pages: [1, 2] = [1, 2];

type PageNum = (typeof pages)[number];

const currentPage = ref<PageNum>(1);

const imageCount: Record<PageNum, number> = { 1: 73, 2: 145 };

const images = ref<Record<PageNum, { dark: string[]; light: string[] }>>({
  1: {
    dark: [],
    light: [],
  },
  2: {
    dark: [],
    light: [],
  },
});

const imagesLoadingStatus = ref<Map<PageNum, 'loading' | 'loaded'>>(new Map());

const imagesLoadingProgress = computed(() =>
  pages.reduce((acc, p) => {
    const progress =
      (images.value[p].dark.length + images.value[p].light.length) / (imageCount[p] * 2);
    return { ...acc, [p]: progress };
  }, {} as Record<PageNum, number>)
);

const scrollEl = ref<HTMLElement | undefined>();

let touchEndTimer: ReturnType<typeof setTimeout> | undefined;

async function loadImages(pageNum: PageNum) {
  if (imagesLoadingStatus.value.has(pageNum)) return;
  imagesLoadingStatus.value.set(pageNum, 'loading');
  const promises: Promise<null>[] = [];
  (['dark', 'light'] as const).forEach((type) => {
    new Array(imageCount[pageNum]).fill(null).forEach((v, i) => {
      if (images.value[pageNum][type][i]) return;
      const promise = new Promise<null>((res) => {
        fetch(`/slides/page${pageNum}/medium-less/${type}/${10000 + i}.jpg`)
          .then((response) => response.blob())
          .then((blob) => {
            images.value[pageNum][type][i] = URL.createObjectURL(blob);
            res(null);
          });
      });
      promises.push(promise);
    });
  });
  await Promise.all(promises);
  imagesLoadingStatus.value.set(pageNum, 'loaded');
}

function touchStartHandler() {
  if (touchEndTimer) clearTimeout(touchEndTimer);
}

function touchendHandler() {
  const el = scrollEl.value;
  if (!el) return;
  touchEndTimer = setTimeout(() => {
    currentPage.value = el.scrollTop < window.innerHeight / 2 ? 1 : 2;
  }, 300);
}

watch(
  currentPage,
  () => {
    loadImages(currentPage.value);
  },
  { immediate: true }
);
</script>
