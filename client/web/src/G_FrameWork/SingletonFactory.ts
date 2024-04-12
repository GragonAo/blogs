// SingletonFactory 类，现在支持带参数的构造函数  
class SingletonFactory {
    private static instances: { [key: string]: any } = {};
    private static constructorsWithArgs: { [key: string]: { ctor: new (...args: any[]) => any, args: any[] } } = {};

    public static getInstance<T>(ctor: new (...args: any[]) => T, ...args: any[]): T {
        const key = ctor.name;
        // 检查是否已经有带有参数的实例  
        if (SingletonFactory.constructorsWithArgs[key] &&
            JSON.stringify(SingletonFactory.constructorsWithArgs[key].args) === JSON.stringify(args)) {
            return SingletonFactory.instances[key] as T;
        }
        // 如果没有，则创建一个新的带有参数的实例  
        if (!SingletonFactory.instances[key]) {
            const instance = new ctor(...args);
            SingletonFactory.instances[key] = instance;
            // 如果需要保存构造函数和参数以便后续比较，可以这样做：  
            // SingletonFactory.constructorsWithArgs[key] = { ctor, args };  
        }
        return SingletonFactory.instances[key] as T;
    }
}
export default SingletonFactory;