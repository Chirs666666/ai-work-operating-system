import axios, { AxiosError, AxiosInstance } from 'axios';

export interface DataForSeoClient {
  login: string;
  password: string;
  baseUrl: string;
  httpClient: AxiosInstance;
  get: <T>(url: string) => Promise<T>;
  post: <T>(url: string, data: any) => Promise<T>;
}

export class DataForSeoModuleNotEnabledError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'DataForSeoModuleNotEnabledError';
  }
}

const MODULE_SCOPE_HINTS: Array<{ pattern: RegExp; module: string }> = [
  {
    pattern: /^\/app_data\/(?:apple|google_play)\/(?:search|app_info|reviews)\/live$/,
    module: 'App Data',
  },
  {
    pattern: /^\/dataforseo_labs\/app_store\//,
    module: 'DataForSEO Labs App Store',
  },
  {
    pattern: /^\/serp\//,
    module: 'SERP',
  },
  {
    pattern: /^\/content_generation\//,
    module: 'Content Generation',
  },
];

function buildModuleScopeError(url: string, error: AxiosError): DataForSeoModuleNotEnabledError | null {
  if (error.response?.status !== 404) {
    return null;
  }

  const matchedModule = MODULE_SCOPE_HINTS.find(entry => entry.pattern.test(url));
  if (!matchedModule) {
    return null;
  }

  return new DataForSeoModuleNotEnabledError(
    `DataForSEO module not enabled: ${matchedModule.module} (${url}). ` +
    `This 404 usually means the module is not included in the current subscription, not that the MCP endpoint is wrong. ` +
    `Enable the module in the DataForSEO dashboard or use a tool from an enabled module.`
  );
}

export function setupApiClient(login: string, password: string): DataForSeoClient {
  const baseUrl = 'https://api.dataforseo.com/v3';
  
  // Create an Axios instance with authentication
  const httpClient = axios.create({
    baseURL: baseUrl,
    auth: {
      username: login,
      password: password
    },
    headers: {
      'Content-Type': 'application/json'
    }
  });
  
  // Create the client interface
  const client: DataForSeoClient = {
    login,
    password,
    baseUrl,
    httpClient,
    
    async get<T>(url: string): Promise<T> {
      try {
        const response = await httpClient.get(url);
        return response.data as T;
      } catch (error) {
        if (axios.isAxiosError(error)) {
          const moduleScopeError = buildModuleScopeError(url, error);
          if (moduleScopeError) {
            console.error(moduleScopeError.message);
            throw moduleScopeError;
          }
          console.error(`DataForSEO API GET error (${url}):`, error.response?.data || error.message);
        } else {
          console.error(`DataForSEO API GET error (${url}):`, error);
        }
        throw error;
      }
    },
    
    async post<T>(url: string, data: any): Promise<T> {
      try {
        const response = await httpClient.post(url, data);
        return response.data as T;
      } catch (error) {
        if (axios.isAxiosError(error)) {
          const moduleScopeError = buildModuleScopeError(url, error);
          if (moduleScopeError) {
            console.error(moduleScopeError.message);
            throw moduleScopeError;
          }
          console.error(`DataForSEO API POST error (${url}):`, error.response?.data || error.message);
        } else {
          console.error(`DataForSEO API POST error (${url}):`, error);
        }
        throw error;
      }
    }
  };
  
  return client;
}
