import axios, {type AxiosInstance, type AxiosRequestConfig,type AxiosResponse,type AxiosError, type InternalAxiosRequestConfig } from "axios";  
  
class Http {  
  public static baseURL = 'http://127.0.0.1:3333/'; // 静态基础 URL，可以按需修改  
  private axiosInstance: AxiosInstance;  
  
  constructor() {  
    this.axiosInstance = axios.create();  
    this.init();  
  }  
  
  private init() {  
    this.axiosInstance.interceptors.request.use(this.httpRequestInterceptor, this.httpRequestError);  
    this.axiosInstance.interceptors.response.use(this.httpResponseInterceptor, this.httpResponseError);  
  }  
  
  private httpRequestInterceptor(config: AxiosRequestConfig<any>): InternalAxiosRequestConfig<any> {  
    // 1. 非 http 开头需拼接基地址  
    // 确保 url 存在，如果不存在则抛出错误或进行其他处理  
    if (!config.url) {  
        throw new Error('config.url is undefined');  
    }  
    
    // 非 http 开头需拼接基地址  
    if (!config.url.startsWith('http')) {  
        config.url = `${Http.baseURL}${config.url}`;  
    }
    // 2. 请求超时时间，默认20s  
    config.timeout = 20000;  
    // 3. 添加请求头标识  
    config.headers = {  
      ...config.headers,  
      'source-client': 'h5',  
      // 如果需要添加 token，请取消注释以下代码  
      // 'Authorization': 'Bearer ' + this.getToken(),  
    };
    console.log(config);
    return config as InternalAxiosRequestConfig<any>;  
  }  
  
  private httpRequestError(error: any) {  
    console.error('Request error:', error);  
    // TODO: 抛出错误或进行其他错误处理  
    return Promise.reject(error);  
  }  
  
  private httpResponseInterceptor(response: AxiosResponse) {
    console.log(response);
    // 可以在这里对响应数据进行处理，例如转换数据结构等  
    return response;  
  }  
  
  private httpResponseError(error: AxiosError) {  
    console.error('Response error:', error);  
    // TODO: 根据错误类型进行不同的处理，例如网络错误、超时等  
    return Promise.reject(error);  
  }  
  
  // 假设有一个获取 token 的方法，可以根据实际情况实现  
  // private getToken(): string | null {  
  //   // 实现获取 token 的逻辑  
  //   return null;  
  // }  
  
  //发送 GET 实现方法
  public get<T = any>(url: string, config?: AxiosRequestConfig): Promise<T | undefined> {  
    return this.axiosInstance.get<T>(url, config).then((response: AxiosResponse<T>) => {  
      return response.data as T;  
    }).catch((error) => {  
      // 这里处理错误，或者将错误传递给调用者  
      console.error('Error fetching data:', error);  
      return undefined; // 或者抛出一个错误  
    });  
  }
  // post 方法实现  
  public post<T = any,D = any>(url: string,data:D,config?: AxiosRequestConfig<any>): Promise<T | undefined> {  
    return this.axiosInstance.post<T>(url,data,config).then((response: AxiosResponse<T>) => {  
      return response.data as T;  
    }).catch((error) => {  
      // 这里处理错误，或者将错误传递给调用者  
      console.error('Error fetching data:', error);  
      return undefined; // 或者抛出一个错误  
    }); 
  }
  
  // put 方法实现  
  public put<T = any,D = any>(url: string,data?:D,config?: AxiosRequestConfig<any>): Promise<T | undefined> {  
    return this.axiosInstance.put<T>(url,data,config).then((response: AxiosResponse<T>) => {  
      return response.data as T;  
    }).catch((error) => {  
      // 这里处理错误，或者将错误传递给调用者  
      console.error('Error fetching data:', error);  
      return undefined; // 或者抛出一个错误  
    }); 
  }  
  
  // delete 方法实现  
  public delete<T = any>(url: string,config?: AxiosRequestConfig<any>): Promise<T | undefined> {  
    return this.axiosInstance.delete<T>(url,config).then((response: AxiosResponse<T>) => {  
      return response.data as T;  
    }).catch((error) => {  
      // 这里处理错误，或者将错误传递给调用者  
      console.error('Error fetching data:', error);  
      return undefined; // 或者抛出一个错误  
    }); 
  }  
}  
  
export default Http;