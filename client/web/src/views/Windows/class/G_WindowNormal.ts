import { G_WindowBase } from "./G_WindowBase";

export class G_WindowNormal extends G_WindowBase {
    // 用于拖拽的变量  
    public dragStartX = 0;
    public dragStartY = 0;
    public init(): void {
        console.log(this.id + " windows被实例化力");
    }
}