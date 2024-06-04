import type { Result } from "@/API/API_Types/Base";
import useUserStore from "@/stores/User";
import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse, type AxiosError, type InternalAxiosRequestConfig } from "axios";
import { APP_CONFIG } from '~/app.config';
class Http {
  public static baseURL = APP_CONFIG.baseURL;
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
    if (!config.url) {
      throw new Error('config.url is undefined');
    }
    if (!config.url.startsWith('http')) {
      config.url = `${Http.baseURL}${config.url}`;
    }
    const token = useUserStore().token?.token;
    config.timeout = 20000;
    config.headers = {
      ...config.headers,
      'Authorization': token ? "Bearer " + token : ''
    };
    return config as InternalAxiosRequestConfig<any>;
  }

  private httpRequestError(error: any) {
    console.error('Request error:', error);
    return Promise.reject(error);
  }

  private httpResponseInterceptor(response: AxiosResponse) {
    console.log(response)
    if (response.status === 401 && response.data.message === 'Token has expired') {
      useUserStore().clearUserInfo();
      useUserStore().clearToken();
    }
    // 可以在这里对响应数据进行处理，例如转换数据结构等  
    return response;
  }

  private httpResponseError(error: AxiosError) {
    console.log(error)
    const res = error.response?.data as Result<any>;
    if (res && res.code === 401) {
      useUserStore().logOut();
    }
    // TODO: 根据错误类型进行不同的处理，例如网络错误、超时等   
    return Promise.reject(error.response?.data);
  }

  public get<T = any>(url: string, config?: AxiosRequestConfig): Promise<T | undefined> {
    return this.axiosInstance.get<T>(url, config).then((response: AxiosResponse<T>) => {
      return response.data as T;
    })
  }
  public post<T = any, D = any>(url: string, data: D, config?: AxiosRequestConfig<any>): Promise<T | undefined> {
    return this.axiosInstance.post<T>(url, data, config).then((response: AxiosResponse<T>) => {
      return response.data as T;
    })
  }
  public put<T = any, D = any>(url: string, data?: D, config?: AxiosRequestConfig<any>): Promise<T | undefined> {
    return this.axiosInstance.put<T>(url, data, config).then((response: AxiosResponse<T>) => {
      return response.data as T;
    });
  }
  public delete<T = any>(url: string, config?: AxiosRequestConfig<any>): Promise<T | undefined> {
    return this.axiosInstance.delete<T>(url, config).then((response: AxiosResponse<T>) => {
      return response.data as T;
    })
  }
}

export default Http;