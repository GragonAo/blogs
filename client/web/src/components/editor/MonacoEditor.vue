<template>
    <el-card style="width: 100%" shadow="always">
        <el-row style="margin-bottom: 10px;">
            <el-col :span="24" class="selectLanguage">
                <el-select @change="updateSelect" v-model="selectLanguageValue" :placeholder="selectedLanguageLabel"
                    size="large" style="width: 240px">
                    <el-option v-for="item in code.LanguageOptions" :key="item.value" :label="item.label"
                        :value="item.value" />
                </el-select>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24">
                <div class="codeEditBox" :style="{ height: '400px' }"></div>
            </el-col>
        </el-row>
    </el-card>
</template>

<script lang="ts" setup>
import * as monaco from 'monaco-editor'
import { CodeEditor } from '@/utils/Code_Editor';
import { nextTick, ref, onBeforeUnmount, computed } from 'vue'
const text = ref('')
defineProps({
    textValue: {
        type: String,
        default: '',
    },
})
const emits = defineEmits(['update:textValue'])
let editor: monaco.editor.IStandaloneCodeEditor | null;
const code = new CodeEditor();
code.initLanguage();
const editorInit = () => {
    nextTick(() => {
        text.value = code.LanguageOptions[0].code;
        !editor ? (editor = monaco.editor.create(document.querySelector('.codeEditBox') as HTMLElement, {
            value: text.value, // 编辑器初始显示文字
            language: 'cpp', // 语言支持自行查阅demo
            automaticLayout: false, // 自适应布局
            theme: 'vs-dark', // 官方自带三种主题vs, hc-black, or vs-dark
            foldingStrategy: 'indentation', // 代码可分小段折叠
            foldingHighlight: true, // 折叠等高线
            renderLineHighlight: 'all', // 行亮
            selectOnLineNumbers: true, // 显示行号
            minimap: {
                enabled: false,
            },
            readOnly: false, // 只读
            fontSize: 16, // 字体大小
            scrollBeyondLastLine: false, // 取消代码后面一大段空白
            overviewRulerBorder: false, // 不要滚动条的边框
            wordWrap: 'on', // 自动换行
            tabSize: 2, // tab 缩进长度
            autoClosingQuotes: 'always', // 是否自动添加结束的单引号 双引号 "always" | "languageDefined" | "beforeWhitespace" | "never"
            contextmenu: true, // 启用上下文菜单
            columnSelection: false, // 启用列编辑 按下shift键位然后按↑↓键位可以实现列选择 然后实现列编辑
            folding: true, // 是否启用代码折叠
        }))
            : editor.setValue('')
        emits('update:textValue', text.value);
        // 监听值的变化
        editor.onDidChangeModelContent((val: any) => {
            text.value = editor!.getValue()
            emits('update:textValue', text.value)
        })
    })
}
editorInit()
onBeforeUnmount(() => {
    // 组件卸载时，销毁 Monaco 编辑器实例和模型  
    if (editor) {
        editor.dispose()
        editor = null
    }
})
const selectLanguageValue = ref(code.LanguageOptions[0].value);
const selectedLanguageLabel = computed(() => {
    const selectedOption: {
        value: string;
        label: string;
        code: string;
    } | undefined = code.LanguageOptions.find(option => option.value === selectLanguageValue.value);
    return selectedOption ? selectedOption.label : '未知语言';
});
const updateSelect = () => {
    if (editor) {
        const selectedOption: {
            value: string;
            label: string;
            code: string;
        } | undefined = code.LanguageOptions.find(option => option.value === selectLanguageValue.value);
        text.value = selectedOption!.code;
        monaco.editor.setModelLanguage(editor.getModel()!, selectedOption!.value);
        editor.getModel()!.setValue(text.value);
    }
}
</script>
<style scoped>
.selectLanguage {
    display: flex;
    justify-content: flex-end;
}
</style>
