<template>
    <div class="message">
        提示：{{ message }}
    </div>
    <div class="face-container">
        <div class="video-container">
            <video ref="videoRef" autoplay muted></video>
            <canvas ref="canvasRef"></canvas>
        </div>
    </div>
</template>

<script setup lang='ts'>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import * as faceapi from 'face-api.js';
const message = ref('初始化中...');
// Use refs to get reactive references to the video and canvas elements
const videoRef = ref<HTMLVideoElement | null>(null);
const canvasRef = ref<HTMLCanvasElement | null>(null);
const MODEL_PATH = "/models/";
let intervalId: number | undefined;
let timeoutId: number | undefined;
const props = defineProps({
    visible: Boolean
});
const emit = defineEmits(['close']);
watch(() => props.visible, (newVal) => {
    if (!newVal) {
        closeFace();
    }
});
onMounted(() => {
    isClose.value = false;
    message.value = '初始化中...'
    if (videoRef.value) {
        videoRef.value.addEventListener('play', startFaceDetection);
        loadModels();
    }
    currentActionIndex = 0;
    resetHeadMovement();
});

onUnmounted(() => {
    closeFace();
});

const closeFace = () => {
    if (isClose.value) return;
    isClose.value = true;
    // 停止视频流
    if (videoRef.value && videoRef.value.srcObject) {
        const stream = videoRef.value.srcObject as MediaStream;
        const tracks = stream.getTracks();
        tracks.forEach(track => {
            track.stop();
        });
        videoRef.value.srcObject = null;
    }

    // 移除事件监听
    if (videoRef.value) {
        videoRef.value.removeEventListener('play', startFaceDetection);
    }

    // 清除定时器
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = undefined;
    }
    if (timeoutId) {
        clearTimeout(timeoutId);
        timeoutId = undefined;
    }

    console.log("子组件关闭了");
    emit('close', pictures.value);
}
const getCamera = async () => {
    try {
        if (videoRef.value) {
            const mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoRef.value.srcObject = mediaStream;
        }
    } catch (error) {
        console.error("Error accessing the camera:", error);
    }
}

const loadModels = async () => {
    await faceapi.loadTinyFaceDetectorModel(MODEL_PATH);
    await faceapi.loadFaceLandmarkTinyModel(MODEL_PATH);
    await faceapi.loadFaceExpressionModel(MODEL_PATH);
    await faceapi.loadAgeGenderModel(MODEL_PATH);
    getCamera();
}
// const actions = ['上下点头', '左右摇头', '笑一笑'];
const actions = ['笑一笑'];
let currentActionIndex = 0;
const pictures = ref(['']);
const isClose = ref(false);
interface HeadMovement {
    nod: { up: boolean, down: boolean },
    shake: { left: boolean, right: boolean }
}

let headMovement: HeadMovement;

const resetHeadMovement = () => {
    headMovement = {
        nod: { up: false, down: false },
        shake: { left: false, right: false }
    };
};

const startFaceDetection = async () => {
    if (!videoRef.value || !canvasRef.value) return;
    const canvas = canvasRef.value;
    const displaySize = { width: videoRef.value!.videoWidth, height: videoRef.value!.videoHeight };
    canvas.width = displaySize.width;
    canvas.height = displaySize.height;
    faceapi.matchDimensions(canvas, displaySize);
    nextAction();
    intervalId = setInterval(async () => {
        if (!videoRef.value) return;

        const detections = await faceapi.detectAllFaces(videoRef.value,
            new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks(true)
            .withAgeAndGender()
            .withFaceExpressions();

        const resizeDetections = faceapi.resizeResults(detections, displaySize);
        canvas.getContext('2d')?.clearRect(0, 0, canvas.width, canvas.height);
        faceapi.draw.drawDetections(canvas, resizeDetections);
        faceapi.draw.drawFaceLandmarks(canvas, resizeDetections);
        faceapi.draw.drawFaceExpressions(canvas, resizeDetections);
        console.log(detections);
        if (detections.length === 0) {
            message.value = '未检测到人脸，请对准摄像头';
            return;
        }
        // Calculate and log the average movement (e.g., nodding, shaking head)
        if (detections.length > 0) {
            const action = actions[currentActionIndex];
            const isValid = await validateAction(detections[0].landmarks, detections[0].expressions, action);
            if (isValid) {
                takePicture();
                currentActionIndex++;
                nextAction();
            }
        }
    }, 300);
}
const nextAction = () => {
    if (currentActionIndex < actions.length) {
        message.value = `请${actions[currentActionIndex]}`;
        resetHeadMovement();
        startActionTimer(); // 开始计时
    } else {
        message.value = '所有动作完成，正在验证...';
        closeFace();
    }
}

const startActionTimer = () => {
    if (timeoutId) {
        clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
        message.value = '动作超时，请重新尝试';
        closeFace();
    }, 5000); // 5秒超时
}
const validateAction = async (landmarks: faceapi.FaceLandmarks68, expressions: faceapi.FaceExpressions, action: string) => {
    switch (action) {
        case '上下点头':
            return checkNodding(landmarks);
        case '左右摇头':
            return checkShaking(landmarks);
        case '笑一笑':
            return checkSmiling(expressions);
    }
    return false;
}

const checkNodding = (landmarks: faceapi.FaceLandmarks68) => {
    const nose = landmarks.getNose();
    const jaw = landmarks.getJawOutline();
    const topNoseY = nose[0].y;
    const bottomJawY = jaw[jaw.length - 1].y;

    if (topNoseY < bottomJawY - 30) {
        headMovement.nod.down = true;
    } else if (topNoseY > bottomJawY - 10) {
        headMovement.nod.up = true;
    }

    return headMovement.nod.down && headMovement.nod.up;
}

const previousNosePositions: { x: number; y: number }[] = [];
const threshold = 20; // 鼻子移动的阈值
const requiredMovements = 5; // 需要的左右移动次数

const checkShaking = (landmarks: faceapi.FaceLandmarks68) => {
    const nose = landmarks.getNose();
    const noseX = nose[3].x; // 使用鼻子的中心点

    previousNosePositions.push({ x: noseX, y: nose[3].y });

    if (previousNosePositions.length > 10) {
        previousNosePositions.shift(); // 保持最后10个位置
    }

    if (previousNosePositions.length >= 2) {
        const movements = previousNosePositions.slice(1).reduce((count, pos, index) => {
            const prevPos = previousNosePositions[index].x;
            if (Math.abs(pos.x - prevPos) > threshold) {
                count += 1;
            }
            return count;
        }, 0);

        // 检查是否已经完成了左右摇头动作
        if (movements >= requiredMovements) {
            return true;
        }
    }

    return false;
}
const checkSmiling = (expressions: faceapi.FaceExpressions) => {
    return expressions.happy > 0.8;
}

const takePicture = () => {
    if (!videoRef.value || !canvasRef.value) return;
    const canvas = canvasRef.value;
    const context = canvas.getContext('2d');
    if (context) {
        context.drawImage(videoRef.value, 0, 0, canvas.width, canvas.height);
        const dataURL = canvas.toDataURL('image/png');
        pictures.value[currentActionIndex] = dataURL;
    }
}
defineExpose({
    closeFace
});
</script>

<style scoped>
.face-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
}

.video-container {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 50px;
    /* Ensure the container takes up full height */
}

.video-container video {
    width: 100%;
    height: 100%;
    border-radius: 50px;
}

.video-container canvas {
    border-radius: 50px;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>