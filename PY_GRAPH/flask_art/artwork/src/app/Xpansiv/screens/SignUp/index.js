// @flow
import React from 'react';
import { withRouter, browserHistory } from 'react-router';
import { connect } from 'react-redux';

import { signup } from 'modules/auth/actions';
import type { CreateUserPayload } from 'modules/auth/definitions';
import styles from './styles.less';

declare type State = {
  email: ?string,
  password: ?string,
  password_confirm: ?string
};

class SignUp extends React.Component {
  state: CreateUserPayload = {
    name: '',
    email: '',
    avatar: '',
    password: '',
    password_confirmation: ''
  };
  props: {
    isLoggedIn: boolean,
    signup: Function
  };
  componentWillMount() {
    !!(this.props.isLoggedIn) && browserHistory.push('/xpansiv');
  }
  componentWillReceiveProps(nextProps) {
    !!(nextProps.isLoggedIn) && browserHistory.push('/xpansiv');
  }
  render() {
    return (
      <div className={styles.Login}>
        <form onSubmit={(e) => {
          e.preventDefault();
          this.props.signup(this.state);
        }}>
          <div className={'row'}>
            <p className={'text-center brand-logo'}><img src={require('app/Xpansiv/assets/xpansiv-logo.png')}/></p>
            <h4 className={'text-center'}>{'Create a new account.'}</h4>
            <p className={'text-center'}>{'Enter your credentials to access your account.'}</p>
          </div>
          <div className="row">
            <div className="input-field">
              <label>{'Email'}</label>
              <input onChange={(e) => this.setState({ email: e.target.value })} id="email" type="email" className="validate"/>
            </div>
          </div>
          <div className="row">
            <div className="input-field">
              <label>{'Password'}</label>
              <input onChange={(e) => this.setState({ password: e.target.value })} id="password" type="password" className="validate"/>
            </div>
          </div>
          <div className="row">
            <div className="input-field">
              <label>{'Password Confirmation'}</label>
              <input onChange={(e) => this.setState({ password_confirmation: e.target.value })} id="password" type="password" className={ this.state.password === this.state.password_confirmation ? 'valid' : 'invalid'}/>
            </div>
          </div>
          <div className="row text-center">
            <button className="btn" type="submit">Signup</button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(
  (state) => {
    return {
      isLoggedIn: state.auth.identity
    };
  },
  { signup }
)(SignUp);
