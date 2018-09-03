// @flow
import types from './types';
import type { ActionCreator } from 'redux';
import type { CIF } from './definitions';

export const loadCIFDetail: ActionCreator<any> = (id) => ({
  type: types.LOAD_CIF_DETAIL,
  responseTypes: [types.LOAD_CIF_DETAIL_SUCCESS, types.LOAD_CIF_DETAIL_FAILURE],
  promise: (client) => client.get(`/cifs/${id}`)
});

export const setCurrentCIF: ActionCreator<any> = (id) => ({
  type: types.SET_CURRENT_CIF,
  payload: id
});

export const listCIFs: ActionCreator<any> = () => ({
  type: types.LIST_CIFS,
  responseTypes: [types.LIST_CIFS_SUCCESS, types.LIST_CIFS_FAILURE],
  promise: (client) => client.get('/cifs')
});
