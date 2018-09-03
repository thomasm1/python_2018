// @flow
import React from 'react';
import { connect } from 'react-redux';
import { withRouter, browserHistory } from 'react-router';
import type { RouteConfig, Location, LocationRouter } from 'react-router';

import { logout } from 'modules/auth/actions';
import type { Identity } from 'modules/auth/definitions';

import $ from 'jquery';

import './styles.less';
import Modal from 'components/Modal';

export type AppProps = {
  children: React$Element<*> | Array<React$Element<*>>,
  user: Identity,
  route: RouteConfig,
  router: LocationRouter,
  location: Location,
  logout: any,
  state: *
};

export class App extends React.Component {
  props: AppProps;

  render () {
    const { children } = this.props;
    return (
      <div>
        <Modal/>
        <main className='container-fluid'>
          <div className='content'>
            {children}
          </div>
        </main>
      </div>
    );
  }
}

export default connect(
  (state) => {
    return {
      user: state.auth.identity,
      state
    };
  },
  { logout }
)(withRouter(App));
