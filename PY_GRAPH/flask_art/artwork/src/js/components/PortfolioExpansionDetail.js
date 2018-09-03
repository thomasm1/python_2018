import React from 'react';
import api from '../utils/api';
import Paper from 'material-ui/Paper';
import RaisedButton from 'material-ui/RaisedButton';
import PortfolioTransactionDialog from './PortfolioTransactionDialog';
import FlatButton from 'material-ui/FlatButton';
import {
  Table,
  TableBody,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import {
  cyan50,
} from 'material-ui/styles/colors';

const btnStyle = {
  margin: 12,
};
const paperstyleDetailPanel = {
  //height: 400,
  width: '100%',
  marginBottom: 40,
  padding: 40,
  textAlign: 'left',
  display: 'inline-block',
};
const paperstyleDetailSubPanel = {
  //height: 400,
  width: '100%',
  padding: 20,
  marginBottom: 20,
  textAlign: 'left',
  display: 'inline-block',
 };
const tableSetup = {
  column : false,
  height: '400px',
  fixedHeader : false,
  fixedFooter : false,
  selectable : false,
  multiSelectable : false,
  onRowSelection : false,
  displaySelectAll : false,
  displayRowCheckbox : false,
  adjustForCheckbox : false,
  enableSelectAll : false,
  stripedRows : false,
  deselectOnClickaway : false
}

export default class PortfolioExpandDetail extends React.Component {

  constructor (props){
      super(props);
      this.state = {
        portfolioListData: null,
        custodyListData: null,
        gasMakeupData: null,
        sendResponse: null,
        selectedDetail: this.props.detailFeedstockUID,
        selectedFeedstockUID: this.props.detailFeedstockUID,
        selectedTransactionType: null,
        selectedTransactionUnits: null,
        openDialog:false

    };
    /*Bind context*/
    this.updateDetails = this.updateDetails.bind(this);
  }

  /*Fire AJAX request on component mount/////////////////////////////////////*/
  componentDidMount = () => {
    this.updateDetails(this.state.selectedDetail)
  };

     /*Update details handler///////////////////////////////////////////////////*/
    updateDetails(selection){
      /*Change the state of the selectedSet -- this could show 'active','retired','put to market',etc*/
      this.setState(function(){
          return {
            custodyListData: null, /*Kill last tab data*/
          }
      });
      //Grab data via /utils/api.js AJAX request and change the data state
      //Get change of custody data
      api.fetchCustodyDetails(selection)
          .then(function(data){
          this.setState(function(){
              return {
                custodyListData: data,
              }
          })
      }.bind(this));
      //Get gas makeup data
      api.fetchGasMakeup(selection)
          .then(function(data){
          this.setState(function(){
              return {
                gasMakeupData: data,
              }
          })
      }.bind(this));
    }


	render(){
		return(
			<div>
      {!this.state.custodyListData||!this.state.gasMakeupData?<p>Loading...</p>:
     
        <div>
            <h3>Digital Feedstock ID: {this.props.detailFeedstockUID}</h3>
              <Paper style={paperstyleDetailPanel} zDepth={1}>
                <h3>Details</h3>
                <p>Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?</p>
              </Paper>

              <Paper style={paperstyleDetailPanel} zDepth={1}>
              <h3>Transaction Chain of Custody</h3>
                {this.state.custodyListData.map((row, index) => (
                  <div key={index}>
                  <Paper key={index} style={paperstyleDetailSubPanel} backgroundcolor={cyan50} zDepth={1}>
                    <div>
                      <p className="detail-graycaps">{row.trans_type}: {row.trans_date}</p>
                      <p className="detail-description">Transaction ID: {row.uid}</p>
                      <p className="detail-description blue">{row.enterprise}</p>
                      {/*below: Odd problem with trying to update the units state holder, it displays the amount instead of just updating the variable. This is a solution for now.*/}
                      <p className="detail-bignumber">{this.state.selectedTransactionUnits = row.unit_amt}</p> 
                      <p className="detail-description-small">Units LEI</p>
                    </div>
                  </Paper>
                  </div>
                ))}
              </Paper>

              <Paper style={paperstyleDetailPanel} zDepth={1}>
              <h3>Gas by Volume</h3>
                <Table
                  height={tableSetup.height}
                  fixedHeader={tableSetup.fixedHeader}
                  fixedFooter={tableSetup.fixedFooter}
                  selectable={tableSetup.selectable}
                  multiSelectable={tableSetup.multiSelectable}
                >
                  <TableHeader
                    displaySelectAll={tableSetup.displaySelectAll}
                    adjustForCheckbox={tableSetup.adjustForCheckbox}
                    enableSelectAll={tableSetup.enableSelectAll}
                  >
                    <TableRow>
                      <TableHeaderColumn>Gas Type</TableHeaderColumn>
                      <TableHeaderColumn>Volume</TableHeaderColumn>
                    </TableRow>
                  </TableHeader>
                  <TableBody
                    displayRowCheckbox={tableSetup.displayRowCheckbox}
                    deselectOnClickaway={tableSetup.deselectOnClickaway}
                    showRowHover={tableSetup.showRowHover}
                    stripedRows={tableSetup.stripedRows}
                    //ref={(tableBody) => { this.tableBody = tableBody; }}
                  >

                  {this.state.gasMakeupData.map( (row, index) => (
                    <TableRow key={index}> 
                      <TableRowColumn>{row.Gas_Type}</TableRowColumn>
                      <TableRowColumn>{row.Volume} MCF</TableRowColumn>
                    </TableRow>
                  ))}
                  </TableBody>
                </Table>
              </Paper>

              {/*Make the transaction Dialog*/}
              <PortfolioTransactionDialog detailFeedstockStatus={this.props.detailFeedstockStatus} detailFeedstockUID={this.props.detailFeedstockUID} selectedTransactionUnits={this.state.selectedTransactionUnits} />

        </div>
      }
     </div>
    )};
}