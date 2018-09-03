// @flow
import types from './types';
import type { AuthReducer } from './definitions';

import localStorage from 'localStorage';

export const reducer: AuthReducer = (
  state = {
    busy: false,
    identity: JSON.parse(localStorage.getItem('GEM-IDENTITY')) || null
  },
  action
) => {
  switch (action.type) {
    case types.LOGIN:
      return {
        ...state,
        busy: true
      };
    case types.LOGIN_SUCCESS:
      return {
        ...state,
        busy: false,
        identity: action.result.data.data
      };
    case types.LOGIN_FAILURE:
      return {
        ...state,
        busy: false,
        identity: null
      };
    case types.LOGOUT:
      return {
        ...state,
        identity: null
      };
    default:
      return state;
  }
};
