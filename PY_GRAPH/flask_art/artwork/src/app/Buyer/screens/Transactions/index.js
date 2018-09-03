// @flow
import React, { Children } from 'react';

import { connect } from 'react-redux';
import type { ActionCreator } from 'redux';

import { withRouter, browserHistory } from 'react-router';
import type { RouteConfig, Location } from 'react-router';

import { Navbar } from 'components/Navbar';

export type TransactionProps = {
  children: React$Element<*> | Array<React$Element<*>>,
  route: RouteConfig,
  location: Location
};

export class Transactions extends React.Component {
  props: TransactionProps;

  state: {
    showBackBtn: boolean;
    action: any;
  };

  state = {
    showBackBtn: false,
    action: ''
  };

  static childContextTypes = {
    setBackBtnVisibility: React.PropTypes.func,
    setPageAction: React.PropTypes.func
  };

  getChildContext () {
    return {
      setBackBtnVisibility: (showBackBtn: boolean) => this.setState({ showBackBtn }),
      setPageAction: (action: any) => this.setState({ action })
    };
  }

  render () {
    const { route, location, children } = this.props;
    const { showBackBtn, action } = this.state;
    return (
      <div className='content-container'>
        {children}
      </div>
    );
  }
}

export default connect(
  () => ({}),
  {}
)(withRouter(Transactions));
