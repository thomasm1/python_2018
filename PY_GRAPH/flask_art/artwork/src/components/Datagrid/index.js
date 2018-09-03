// @flow
import React from 'react';

import { isArray } from 'lodash';

import styles from './styles.less';

import crypto from 'crypto';

export type DatagridProps = {
  zDepth?: number,
  data: Array<{
    title: string|React$Element<*>,
    value: number|string|React$Element<*>
  }>,
  gridSize?: number,
  className?: string | Array<string>,
  title?: string,
  colStyle?: any,
  style?: any
};

function _toArray<T> (tOrArray: any): Array<T> {
  if (!tOrArray) return [];
  if (!isArray(tOrArray)) {
    return [tOrArray];
  } else {
    return tOrArray
  };
}

export const Datagrid = ({ style, title, zDepth = 1, data, className, colStyle = {}, gridSize = 4, ...rest }: DatagridProps) => {
  const key = `${Date.now()}.${Math.random()}`;
  return (
    <div className={['z-depth-1', styles.Datagrid, 'row', ...(_toArray(className): Array<string>)].join(' ')} style={style}>
      { title ? <h5>{title}</h5> : null }
      {data.map(
        ({ title, value }, i) => (
          <div className={`col s${gridSize}`} style={colStyle} key={`${key}-${i}`}>
            <label>{title}</label><br/>
            <span>{value}</span>
          </div>
        )
      )}
    </div>
  );
};
