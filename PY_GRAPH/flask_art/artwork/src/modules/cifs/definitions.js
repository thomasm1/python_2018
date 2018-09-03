// @flow
import types from './types';

export type CIF = {
  status: string,
  producer: string,
  ownership: string,
  standardBody: string,
  creationDate: string,
  trancheSize: number
}

export type State = {
  busy: boolean,
  all: { [id: string]: CIF }
};

export type Action = {
  type: $Keys<typeof types>,
  payload?: any,
  id?: string,
  result?: any,
  error?: any
};
