<template>
  <button
    type="button"
    class="theme-toggle"
    id="theme-toggle"
    title="Toggles light & dark"
    aria-label="auto"
    aria-live="polite"
    @click="store.toggleTheme()">
    <svg class="sun-and-moon" aria-hidden="true" width="24" height="24" viewBox="0 0 24 24">
      <mask class="moon" id="moon-mask">
        <rect x="0" y="0" width="100%" height="100%" fill="white" />
        <circle cx="24" cy="10" r="6" fill="black" />
      </mask>
      <circle class="sun" cx="12" cy="12" r="6" mask="url(#moon-mask)" fill="currentColor" />
      <g class="sun-beams" stroke="currentColor">
        <line x1="12" y1="1" x2="12" y2="3" />
        <line x1="12" y1="21" x2="12" y2="23" />
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
        <line x1="1" y1="12" x2="3" y2="12" />
        <line x1="21" y1="12" x2="23" y2="12" />
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
      </g>
    </svg>
  </button>
</template>

<script setup lang="ts">
import { useStore } from '@/stores/index';

const store = useStore();
</script>

<style lang="postcss">
:where(html){--ease-1:cubic-bezier(.25,0,.5,1);--ease-2:cubic-bezier(.25,0,.4,1);--ease-3:cubic-bezier(.25,0,.3,1);--ease-4:cubic-bezier(.25,0,.2,1);--ease-5:cubic-bezier(.25,0,.1,1);--ease-in-1:cubic-bezier(.25,0,1,1);--ease-in-2:cubic-bezier(.50,0,1,1);--ease-in-3:cubic-bezier(.70,0,1,1);--ease-in-4:cubic-bezier(.90,0,1,1);--ease-in-5:cubic-bezier(1,0,1,1);--ease-out-1:cubic-bezier(0,0,.75,1);--ease-out-2:cubic-bezier(0,0,.50,1);--ease-out-3:cubic-bezier(0,0,.3,1);--ease-out-4:cubic-bezier(0,0,.1,1);--ease-out-5:cubic-bezier(0,0,0,1);--ease-in-out-1:cubic-bezier(.1,0,.9,1);--ease-in-out-2:cubic-bezier(.3,0,.7,1);--ease-in-out-3:cubic-bezier(.5,0,.5,1);--ease-in-out-4:cubic-bezier(.7,0,.3,1);--ease-in-out-5:cubic-bezier(.9,0,.1,1);--ease-elastic-1:cubic-bezier(.5,.75,.75,1.25);--ease-elastic-2:cubic-bezier(.5,1,.75,1.25);--ease-elastic-3:cubic-bezier(.5,1.25,.75,1.25);--ease-elastic-4:cubic-bezier(.5,1.5,.75,1.25);--ease-elastic-5:cubic-bezier(.5,1.75,.75,1.25);--ease-squish-1:cubic-bezier(.5,-.1,.1,1.5);--ease-squish-2:cubic-bezier(.5,-.3,.1,1.5);--ease-squish-3:cubic-bezier(.5,-.5,.1,1.5);--ease-squish-4:cubic-bezier(.5,-.7,.1,1.5);--ease-squish-5:cubic-bezier(.5,-.9,.1,1.5);--ease-step-1:steps(2);--ease-step-2:steps(3);--ease-step-3:steps(4);--ease-step-4:steps(7);--ease-step-5:steps(10)}

.sun-and-moon>:is(.moon,.sun,.sun-beams) {
    transform-origin: center center;
}

.sun-and-moon>:is(.moon,.sun) {
    fill: var(--icon-fill);
}

.theme-toggle:is(:hover,:focus-visible)>.sun-and-moon>:is(.moon,.sun) {
    fill: var(--icon-fill-hover);
}

.sun-and-moon>.sun-beams {
    stroke: var(--icon-fill);
    stroke-width: 2px;
}

.theme-toggle:is(:hover,:focus-visible) .sun-and-moon>.sun-beams {
    stroke: var(--icon-fill-hover)
}

.dark .sun-and-moon>.sun {
    transform: scale(1.75);
}

.dark .sun-and-moon>.sun-beams {
    opacity: 0;
}

.dark .sun-and-moon>.moon>circle {
    transform: translate(-7px);
}

@supports (cx: 1) {
    .dark .sun-and-moon>.moon>circle {
        transform: translate(0);
        cx: 17;
    }
}

@media (prefers-reduced-motion: no-preference) {
    .sun-and-moon>.sun {
        transition: transform .5s var(--ease-elastic-3);
    }

    .sun-and-moon>.sun-beams {
        transition: transform .5s var(--ease-elastic-4),opacity .5s var(--ease-3);
    }

    .sun-and-moon .moon>circle {
        transition: transform .25s var(--ease-out-5);
    }

    @supports (cx: 1) {
        .sun-and-moon .moon>circle {
            transition: cx .25s var(--ease-out-5);
        }
    }

    .dark .sun-and-moon>.sun {
        transform: scale(1.75);
        transition-timing-function: var(--ease-3);
        transition-duration: .25s;
    }

    .dark .sun-and-moon>.sun-beams {
        transform: rotate(-25deg);
        transition-duration: .15s;
    }

    .dark .sun-and-moon>.moon>circle {
        transition-delay: .25s;
        transition-duration: .5s;
    }
}

.theme-toggle {
    --size: 2rem;
    --icon-fill: hsl(210 10% 30%);
    --icon-fill-hover: hsl(210 10% 15%);
    background: none;
    border: none;
    padding: 0;
    inline-size: var(--size);
    block-size: var(--size);
    aspect-ratio: 1;
    border-radius: 50%;
    cursor: pointer;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    outline-offset: 5px;
}

.theme-toggle>svg {
    inline-size: 100%;
    block-size: 100%;
    stroke-linecap: round;
}

.dark .theme-toggle {
    --icon-fill: hsl(210 10% 70%);
    --icon-fill-hover: hsl(210 15% 90%);
}

@media (hover: none) {
    .theme-toggle {
        --size: 1.875rem;
    }
}
</style>
