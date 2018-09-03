// @flow

import { createStore, combineReducers, applyMiddleware } from 'redux';
import type { Store } from 'redux';

import { clientMiddleware } from './middleware/clientMiddleware';
import * as app from './modules';
import initializeMockAPI from './utils/mockAPI';
import createLogger from 'redux-logger';

export function create(client: any, state?: Object): Store {

  initializeMockAPI(client);
  const logger = createLogger({diff: true});
  return createStore(
    combineReducers(app),
    state,
  	applyMiddleware(clientMiddleware(client), logger)
  );
};
