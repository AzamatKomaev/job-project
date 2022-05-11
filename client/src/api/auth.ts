import {AxiosResponse} from "axios";
import axios from "./api-client";

export interface ILoginData {
  username: string | null,
  first_name: string | null,
  last_name: string | null,
  role: string | null,
  password: string | null,
  email: string | null
}

export class AuthApi {
  public static async create(data: ILoginData): Promise<AxiosResponse> {
    try {
      return await axios.post(`${process.env.REACT_APP_SERVER_URL}/users/create/`, data);
    } catch (e: any) {
      return e.response;
    }
  }
}