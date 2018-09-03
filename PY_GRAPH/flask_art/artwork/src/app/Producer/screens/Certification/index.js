// @flow
import React, { Children } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router';

type CertificationProps = {
  children: React$Element<*> | Array<React$Element<*>>
};

export class Certifications extends React.Component {
  props: CertificationProps;

  render () {
    const { children } = this.props;
    return (
      <div className='content-container'>
        {children}
      </div>
    );
  }
}

export default connect(undefined, {})(withRouter(Certifications));
