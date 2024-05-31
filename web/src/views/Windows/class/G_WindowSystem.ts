import type { Type } from "typescript";
import { G_WindowBase, type G_IWindow } from "./G_WindowBase";
export interface WindowClass<T extends G_WindowBase> {
    new(...args: any[]): T;
    createInstance(id: number, title: string, top: number, left: number): T;
}

export default class G_WindowSystem {
    private window_id = 0;
    private windows = new Map<number, G_IWindow>();
    // 检查并清理未使用的窗口  
    public checkAndCleanUpUnusedWindows(): void {
        const now = new Date();
        for (const [id, window] of this.windows) {
            const lastUpdateTime = window.getUpdateTime();
            const minutesDiff = (now.getTime() - lastUpdateTime) / (1000 * 60);
            const baseWindow = window as G_WindowBase;
            if (minutesDiff > 2 && baseWindow.IsOpen === false) { // 如果超过2分钟未使用  
                this.destroyWindow(id);
            }
        }
    }
    // 使用泛型约束确保传入的构造函数返回 G_IWindow 类型  
    public addWindow<T extends G_WindowBase>(type: WindowClass<T>, title: string, top: number, left: number): number {
        const id = this.window_id;
        const window = type.createInstance(id, title, top, left); // 调用静态方法创建实例
        window.init();
        this.windows.set(this.window_id++, window);
        return id;
    }

    public destroyWindow(id: number) {
        const window = this.windows.get(id);
        if (window) {
            window.destroyWindow();
            this.windows.delete(id);
        } else {
            console.error(`ID 为 ${id} 的窗口不存在`);
        }
    }
    public openWindow(id: number) {
        const window = this.windows.get(id);
        if (window) {
            window.openWindow();
        } else {
            throw new Error(`ID 为 ${id} 的窗口不存在，无法打开`);
        }
    }
    public closeWindow(id: number) {
        const window = this.windows.get(id);
        if (window) {
            window.closeWindow();
        } else {
            throw new Error(`ID 为 ${id} 的窗口不存在，无法关闭`);
        }
    }
    public getWindowList(): G_WindowBase[] {
        return Array.from(this.windows.values()) as G_WindowBase[];
    }
    public getWindowById<T extends G_IWindow>(id: number): T | null {
        const window = this.windows.get(id);
        return window as T;
    }
}