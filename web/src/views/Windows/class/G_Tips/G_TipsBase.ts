export interface G_ITips {
    showTips(title: string, message?: string): boolean;
}
import { ElNotification } from 'element-plus'
export class G_TipsBase implements G_ITips {
    showTips(title: string, message?: string): boolean {
        ElNotification({
            title: 'Custom Position',
            message: "I'm at the top right corner",
            offset: 20,
        })
        return true;
    }
}