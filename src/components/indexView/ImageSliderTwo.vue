<template>
  <Splide
    class="!absolute  top-0 bottom-0 left-0 right-0"
    :options="{ rewind: true }"
    @splide:dragging="dragging"
    aria-label="My Favorite Images">
    <SplideSlide>
      Slide 1
    </SplideSlide>
    <SplideSlide>
      Slide 2
    </SplideSlide>
  </Splide>
</template>

<script setup lang="ts">
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/vue-splide/css/core';

function dragging(e: any) {
  console.log(e);
}
</script>
