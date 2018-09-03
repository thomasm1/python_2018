// @flow
import types from './types';
import type { ActionCreator } from 'redux';

export const setModalType: ActionCreator<any> = (modalType) => ({
  type: types.SET_MODAL_TYPE,
  modalType
});
