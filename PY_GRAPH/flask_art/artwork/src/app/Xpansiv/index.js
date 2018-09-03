import React from 'react';
import { connect } from 'react-redux';
import { withRouter, browserHistory } from 'react-router';

import { logout } from 'modules/auth/actions';

import Appbar from 'components/Appbar/index';

class Producer extends React.Component {
  componentWillMount() {
    if (!this.props.user) {
      browserHistory.push('/xpansiv/login');
    }
  }

  shouldComponentUpdate(nextProps: AppProps) {
    if (!nextProps.user) {
      browserHistory.push('/xpansiv/login');
      return false;
    }
    return true;
  }

  render() {
    const { user, logout, location } = this.props;
    const paths = [
      {path:'/xpansiv', pathname: 'Home'},
      {path:'/xpansiv/production', pathname: 'Producers'},
      {path:'/xpansiv/buyers', pathname: 'Buyers'},
      {path:'/xpansiv/standards', pathname: 'Standards'},
      {path:'/xpansiv/cifs', pathname: 'CIFs'}
      ]
    return (
      <div>
        <Appbar logo={{src: require('./assets/xpansiv-logo.png'), text: ''}} {...{paths, user, logout, location}}/>
        <div className={'appbar-offset'}>
          { this.props.children }
        </div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    user: state.auth.identity
  }
}

export default connect(mapStateToProps, { logout })(withRouter(Producer));
export { routes } from './routes';
