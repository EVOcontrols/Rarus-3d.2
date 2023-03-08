<template>
  <div
    @touchstart="touchHandler"
    @touchmove="moveHandler"
    @touchend="endHandler"
    class="absolute top-0 bottom-0 left-0 right-0">
    <Transition name="fade">
      <div
        class="absolute top-0 bottom-0 left-0 right-0"
        v-show="theme === 'dark'">
        <img
          v-for="(img, i) in images.dark"
          :src="img"
          :key="`dark${i}`"
          class=" absolute h-full w-full object-cover"
          :class="{
            invisible: i !== imageIndex,
          }"
          alt="">
      </div>
    </Transition>
    <Transition name="fade">
      <div
        class="absolute top-0 bottom-0 left-0 right-0"
        v-show="theme === 'light'">
        <img
          v-for="(img, i) in images.light"
          :src="img"
          :key="`dark${i}`"
          class="absolute h-full w-full object-cover"
          :class="{
            invisible: i !== imageIndex,
          }"
          alt="">
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { useStore } from '@/stores/index';
import { storeToRefs } from 'pinia';
import { ref, watch, type PropType } from 'vue';

const props = defineProps({
  nextSlideTrigger: {
    type: Number,
    required: true,
  },
  images: {
    type: Object as PropType<{ dark: string[], light: string[] }>,
    required: true,
  },
  imageCount: {
    type: Number,
    required: true,
  },
  pageNum: {
    type: Number,
    required: true
  }
});

const store = useStore();

const { theme } = storeToRefs(store);

const imageIndex = ref(0);

const viewWidth = document.body.clientWidth;

const slideNum = ref(0);

const touchStartX = ref(0);

let touchStartY = 0;

let isTouch = false;

let direction: 'left' | 'right' = 'left';

let moveTimer: ReturnType<typeof setTimeout> | undefined;

let isHorizontalMoving: boolean | undefined;

const isMoving = ref(false);

const lastImageIndex = props.imageCount - 1;

function touchHandler(e: TouchEvent) {
  if (isMoving.value) return;
  isMoving.value = true;
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
  } else if (index > lastImageIndex) {
    imageIndex.value = lastImageIndex;
  } else {
    imageIndex.value = index;
  }
}

function move(delay: number, index: number, increment: number) {
  const shouldStop = isTouch || imageIndex.value === lastImageIndex || imageIndex.value === 0;
  if (shouldStop) {
    isMoving.value = false;
    return;
  }
  imageIndex.value += increment;
  if (imageIndex.value !== index) {
    moveTimer = setTimeout(() => {
      move(delay, index, increment);
    }, delay);
  } else {
    setTimeout(() => {
      isMoving.value = false;
    }, 100);
  }
}

function endHandler() {
  isTouch = false;
  if (isHorizontalMoving === false) {
    isHorizontalMoving = undefined;
    isMoving.value = false;
    return;
  }
  isHorizontalMoving = undefined;
  const increment = direction === 'left' ? 1 : -1;
  const targetSlideNum = slideNum.value + increment;
  const targetIndex = targetSlideNum * 24;
  const doNoNeedToMoveFurther = targetIndex > lastImageIndex
    || targetIndex < 0
    || imageIndex.value === lastImageIndex
    || imageIndex.value === 0;
  if (doNoNeedToMoveFurther) {
    isMoving.value = false;
    return;
  }
  move(300 / 24, targetIndex, increment);
  slideNum.value = targetSlideNum;
}

watch(() => props.nextSlideTrigger, () => {
  if (imageIndex.value === lastImageIndex) return;
  direction = 'left';
  imageIndex.value += 1;
  endHandler();
});
</script>
