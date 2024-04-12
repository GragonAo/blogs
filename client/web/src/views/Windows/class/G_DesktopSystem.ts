import G_WindowSystem from "./G_WindowSystem";
import G_FileSystem from "./G_FileSystem";
import SingletonFactory from "@/G_FrameWork/SingletonFactory";

export default class G_DesktopSystem {
    private windows: G_WindowSystem;
    private files: G_FileSystem;
    private checkInterval: NodeJS.Timeout | null = null;
    constructor() {
        this.windows = SingletonFactory.getInstance(G_WindowSystem);
        this.files = SingletonFactory.getInstance(G_FileSystem);
    }
    // 启动系统时开始定期检查  
    public start(): void {
        this.checkInterval = setInterval(this.checkAndCleanUp.bind(this), 60000); // 每60秒检查一次  
    }
    // 停止系统时停止定期检查  
    public stop(): void {
        if (this.checkInterval) {
            clearInterval(this.checkInterval);
            this.checkInterval = null;
        }
    }
    // 定期检查并清理子模块中的资源  
    private checkAndCleanUp(): void {
        this.windows.checkAndCleanUpUnusedWindows(); // 检查并清理未使用的窗口  
        this.files.checkAndCleanUpUnusedFiles(); // 检查并清理未使用的文件  
        // 可以添加其他子模块的自我检查调用  
    }
}