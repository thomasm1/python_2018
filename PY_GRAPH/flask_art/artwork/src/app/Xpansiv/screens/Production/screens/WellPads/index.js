// @flow
import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router';

import ProductionBarGraph from 'components/Charts/Production';
import type { Location, LocationRouter, RouteConfig } from 'react-router';
import { Breadcrumb } from 'components/Breadcrumb';
import { Datagrid } from 'components/Datagrid';
import { PageHeader } from 'components/PageHeader';
import Pagination from 'components/Pagination';
import { Paper } from 'components/Paper';
import { Table, Column } from 'components/Table';
import { Tabs } from 'components/Tabs';
import { startCase, times, get, map, random } from 'lodash';
import { statusColor } from 'utils/formatter';
import styles from './styles.less';

type WellpadDetailProps = {
  production: Well,
  provider: any,
  route: RouteConfig,
  router: LocationRouter,
  location: Location,
  params: {
    id: string
  }
};

type Well = {
  id: string,
  status: string,
  timestamp: string,
  meterLocation: string,
  mcfd: number,
  compliance: string,
  action: string
}

export class WellpadDetail extends React.Component {
  props: WellpadDetailProps;

  state: {
    showBackBtn: boolean;
    action: any;
  };

  state = {
    showBackBtn: true,
    action: <div className='btn'>Update Information</div>
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
    const { route, location, router, params  } = this.props;
    const { showBackBtn, action } = this.state;

    const wellPad = [
      { title: 'Well Pad ID', value: 'Big Cat' },
      { title: 'Basin', value: 'Powder River' },
      { title: 'Field', value: 'ig Cat' },
      { title: 'API Number', value: '30-000-1234' },
      { title: 'Input Name', value: 'MS14102/MS14103' },
      { title: 'Latitude', value: '36.2' },
      { title: 'DATUM', value: 'NAD1983' },
      { title: 'Section', value: '26' },
      { title: 'Longitude', value: '-107.25841' }
    ];

    const certDetails = [
      { title: 'Certification Number', value: '12345678' },
      { title: 'Standard Body', value: 'American Carbon Registry' },
      { title: 'Inspector Name', value: 'John Doe' },
      { title: 'Date of Inspection', value: '12/21/2015' },
      { title: 'Date of Expiration', value: '12/21/2016' }
    ];

    const productionData = times(6, () => {
      return {
        id: 'Big Cat FED 2126-4899',
        status: 'Verified',
        timestamp: `2/${random(10,20)}/2016`,
        meterLocation: 'Big Cat FED 2126',
        mcfd: random(163, 234),
        action: ''
      }
    });

    const maintenanceData = times(6, () => {
      return {
        id: 'Big Cat FED 2126-4899',
        status: 'Active',
        compliance: `${random(4,120)} Days`,
        meterLocation: 'Big Cat FED 2126',
        mcfd: random(163, 234),
        action: ''
      }
    });

    return (<div>
      <Breadcrumb location={location}/>
      <PageHeader
        location={location}
        route={route}
        withBackBtn={showBackBtn}
        actions={action}
        customTitle={params.id} />
      <div className='content-container'>
        <h5>{'Well Pad Summary'}</h5>
        <div className={'row'}>
          <Datagrid data={ wellPad }/>
        </div>

        <h5>{'Certification Details'}</h5>
        <div className={'row'}>
          <Datagrid data={ certDetails }/>
        </div>

        <h5>{'CIF Generation'}</h5>
        <div className={'row'}>
          <Paper>
            <ProductionBarGraph />
          </Paper>
        </div>
        <div className='content-container'>
          <h5>{'Production Data'}</h5>
          <div className={'row'}>
            <Table data={productionData}>
              <Column
                name={'Status'}
                render={(c: Well) => <span style={{ color: statusColor(c.status), fontWeight: 500 }}>{startCase(c.status)}</span>}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Timestamp'}
                render={(c: Well) => c.timestamp}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Meter Location'}
                render={(c: Well) => c.meterLocation}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Flow in MCFD'}
                render={(c: Well) => c.mcfd}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Actions'}
                colSpan={2}
                render={ (c: Well) => <i className="fa fa-ellipsis-h"></i> }
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

            </Table>
            <Pagination />
          </div>

          <div className={styles.Maintenance}>
            <h5>{'Maintenance'}</h5>
            <div className='btn secondary right'>Add Maintenance</div>
          </div>
            <div style={{width: 450}}>
              <Tabs/>
            </div>
            <Table data={maintenanceData}>
              <Column
                name={'Status'}
                render={(c: Well) => <span style={{ color: statusColor(c.status), fontWeight: 500 }}>{startCase(c.status)}</span>}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Next Compliance Check'}
                render={(c: Well) => c.compliance}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Meter Location'}
                render={(c: Well) => c.meterLocation}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                colSpan={2}
                name={'Flow in MCFD'}
                render={(c: Well) => c.mcfd}
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

              <Column
                name={'Actions'}
                colSpan={2}
                render={ (c: Well) => <i className="fa fa-ellipsis-h"></i> }
                onClick={(c: Well) => router.push(`/production/${c.id}`)}/>

            </Table>
            <Pagination />
          </div>
        </div>
    </div>);
  }
}

export default connect(undefined, {})(withRouter(WellpadDetail));
