// @flow
import React, { Children } from 'react';

import { connect } from 'react-redux';
import type { ActionCreator } from 'redux';

import { withRouter, browserHistory } from 'react-router';
import type { RouteConfig, Location } from 'react-router';

export type AccountProps = {
  children: React$Element<*> | Array<React$Element<*>>
};

export class Accounts extends React.Component {
  props: AccountProps;

  render () {
    const { children } = this.props;
    return (
      <div className='content-container'>
        {children}
      </div>
    );
  }
}

export default connect(undefined, {})(withRouter(Accounts));
