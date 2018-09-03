// @flow
import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import { isArray } from 'lodash';
import styles from './styles.less';
import { Paper } from 'components/Paper';

export type ModalProps = {
  children?: React$Element<*>,
  className?: string | Array<string>,
  style?: *,
  modal: any
};

class Modal extends React.Component {
  props: any;

  footerSubmit(type) {
    switch (type) {
      case 'retire':
        return 'Retire CIF';
      case 'transfer':
        return 'Transfer CIFs';
      default:
        return 'Submit';
    }
  }

  content() {
    switch (this.props.modal.type) {
      case 'retire':
        return <Retire />;
      case 'transfer':
        return <Transfer />;
      case 'audit':
        return <Audit />;
      case 'sale':
        return <ForSale />;
      case'retired':
        return <Retired />;
      case'transactions':
        return <Transactions />;
      default: return <Transfer />;
    }
  }

  render() {
    const {children, modal: {type} } = this.props;
    return (
      <div className={'styles.Modal modal'} id='modal1'>
        <i className={'modal-action modal-close material-icons modal-close-icon'}>close</i>
        	{this.content()}
          <div className={'modal-footer text-center'}>
            <a className={'modal-action modal-close btn'}>{this.footerSubmit(type)}</a>
            <a className={'modal-action modal-close btn secondary'}>{'Cancel'}</a>
          </div>
      </div>
    );
  }
};

const Retire = () => {
  return (
    <div>
      {renderHeader('Retire CIF', 'Are you sure you want to perform this task?')}
      <div className={'modal-content'}>
        <div className={'text-center'} style={{color: '#6C7480', fontWeight: 100, fontSize: 20}}>
          {'By Selecting Retire CIF you are claiming the CIF as your own and permanently preventing it from being transacted on the network. Pelase select Retire CIF to appprove or Cancel to cancel.'}
          <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>1,582</h2>
                <p style={{fontSize: 14, color: '#4C5159'}}>{'Total CIFs Owned'}</p>
              </Paper>
            </div>
          </div>
          <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'} >
                <div style={{margin: '50px auto 0', maxWidth: 134, borderBottom: '4px solid #52A0D7'}} />
                <p style={{fontSize: 14, color : '#4C5159'}}>{'Select CIFs for Transfer'}</p>
              </Paper>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

const Transfer = () => {
  return (
    <div>
      {renderHeader('Transfer CIFs', 'Are you sure you want to perform this task?')}
      <div className={'modal-content'}>
        <div className={'text-center'} style={{color: '#6C7480', fontWeight: 100, fontSize: 20}}>
          {'By Selecting Transfer CIF you are transferring ownership of the selected tranche size to the buying party . Pelase select Transfer CIF to appprove or Cancel to cancel.'}      <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>1,582</h2>
                <p style={{fontSize: 14, color: '#4C5159'}}>{'Total CIFs Owned'}</p>
              </Paper>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

const Audit = () => {
  return (
    <div>
      {renderHeader('Audit CIFs')}
      <div className={'modal-content'}>
        <div className={'text-center'} style={{color: '#6C7480', fontWeight: 100, fontSize: 20}}>
          {'By Selecting Transfer CIF you are transferring ownership of the selected tranche size to the buying party . Pelase select Transfer CIF to appprove or Cancel to cancel.'}      <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>1,582</h2>
                <p style={{fontSize: 14, color: '#4C5159'}}>{'Total CIFs Owned'}</p>
              </Paper>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

const ForSale = () => {
  return (
    <div>
      {renderHeader('CIFs For Sale')}
      <div className={'modal-content'}>
        <div className={'text-center'} style={{color: '#6C7480', fontWeight: 100, fontSize: 20}}>
          {'By Selecting Transfer CIF you are transferring ownership of the selected tranche size to the buying party . Pelase select Transfer CIF to appprove or Cancel to cancel.'}      <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>1,582</h2>
                <p style={{fontSize: 14, color: '#4C5159'}}>{'Total CIFs Owned'}</p>
              </Paper>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

const Retired = () => {
  return (
    <div>
      {renderHeader('Retired CIFs')}
      <div className={'modal-content'}>
        <div className={'text-center'} style={{color: '#6C7480', fontWeight: 100, fontSize: 20}}>
          {'By Selecting Transfer CIF you are transferring ownership of the selected tranche size to the buying party . Pelase select Transfer CIF to appprove or Cancel to cancel.'}      <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>1,582</h2>
                <p style={{fontSize: 14, color: '#4C5159'}}>{'Total CIFs Owned'}</p>
              </Paper>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

const Transactions = () => {
  return (
    <div>
      {renderHeader('CIF Transaction History')}
      <div className={'modal-content'}>
        <div className={'text-center'} style={{color: '#6C7480', fontWeight: 100, fontSize: 20}}>
          {'By Selecting Transfer CIF you are transferring ownership of the selected tranche size to the buying party . Pelase select Transfer CIF to appprove or Cancel to cancel.'}      <div className={'row'}>
            <div className={'col s5'} style={{ margin: '0 auto', float: 'initial' }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>1,582</h2>
                <p style={{fontSize: 14, color: '#4C5159'}}>{'Total CIFs Owned'}</p>
              </Paper>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

function renderHeader(title, subtitle = 'Subtitle goes here') {
  return (
    <div>
      <h1 className={'modal-title text-center'}>{title}</h1>
      <h6 className={'modal-subtitle text-center'}>{subtitle}</h6>
    </div>
  )
}

function mapStateToProps(state) {
  return { modal: state.modal }
}
export default connect(mapStateToProps, {})(withRouter(Modal));
