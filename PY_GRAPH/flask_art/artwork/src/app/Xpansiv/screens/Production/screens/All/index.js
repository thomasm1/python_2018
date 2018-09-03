// @flow
import React, { Children } from 'react';

import { connect } from 'react-redux';
import type { ActionCreator } from 'redux';
import { startCase, random, times } from 'lodash';
import styles from './styles.less';
import type { RouteConfig, Location, LocationRouter } from 'react-router';
import Pagination from 'components/Pagination';
import { Table, Column } from 'components/Table';
import { statusColor } from 'utils/formatter';
import { withRouter } from 'react-router';

type ProductionProps = {
  router: LocationRouter,
  location: Location
};

type ProducerItems = {
  logo: string,
  producerName: string,
  lastTransaction: string,
  phoneNumber: string,
  POC: string,
  action: string
}

export class Producers extends React.Component {
  props: ProductionProps;
  onSearchChange: () => void;

  state: {
    showBackBtn: boolean;
    action: any;
    searchFilter: string;
  };

  constructor(props: ProductionProps) {
    super(props);
    this.state = {
      showBackBtn: false,
      action: '',
      searchFilter: ''
    };
    this.onSearchChange = this.onSearchChange.bind(this);
  }

  onSearchChange(event: Event) {
    if (event.target instanceof HTMLInputElement) {
      this.setState({
        searchFilter: event.target.value
      });
    }
  }

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
    const { router, location } = this.props;
    const { showBackBtn, action } = this.state;
    const producerData = [
      { logo: 'carbon-creek', producerName: 'Carbon Creek Energy', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'statoil', producerName: 'Statoil', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'galp', producerName: 'Galp Energia', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'neste', producerName: 'Neste Oil', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'enbridge', producerName: 'Enbridge', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'hess', producerName: 'Hess', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'bg', producerName: 'BG Group', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'baker-hughes', producerName: 'Baker Hughes', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'encana', producerName: 'Encana', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' },
      { logo: 'suncor', producerName: 'Suncor', lastTransaction: `${random(1,12)}/${random(10,20)}/2015`, phoneNumber: `(${random(200,999)}) ${random(200,999)}-${random(3000,9999)}`, POC: 'John Doe', actions: '' }
    ];
    // const filteredRows = this.filterRows(claims, this.state.searchFilter);
    return (
       <div className={styles.Production}>
         <div className='content-container'>
            <h3 className={'producer-header'}>{'Producers'}</h3>
            <div className={'row'}>
              <Table data={ producerData }>
                <Column
                  colSpan={1}
                  name={' '}
                  render={(c: ProducerItems) => {
                    return c.logo
                    // $FlowFixMe
                    ? <span><img style={{ height: 50, verticalAlign: 'middle'}} src={require(`../../../../assets/${c.logo}.png`)}/></span>
                    : <span/>
                  }}
                  onClick={(c: ProducerItems) => router.push(`/xpansiv/production/detail`)}
                />
                <Column
                  colSpan={2}
                  name={'Producer Name'}
                  render={(c: ProducerItems) => c.producerName}
                  onClick={(c: ProducerItems) => router.push(`/xpansiv/production/detail`)}
                />
                <Column
                  colSpan={2}
                  name={'Last Transaction'}
                  render={(c: ProducerItems) => c.lastTransaction}
                  onClick={(c: ProducerItems) => router.push(`/xpansiv/production/detail`)}
                />
                <Column
                  colSpan={2}
                  name={'Phone Number'}
                  render={(c: ProducerItems) => c.phoneNumber}
                  onClick={(c: ProducerItems) => router.push(`/xpansiv/production/detail`)}
                />
                <Column
                  colSpan={2}
                  name={'Point of Contact'}
                  render={(c: ProducerItems) => c.POC}
                  onClick={(c: ProducerItems) => router.push(`/xpansiv/production/detail`)}
                />
                <Column
                  name={'Actions'}
                  render={(c: ProducerItems) => <i className="fa fa-ellipsis-h"></i>}
                  onClick={(c: ProducerItems) => router.push(`/xpansiv/production/detail`)}
                />
              </Table>
              <Pagination />
            </div>
          </div>
        </div>
    );
  }

  filterRows(rows: any, filter: any) {
    let filteredRows = rows;
    const regexp = new RegExp(filter);
    filteredRows = rows.filter((row) => {
      return regexp.test(row.id);
    });
    return filteredRows;
  };

}

export default connect()(withRouter(Producers));
