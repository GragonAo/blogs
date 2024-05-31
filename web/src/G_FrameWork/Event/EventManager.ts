/* 事件管理器类：提供了注册事件、触发事件以及注销事件的功能。*/
class EventManager {
    private events: { [key: string]: Function[] } = {};

    /**  
     * 注册事件  
     * @param eventName 事件名  
     * @param callback 回调函数  
     */
    public on(eventName: string, callback: Function): void {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        this.events[eventName].push(callback);
    }

    /**  
     * 触发事件  
     * @param eventName 事件名  
     * @param data 传递给回调的数据  
     */
    public emit(eventName: string, data?: any): void {
        if (this.events[eventName]) {
            this.events[eventName].forEach(callback => {
                callback(data);
            });
        }
    }

    /**  
     * 注销事件  
     * @param eventName 事件名  
     * @param callback 回调函数，如果不提供，则注销所有该事件的回调函数  
     */
    public off(eventName: string, callback?: Function): void {
        if (this.events[eventName]) {
            if (callback) {
                this.events[eventName] = this.events[eventName].filter(cb => cb !== callback);
            } else {
                delete this.events[eventName];
            }
        }
    }
}
export default EventManager;