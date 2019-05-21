import React, {Component} from 'react';

import Radium from 'radium';

import { getSelf } from './actions/usersActions';
import { resizeEvent } from './actions/windowStateActions';

import { connect } from 'react-redux';

// sections
import { Navbar } from './sections/Navbar';
import { LoadingComponent } from './components/LoadingComponent';

/* This is the base*/
class App extends Component {
  static displayName = 'IronBlogger';

  static propTypes = {
    children: React.PropTypes.object,
    dispatch: React.PropTypes.func,
    usersStore: React.PropTypes.object,
  };

  constructor(props) {
    super(props);
  }

  handleResize = () => {
    const {dispatch} = this.props;
    dispatch(resizeEvent());
  };

  componentWillMount() {
    // populate the user and windowState stores
    window.addEventListener('resize', this.handleResize);
    this.props.dispatch(getSelf());
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.handleResize);
  }

  render() {
    const style = {
      backgroundColor: '#ffffff',
      boxSizing: 'border-box',
      color: '#333332',
      display: 'inline-block',
      fontFamily: "Lato, 'Helvetica Neue', Helvetica, Arial, sans-serif",
      fontSize: '18px',
      marginLeft: 'auto',
      marginRight: 'auto',
      paddingLeft: '15px',
      paddingRight: '15px',
      width: '100%',
    };
    // show a loading screen while the usersStore is loading...
    if (this.props.usersStore.meta.listIsLoading === true) {
      return (
        <div key='container' style={style}>
          <LoadingComponent />
        </div>
      );
    }
    return (
      <div key='container' style={style}>
        <Navbar />
        {this.props.children}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    usersStore: state.usersStore,
  };
}

module.exports = connect(mapStateToProps)(Radium(App));