/* 原生方法并不提供很好的任务管理功能，比如暂停、恢复或取消定时任务。*/
class TaskManager {
  private tasks: { [key: string]: { timerId: NodeJS.Timeout, interval: number, callback: () => void } } = {};
  /**  
   * 创建定时任务  
   *  
   * @param name 任务名称  
   * @param interval 任务执行间隔（毫秒）  
   * @param callback 回调函数  
   */
  public create(name: string, interval: number, callback: () => void): void {
    if (this.tasks[name]) {
      console.warn(`Task with name "${name}" already exists.`);
      return;
    }
    const timerId = setInterval(callback, interval);
    this.tasks[name] = { timerId, interval, callback };
  }
  /**  
  * 暂停定时任务  
  *  
  * @param name 任务名称  
  */
  public pause(name: string): void {
    const task = this.tasks[name];
    if (task) {
      clearInterval(task.timerId);
    } else {
      console.warn(`Task with name "${name}" does not exist.`);
    }
  }
  /**  
   * 恢复定时任务  
   *  
   * @param name 任务名称  
   */
  public resume(name: string): void {
    const task = this.tasks[name];
    if (task) {
      task.timerId = setInterval(task.callback, task.interval);
    } else {
      console.warn(`Task with name "${name}" does not exist.`);
    }
  }
  /**  
   * 取消定时任务  
   *  
   * @param name 任务名称  
   * 如果提供了任务名称，则取消对应的定时任务；  
   * 如果不提供任务名称，则取消所有定时任务。  
   */
  public cancel(name: string): void {
    const task = this.tasks[name];
    if (task) {
      clearInterval(task.timerId);
      delete this.tasks[name];
    } else {
      console.warn(`Task with name "${name}" does not exist.`);
    }
  }
}
export default TaskManager;