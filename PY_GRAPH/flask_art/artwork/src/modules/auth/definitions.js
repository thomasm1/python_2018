// @flow
import type { Reducer } from 'redux';

export type Identity = {
  avatar: ?string,
  created_at: string,
  email: string,
  id: number,
  name: ?string,
  network_id: string,
  provider: string,
  uid: string,
  updated_at: string
};

export type CreateUserPayload = {
  name: string,
  avatar: ?string,
  email: string,
  password: string,
  password_confirmation: string
};

export type AuthState = {
  busy: boolean,
  identity: ?Object,
};

export type AuthAction = {
  type: string,
  payload: any,
  result: any
};

export type AuthReducer = Reducer<AuthState, AuthAction>;
