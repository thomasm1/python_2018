import React from 'react';
import { connect } from 'react-redux';
import { withRouter, router } from 'react-router';
import type { Location, LocationRouter, RouteConfig } from 'react-router';

import CIFvsGasProduction from 'components/Charts/CIFvsGasProduction';
import CIFGeneration from 'components/Charts/CIFGeneration';
import Pagination from 'components/Pagination';
import ProductionEfficiency from 'components/Charts/ProductionEfficiency';
import styles from './styles.less';
import { Paper } from 'components/Paper';
import { Table, Column } from 'components/Table';
import { startCase, times, random } from 'lodash';
import { statusColor } from 'utils/formatter';

type HomeProps = {
  router: LocationRouter,
  location: Location
};

type ActionItems = {
  id: String,
  status: String,
  inspector: String,
  DOI: String,
  DOE: String,
  nextStep: String,
  certification: Number,
  action: String
}

export class Home extends React.Component {
  props: HomeProps;

  render () {
    const {
      router, location
    } = this.props;

    const producerData = [
      { logo: 'carbon-creek', producerName: 'Carbon Creek Energy', availableCIFs: '2,030,000', AvgDailyProduction: '30,000', CIFEfficiency: '87%', actions: '' },
      { logo: 'statoil', producerName: 'Statoil', availableCIFs: '3,150,249', AvgDailyProduction: '40,000', CIFEfficiency: '85%', actions: '' },
      { logo: 'galp', producerName: 'Galp Energia', availableCIFs: '5,125,230', AvgDailyProduction: '50,000', CIFEfficiency: '67%', actions: '' },
      { logo: 'encana', producerName: 'Encana', availableCIFs: '400,000', AvgDailyProduction: '10,000', CIFEfficiency: '90%', actions: '' },
      { logo: 'enbridge', producerName: 'Enbridge', availableCIFs: '4,900,000', AvgDailyProduction: '365,000', CIFEfficiency: '78%', actions: '' }
    ];

    const buyerData = [
      { logo: 'engie', buyerName: 'Engie', purchasedCIFs: '100,000', retiredCIFs: '20,000', lastActive: '12/1/2015', actions: ''},
      { logo: 'nrg', buyerName: 'NRG', purchasedCIFs: '20,000,000', retiredCIFs: '1,500,000', lastActive: '11/8/2015', actions: ''},
      { logo: 'nextera', buyerName: 'Nextera Energy', purchasedCIFs: '5,000,000', retiredCIFs: '5,000,000', lastActive: '12/31/2015', actions: ''},
      { logo: 'exelon', buyerName: 'Exelon Energy', purchasedCIFs: '4,000,000', retiredCIFs: '1,000,000', lastActive: '3/1/2016', actions: ''},
      { logo: 'edison', buyerName: 'Edison International', purchasedCIFs: '15,000,000', retiredCIFs: '14,750,000', lastActive: '10/31/2016', actions: ''}
    ];

    const actionData =  [
    {
      status: 'alert',
      wellpad: 'Big Cat FED 2126-4899',
      basin: 'Powder River',
      field: 'Big Cat',
      reason: 'Currently out of compliance',
      actions: ''
    }].concat(times(4, () => {
      return {
        status: 'attention required',
        wellpad: 'Big Cat FED 2126-4899',
        basin: 'Powder River',
        field: 'Big Cat',
        reason: 'Compliance measure needed',
        action: ''
      }
    }));

    return (
      <div>
        <div className='content-container'>
          <h2 className={'producer-header'}>{'CIF Generation'}</h2>
          <h5>{'CIF Generation by Producer'}</h5>
          <div className={'row'}>
            <div className={'col s4'} style={{ padding: 12.5, paddingLeft: 0 }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>30,000,000</h2>
                <p>{'Total CIFs Generated'}</p>
              </Paper>
            </div>
            <div className={'col s4'} style={{ padding: 12.5 }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>2,500,000</h2>
                <p>{'Total CIFs Transferred'}</p>
              </Paper>
            </div>
            <div className={'col s4'} style={{ padding: 12.5, paddingRight: 0 }}>
              <Paper className={'text-center'}>
                <h2 className={"overview-stats"}>2,000,000</h2>
                <p>{'Retired CIFs'}</p>
              </Paper>
            </div>
          </div>
          <div className={'row'}>
            <h5>{'Production Efficiency'}</h5>
            <Paper>
              <ProductionEfficiency />
            </Paper>
          </div>
          <div className={'row'}>
            <div className="col s6">
              <h5>{'Hourly Global CIF Production'}</h5>
              <div className={'row'}>
                <Paper style={{ marginTop: 35 }}>
                  <CIFGeneration />
                </Paper>
              </div>
            </div>
            <div className="col s6">
              <h5>{'CIF Production v Gas Production'}</h5>
              <div className={'row'}>
                <Paper style={{ marginTop: 35 }}>
                  <CIFvsGasProduction />
                </Paper>
              </div>
            </div>
          </div>
          <h5>{'Action Items'}</h5>
          <div className={'row'}>
            <Table data={ actionData }>
              <Column
                colSpan={2}
                name={'Status'}
                render={(c: ActionItems) => <li style={{ color: statusColor(c.status) }}>{startCase(c.status)}</li>}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/wellpads/detail`)}
              />
              <Column
                colSpan={2}
                name={'Well Pad ID'}
                render={(c: ActionItems) => c.wellpad}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/wellpads/detail`)}
              />
              <Column
                colSpan={2}
                name={'Basin'}
                render={(c: ActionItems) => c.basin}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/wellpads/detail`)}
              />
              <Column
                colSpan={2}
                name={'Field'}
                render={(c: ActionItems) => c.field}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/wellpads/detail`)}
              />
              <Column
                colSpan={2}
                name={'Reason'}
                render={(c: ActionItems) => c.reason}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/wellpads/detail`)}
              />
              <Column
                name={'Actions'}
                render={(c: ActionItems) => <i className="fa fa-ellipsis-h"></i>}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/wellpads/detail`)}
              />
            </Table>
          </div>
          <h5>{'Producers'}</h5>
          <div className={'row'}>
            <Table data={ producerData }>
              <Column
                colSpan={1}
                name={' '}
                render={(c: ActionItems) => {
                  return c.logo
                  ? <span><img style={{height: 50, verticalAlign: 'middle'}} src={require(`../../assets/${c.logo}.png`)}/></span>
                  : <span/>
                }}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/detail`)}
              />
              <Column
                colSpan={2}
                name={'Producer Name'}
                render={(c: ActionItems) => c.producerName}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/detail`)}
              />
              <Column
                colSpan={2}
                name={'Available CIFs'}
                render={(c: ActionItems) => c.availableCIFs}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/detail`)}
              />
              <Column
                colSpan={2}
                name={'Average Daily Production'}
                render={(c: ActionItems) => c.AvgDailyProduction}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/detail`)}
              />
              <Column
                colSpan={2}
                name={'CIF Efficiency %'}
                render={(c: ActionItems) => c.CIFEfficiency}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/detail`)}
              />
              <Column
                name={'Actions'}
                render={(c: ActionItems) => <i className="fa fa-ellipsis-h"></i>}
                onClick={(c: ActionItems) => router.push(`/xpansiv/production/detail`)}
              />
            </Table>
            <Pagination />
          </div>

          <h5>{'Buyers'}</h5>
          <div className={'row'}>
            <Table data={ buyerData }>
              <Column
                colSpan={1}
                name={' '}
                render={(c: ActionItems) => {
                  return c.logo
                  ? <span><img style={{height: 50, verticalAlign: 'middle'}} src={require(`../../assets/${c.logo}.png`)}/></span>
                  : <span/>
                }}
                onClick={(c: ActionItems) => router.push(`/xpansiv/buyers/detail`)}
              />
              <Column
                colSpan={2}
                name={'Buyer Name'}
                render={(c: ActionItems) => c.buyerName}
                onClick={(c: ActionItems) => router.push(`/xpansiv/buyers/detail`)}
              />
              <Column
                colSpan={2}
                name={'CIFs Purchased'}
                render={(c: ActionItems) => c.purchasedCIFs}
                onClick={(c: ActionItems) => router.push(`/xpansiv/buyers/detail`)}
              />
              <Column
                colSpan={2}
                name={'CIFS Retired'}
                render={(c: ActionItems) => c.retiredCIFs}
                onClick={(c: ActionItems) => router.push(`/xpansiv/buyers/detail`)}
              />
              <Column
                colSpan={2}
                name={'Last Active'}
                render={(c: ActionItems) => c.lastActive}
                onClick={(c: ActionItems) => router.push(`/xpansiv/buyers/detail`)}
              />
              <Column
                name={'Actions'}
                render={(c: ActionItems) => <i className="fa fa-ellipsis-h"></i>}
                onClick={(c: ActionItems) => router.push(`/xpansiv/buyers/detail`)}
              />
            </Table>
            <Pagination />
          </div>
        </div>
      </div>
    );
  }
}

export default connect(undefined, {} )(withRouter(Home));
