interface MessageHandler {
    (message: string): void;
}
/**  
 * WebSocket消息类型。
 */
type MessageType = 'typeA' | 'typeB' | 'typeC'; // 定义所有可能的消息类型

class WebSocketClient {
    private socket?: WebSocket;
    // 连接服务器的地址
    private url: string;
    // 用来存储不同消息类型对应的处理器函数数组 
    private handlers: { [key in MessageType]?: MessageHandler[] } = {};
    constructor(url: string) {
        this.url = url;
    }
    /**  
     * 连接到WebSocket服务器。  
     * 如果WebSocket已经连接，则不会重新连接。  
     */
    public connect(): void {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            console.log('WebSocket is already connected.');
            return;
        }

        this.socket = new WebSocket(this.url);

        this.socket.onopen = (event) => {
            console.log('WebSocket connection opened.');
            this.onOpen(event);
        };

        this.socket.onmessage = (event) => {
            console.log('Received message:', event.data);
            this.onMessage(event);
        };

        this.socket.onclose = (event) => {
            console.log('WebSocket connection closed.');
            this.onClose(event);
            this.socket = undefined; // 重置socket对象  

        }
    }
    /**  
     * 当WebSocket连接成功打开时调用的方法。  
     * @param event WebSocket打开事件对象。  
     */
    private onOpen(event: Event): void {
        //TODO 连接成功后的操作
    }
    /**  
     * 当WebSocket连接关闭时调用的方法。  
     * @param event WebSocket关闭事件对象。  
     */
    private onClose(event: CloseEvent): void {
        //TODO 连接关闭的逻辑
    }
    /**  
     * 当WebSocket发生错误时调用的方法。  
     * @param error 错误事件对象。  
     */
    private onError(error: Event): void {
        //TODO 处理错误情况 
    }
    /**  
     * 向WebSocket服务器发送消息。  
     * 如果WebSocket未连接或连接已关闭，则打印错误信息并返回。  
     * @param message 要发送的消息内容。  
     */
    public send(message: string): void {
        if (!this.socket || this.socket.readyState !== WebSocket.OPEN) {
            console.error('WebSocket is not connected. Cannot send message.');
            return;
        }
        this.socket.send(message);
    }
    /**  
     * 关闭WebSocket连接。  
     * 如果WebSocket已连接，则关闭连接。  
     */
    public close(): void {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            this.socket.close();
        }
    }
    /**  
     * 注册消息处理器。  
     * 当收到特定类型的消息时，调用相应的处理器函数。  
     * @param type 消息类型。  
     * @param handler 消息处理器函数。  
     */
    public registerMessageHandler(type: MessageType, handler: MessageHandler): void {
        if (!this.handlers[type]) {
            this.handlers[type] = [];
        }
        this.handlers[type]?.push(handler);
    }
    /**  
     * 注销消息处理器。  
     * 从指定类型的消息处理器列表中移除指定的处理器函数。  
     * @param type 消息类型。  
     * @param handler 要注销的消息处理器函数。  
     */
    public unregisterMessageHandler(type: MessageType, handler: MessageHandler): void {
        if (this.handlers[type]) {
            const index = this.handlers[type]?.indexOf(handler);
            if (index !== -1) {
                this.handlers[type]?.splice(index!, 1);
                if (this.handlers[type]?.length === 0) {
                    delete this.handlers[type]; // 如果该类型的处理器数组为空，则删除它  
                }
            } else {
                console.warn(`Handler for type ${type} not found.`);
            }
        } else {
            console.warn(`No handlers registered for type ${type}.`);
        }
    }
    /**  
     * 当WebSocket收到消息时调用的方法。  
     * 根据消息类型调用相应的处理器函数。  
     * @param event WebSocket消息事件对象。  
     */
    private onMessage(event: MessageEvent): void {
        const messageType = event.data as MessageType; // 假设消息体就是消息类型  
        const handlers = this.handlers[messageType];
        if (handlers) {
            handlers.forEach(handler => {
                handler(event.data);
            });
        } else {
            console.log(`No handler registered for message type: ${messageType}`);
        }
    }
}
export default WebSocketClient;