import SingletonFactory from "@/G_FrameWork/SingletonFactory";
import WindowSystem from "./WindowSystem";

export interface G_IWindow {
    /**
     * 打开窗口
     */
    openWindow(): void;
    /**
     * 关闭窗口
     */
    closeWindow(): void;
    /**
     * 获取最后一次使用的时间戳
     */
    getUpdateTime(): number;
    /**
     * 销毁窗口
     */
    destroyWindow(): void;
}

export abstract class G_WindowBase implements G_IWindow {
    private id: number;
    private updata_time: number;
    private title: string;
    private isOpen: boolean;
    private top: number;
    private left: number;

    public Get_IsOpen() { return this.isOpen; }
    public Get_Title() { return this.title; }
    public Get_Top() { return this.top; }
    public Get_Left() { return this.left; }
    public Set_Top(top: number) { this.top = top; }
    public Set_Left(left: number) { this.left = left; }

    constructor(title: string, top: number, left: number) {
        this.id = 0;
        this.title = title;
        this.isOpen = false;
        this.top = top;
        this.left = left;
        this.updata_time = new Date().getTime();
        SingletonFactory.getInstance(WindowSystem).addWindow(this);
        this.init();
    }
    public abstract init(): void;
    destroyWindow(): void {
        this.closeWindow();
        //TODO 销毁的事情 例如卸载什么。。
    }
    getUpdateTime(): number {
        return this.updata_time;
    }
    openWindow(): void {
        this.isOpen = true;
    }
    closeWindow(): void {
        this.isOpen = false;
    }
}