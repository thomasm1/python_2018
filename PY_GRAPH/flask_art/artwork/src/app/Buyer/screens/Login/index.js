// @flow
import React from 'react';
import { withRouter, Link } from 'react-router';
import { connect } from 'react-redux';

import { login } from 'modules/auth/actions';
import styles from './styles.less';

import { browserHistory } from 'react-router';

class Login extends React.Component {
  state: {
    email: string,
    password: string
  } = {
    email: '',
    password: ''
  };
  props: {
    isLoggedIn: boolean,
    login: Function
  };
  componentWillMount() {
    !!(this.props.isLoggedIn) && browserHistory.push('/buyer');
  }
  componentWillReceiveProps(nextProps) {
    !!(nextProps.isLoggedIn) && browserHistory.push('/buyer');
  }
  render() {
    return (
      <div className={styles.Login}>
        <form onSubmit={(e) => {
          e.preventDefault();
          this.props.login(this.state.email, this.state.password);
        }}>
          <div className={'row'}>
            <p className={'text-center brand-logo'}><img src={require('app/Buyer/assets/buyer-logo.png')}/></p>
            <h4 className={'text-center login-header'}>{'Login to your account.'}</h4>
            <p className={'text-center'}>{'Enter your credentials to access your account.'}</p>
          </div>
          <div className="row">
            <div className="input-field">
              <label>Email</label>
              <input placeholder="Email your email" onChange={(e) => this.setState({ email: e.target.value })} id="email" type="email" className="validate" />
            </div>
          </div>
          <div className="row">
            <div className="input-field">
              <label>Password</label>
              <input placeholder="Select a password" onChange={(e) => this.setState({ password: e.target.value })} id="password" type="password" className="validate"/>
            </div>
          </div>
          <div className="row text-center">
            <button className="btn" type="submit">Login</button>
          </div>
          <p className="text-center">
            <small>{`Don't have an account? Create one `}<Link to={'/buyer/signup'}>{'here'}</Link></small>
          </p>
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
  { login }
)(Login);
