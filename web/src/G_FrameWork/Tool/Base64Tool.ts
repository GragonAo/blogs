export default class Base64Tool {
    /**
     * 将文件转换为 Base64 编码字符串
     * @param file - 需要转换的文件
     * @returns Promise<string> - 返回一个 Promise，解析为 Base64 编码字符串
     */
    static fileToBase64(file: File): Promise<string> {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result as string);
            reader.onerror = reject;
            reader.readAsDataURL(file);
        });
    }

    /**
     * 将 Base64 编码字符串转换为 Blob
     * @param base64 - Base64 编码字符串
     * @returns Blob - 返回 Blob 对象
     */
    static base64ToBlob(base64: string): Blob {
        const parts = base64.split(',');
        const byteString = atob(parts[1]);
        const mimeString = parts[0].match(/:(.*?);/)![1];
        const ab = new ArrayBuffer(byteString.length);
        const ia = new Uint8Array(ab);
        for (let i = 0; i < byteString.length; i++) {
            ia[i] = byteString.charCodeAt(i);
        }
        return new Blob([ab], { type: mimeString });
    }

    /**
     * 将 Base64 编码字符串转换为 File
     * @param base64 - Base64 编码字符串
     * @param filename - 文件名
     * @returns File - 返回 File 对象
     */
    static base64ToFile(base64: string, filename: string): File {
        const blob = Base64Tool.base64ToBlob(base64);
        return new File([blob], filename, { type: blob.type });
    }
}