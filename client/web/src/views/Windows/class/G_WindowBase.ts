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
    protected id: number;
    private updateTime: number;
    private title: string;
    private isOpen: boolean;
    private top: number;
    private left: number;

    public get IsOpen(): boolean { return this.isOpen; }
    public get Title(): string { return this.title; }
    public get Top(): number { return this.top; }
    public get Left(): number { return this.left; }

    public set Title(value: string) { this.title = value; }
    public set Top(value: number) { this.top = value; }
    public set Left(value: number) { this.left = value; }

    protected constructor(id: number, title: string, top: number, left: number) {
        this.id = id;
        this.title = title;
        this.isOpen = false;
        this.top = top;
        this.left = left;
        this.updateTime = new Date().getTime();
    }
    // 静态工厂方法，用于创建实例
    protected static createInstance<T extends G_WindowBase>(
        this: new (id: number, title: string, top: number, left: number) => T,
        id: number,
        title: string,
        top: number,
        left: number
    ): T {
        return new this(id, title, top, left);
    }
    public abstract init(): void;
    public destroyWindow(): void {
        this.closeWindow();
        // TODO: 在这里添加具体的销毁逻辑，例如解除事件监听、清理资源等。
        console.log(`Window ${this.id} is being destroyed.`);
    }
    public getUpdateTime(): number {
        return this.updateTime;
    }
    public getWindowId(): number {
        return this.id;
    }
    public openWindow(): void {
        console.log(`Window ${this.id} is being open.`);
        this.isOpen = true;
        this.updateTime = new Date().getTime(); // 更新时间戳为当前时间
    }
    public closeWindow(): void {
        console.log(`Window ${this.id} is being close.`);
        this.isOpen = false;
        this.updateTime = new Date().getTime(); // 更新时间戳为当前时间
    }
}