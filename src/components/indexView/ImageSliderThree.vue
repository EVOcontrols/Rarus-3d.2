<template>
  <div
    @touchstart.stop.prevent="touchHandler"
    @touchmove.stop.prevent="moveHandler"
    @touchend="endHandler"
    class="absolute  top-0 bottom-0 left-0 right-0">
    <Transition name="fade">
      <img
        :src="images[theme][imageIndex]?.src"
        :key="theme"
        class="absolute m-auto top-0 bottom-0 left-0 right-0 h-full"
        alt="">
    </Transition>
    <!-- <div class=" absolute top-2 left-2 text-red-700">
      {{ `x: ${testDiffX}, y: ${testDiffY}` }}
    </div> -->
  </div>
</template>

<script setup lang="ts">
import { useStore } from '@/stores/index';
import { storeToRefs } from 'pinia';
import { ref, watch } from 'vue';

const props = defineProps({
  nextSlideTrigger: {
    type: Number,
    required: true,
  },
});

const store = useStore();

const { theme } = storeToRefs(store);

const images = ref<{ dark: HTMLImageElement[], light: HTMLImageElement[] }>({
  dark: [],
  light: [],
});

const imageIndex = ref(0);

const viewWidth = document.body.clientWidth;

const slideNum = ref(0);

const touchStartX = ref(0);

let touchStartY = 0;

let isTouch = false;

let direction: 'left' | 'right' = 'left';

let moveTimer: ReturnType<typeof setTimeout> | undefined;

let isHorizontalMoving: boolean | undefined;

// const testDiffX = ref(0);

// const testDiffY = ref(0);

// async function loadImages() {
//   new Array(73).fill(null).reduce((acc, v, i) => (
//     acc.then(() => new Promise((res) => {
//       const image = new Image();
//       image.onload = () => {
//         images.value.push(image);
//         res(null);
//       };
//       image.src = `/slides/white/${10000 + i}.jpg`;
//     }))
//   ), Promise.resolve(null));
// }

async function loadImages() {
  const promises: Promise<null>[] = [];
  (['dark', 'light'] as const).forEach((type) => {
    new Array(73).fill(null).forEach((v, i) => {
      const promise = new Promise<null>((res) => {
        const image = new Image();
        image.onload = () => {
          images.value[type][i] = image;
          res(null);
        };
        image.src = `/slides/${type}/${10000 + i}.jpg`;
      });
      promises.push(promise);
    });
  });
  await Promise.all(promises);
}

await loadImages();

function touchHandler(e: TouchEvent) {
  if (moveTimer) clearTimeout(moveTimer);
  isTouch = true;
  touchStartX.value = e.touches[0].clientX;
  touchStartY = e.touches[0].clientY;
}

function moveHandler(e: TouchEvent) {
  if (isHorizontalMoving === false) return;
  if (isHorizontalMoving === undefined) {
    const diffX = touchStartX.value - e.touches[0].clientX;
    const diffY = touchStartY - e.touches[0].clientY;
    // testDiffX.value = Math.abs(diffX);
    // testDiffY.value = Math.abs(diffY);
    if (Math.abs(diffY) > Math.abs(diffX)) {
      if (diffX < 1) return;
      isHorizontalMoving = false;
      return;
    }
    isHorizontalMoving = true;
  }
  direction = touchStartX.value > e.touches[0].clientX ? 'left' : 'right';
  const progress = (touchStartX.value - e.touches[0].clientX) / viewWidth;
  const index = Math.round((progress + slideNum.value) * 24);
  if (index < 0) {
    imageIndex.value = 0;
  } else if (index > 72) {
    imageIndex.value = 72;
  } else {
    imageIndex.value = index;
  }
}

function move(delay: number, index: number, increment: number) {
  if (isTouch) return;
  if (imageIndex.value === 72 || imageIndex.value === 0) return;
  imageIndex.value += increment;
  if (imageIndex.value !== index) {
    moveTimer = setTimeout(() => {
      move(delay, index, increment);
    }, delay);
  }
}

function endHandler() {
  isTouch = false;
  if (isHorizontalMoving === false) {
    isHorizontalMoving = undefined;
    return;
  }
  isHorizontalMoving = undefined;
  const increment = direction === 'left' ? 1 : -1;
  const targetSlideNum = slideNum.value + increment;
  const targetIndex = targetSlideNum * 24;
  if (targetIndex > 72 || targetIndex < 0) return;
  if (imageIndex.value === 72 || imageIndex.value === 0) return;
  move(300 / 24, targetIndex, increment);
  slideNum.value = targetSlideNum;
}

watch(() => props.nextSlideTrigger, () => {
  if (imageIndex.value === 72) return;
  direction = 'left';
  imageIndex.value += 1;
  endHandler();
});
</script>
