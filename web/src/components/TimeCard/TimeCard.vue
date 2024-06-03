<template>
    <div class="clock">
        <div class="layer layer--img"></div>
        <div class="layer layer--shade"></div>
        <div class="layer layer--face">
            <div class="digits">
                <span class="digit-group" data-unit="h">{{ hours }}</span>
                <span>:</span>
                <span class="digit-group" data-unit="m">{{ minutes }}</span>
                <small class="digit-group digit-group--small" data-unit="s">{{ seconds }}</small>
                <small class="digit-group digit-group--small" data-unit="ap">{{ ampm }}</small>
            </div>
            <!-- <div class="hand hand--hr"></div>
            <div class="hand hand--min"></div>
            <div class="hand hand--sec"></div> -->
            <div class="ring"></div>
        </div>
        <div class="layer layer--profile">
            <img src="@/assets/imgs/timeBg.jpg" alt="Profile" class="profile">
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue';

const hours = ref('');
const minutes = ref('');
const seconds = ref('');
const ampm = ref('');
const secAngle = ref('');
const minAngle = ref('');
const hrAngle = ref('');

const updateClock = () => {
    const now = new Date();
    let h = now.getHours();
    const m = now.getMinutes();
    const s = now.getSeconds();

    const ap = h > 11 ? 'P' : 'A';
    if (h === 0) h += 12;
    else if (h > 12) h -= 12;

    hours.value = String(h).padStart(2, '0');
    minutes.value = String(m).padStart(2, '0');
    seconds.value = String(s).padStart(2, '0');
    ampm.value = ap;

    const secFraction = s / 60;
    const minFraction = (m + secFraction) / 60;
    const hrFraction = (h + minFraction) / 12;

    secAngle.value = `${360 * secFraction}deg`;
    minAngle.value = `${360 * minFraction}deg`;
    hrAngle.value = `${360 * hrFraction}deg`;
};

let timer: number;

onMounted(() => {
    updateClock();
    timer = window.setInterval(updateClock, 1000);
});

onBeforeUnmount(() => {
    clearInterval(timer);
});
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: hsl(223, 90%, 40%);
    color: hsl(0, 0%, 100%);
    font: 1em/1.5 Rubik, sans-serif;
    display: flex;
    height: 100vh;
    transition: background-color 0.3s, color 0.3s;
}

.clock {
    --hrAngle: 0;
    --minAngle: 0;
    --secAngle: 0;
    border-radius: 50%;
    margin: auto;
    outline: transparent;
    position: relative;
    width: 12em;
    height: 12em;
    transform: rotateX(30deg) rotateY(-30deg) rotateZ(30deg);
    transform-style: preserve-3d;
    transition: transform 0.3s cubic-bezier(0.42, 0, 0.58, 1);
}

.profile {
    background-color: hsl(223, 10%, 50%);
    border: 0;
    border-radius: 50%;
    box-shadow: 0 0 0 0.25em hsla(203, 74%, 83%, 0.511);
    display: block;
    margin: 7.75em auto 0 auto;
    width: 2em;
    height: 2em;
}

.clock:focus-visible,
.clock:hover {
    transform: rotateX(0) rotateY(0) rotateZ(0);
}

.digits {
    display: flex;
    justify-content: center;
    align-items: end;
    line-height: 1;
    margin-top: 2.25em;
    user-select: none;
}

.digit-group {
    margin: 0 0.1em;
    width: 2ch;
}

.digit-group[data-unit="h"] {
    text-align: right;
}

.digit-group--small {
    font-size: 0.75em;
}

.hand,
.layer,
.ring {
    position: absolute;
}

.hand {
    bottom: calc(50% - 0.5em);
    left: calc(50% - 0.5em);
    width: 1em;
    mix-blend-mode: difference;
    perspective: 4.25em;
    transform-origin: 0.5em calc(100% - 0.5em);
    transition: .5s;
}

.hand--hr {
    height: 2.75em;
    transform: rotate(var(--hrAngle)) translateY(-2em);
}

.hand--min {
    height: 3.75em;
    transform: rotate(var(--minAngle)) translateY(-2em);
}

.hand--sec {
    width: .5em;
    height: 3.75em;
    transform: rotate(var(--secAngle)) translateY(-2em);
}

.hand:before {
    background-color: hsl(0, 0%, 100%);
    content: "";
    display: block;
    width: 100%;
    height: 100%;
    transform: rotateX(-30deg);
    transform-origin: 50% 100%;
}

.hand--hr:before {
    border-radius: 0.5em 0.5em 0.5em 0.5em / 0.5em 0.5em 0.75em 0.75em;
}

.hand--min:before {
    border-radius: 0 0 0.5em 0.5em / 0 0 0.75em 0.75em;
}

.hand--sec:before {
    border-radius: 0 0 0.25em 0.25em / 0 0 0.5em 0.5em;
}

.layer,
.ring {
    border-radius: 50%;
    inset: 0;
}

.layer--face {
    transform: translateZ(3.75em);
}

.layer--img {
    background: url("@/assets/imgs/Gragons_Blog_Logo.png") 0 0 / 100% 100%;
    transform: translateZ(-3.75em);
}

.layer--profile {
    transform: translateZ(11em);
}

.layer--shade {
    background-color: hsla(187, 58%, 82%, 0.6);
}

.ring {
    box-shadow: 0 0 0 0.625em hsl(0, 0%, 100%) inset;
}
</style>