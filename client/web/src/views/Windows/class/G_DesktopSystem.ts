import WindowSystem from "./WindowSystem";
import FileSystem from "./FileSystem";

export class G_DesktopSystem {
    private windows: WindowSystem;
    private files: FileSystem;
    constructor() {
        this.windows = new WindowSystem();
        this.files = new FileSystem();
    }
}