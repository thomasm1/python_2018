import React, { Component } from 'react';
import cn from 'classnames';
import { ExpansionList, ExpansionPanel } from 'react-md';
import PendingExpandDetail from './PendingExpansionDetail';
import {
  cyan50,
} from 'material-ui/styles/colors';

export default class PendingExpand extends Component {
  render() {
    return (
      <div>
        {!this.props.data?<p>Loading...</p>:
        <div>
          <ExpansionList className={cn({ 'md-cell md-cell--12': true })}>
            {this.props.data.map( (row, index) => (
              <ExpansionPanel 
                children={
                  <PendingExpandDetail 
                  key={index} 
                  detailFeedstockUID={row.uid} /*hash*/
                  detailFeedstockStatus={row.status} /*active,retired,market,etc.*/
                  />
                } 
                key={index} 
                headerStyle={{backgroundColor: cyan50}} 
                footer="" 
                label={row.status} secondaryLabel={[row.producer,row.units,row.units_type,row.trans_date]} 
                />
            ))}
          </ExpansionList>
        </div>
        }
      </div>
    )
  }
}