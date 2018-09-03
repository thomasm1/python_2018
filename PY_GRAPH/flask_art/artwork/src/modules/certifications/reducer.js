// @flow
import types from './types';
import { combineReducers } from 'redux';
import type { Reducer } from 'redux';
import type { State, Action, Certification } from './definitions';
import { reduce, get, set, uniq, assign } from 'lodash';


const all: Reducer<any, Action> = (
  state = {data: []},
  action
) => {
  switch (action.type) {
    case types.LIST_CERTIFICATIONS_SUCCESS:
      return assign({}, state, get(action, 'result.data'))
    default: return state;
  }
};

const current: Reducer<any, Action> = (
  state = {
  	id: null,
  	status: null,
  	inspector: null,
  	DOI: null,
  	DOE: null,
  	nextStep: null,
  	certification: null,
  	action: null
  },
  action
) => {
  switch (action.type) {
    case types.LOAD_CERTIFICATION_DETAIL_SUCCESS:
      return assign({}, state, get(action, 'result.data'));
    default: return state;
  }
}

export const reducer: Reducer<State, Action> = combineReducers({ all, current })
