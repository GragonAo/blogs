import type { G_ITips, G_TipsBase } from "./G_TipsBase";

export default class G_TipsSystem {
    // 使用类的构造函数作为键，G_TipsBase 的实例作为值  
    private tipsMap = new Map<new () => G_ITips, G_TipsBase>();
    /**
     * 根据类的类型找到对应的实例，如果未注册则动态创建  不要存直接获取完调用对应方法，防止内存泄露
     * @param ctor 返回继承G_ITips的接口
     * @returns 
     */
    public getTips<T extends G_ITips>(ctor: new () => T): T {
        // 尝试从映射中获取实例
        let instance = this.tipsMap.get(ctor);
        if (!instance) {
            // 如果实例不存在，则创建新实例并添加到映射中  
            instance = new ctor();
            this.tipsMap.set(ctor, instance);
        }
        // 返回与ctor类型相匹配的实例  
        return instance as T;
    }
}