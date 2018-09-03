// @flow
import types from './types';
import type { ActionCreator } from 'redux';
import type { Certification } from './definitions';

export const loadCertificationDetail: ActionCreator<any> = (id) => ({
  type: types.LOAD_CERTIFICATION_DETAIL,
  responseTypes: [types.LOAD_CERTIFICATION_DETAIL_SUCCESS, types.LOAD_CERTIFICATION_DETAIL_FAILURE],
  promise: (client) => client.get(`/certifications/${id}`)
});

export const setCurrentCertification: ActionCreator<any> = (id) => ({
  type: types.SET_CURRENT_CERTIFICATION,
  payload: id
});

export const listCertifications: ActionCreator<any> = () => ({
  type: types.LIST_CERTIFICATIONS,
  responseTypes: [types.LIST_CERTIFICATIONS_SUCCESS, types.LIST_CERTIFICATIONS_FAILURE],
  promise: (client) => client.get('/certifications')
});
