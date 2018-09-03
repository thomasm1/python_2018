import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Paper from 'material-ui/Paper';
import FlatButton from 'material-ui/FlatButton';
import {
  Table,
  TableBody,
  //TableFooter,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import {
  blue300,
  indigo900,
  orange200,
  deepOrange300,
  pink400,
  purple500,
  cyan50,
  cyan100,
  cyan200,
} from 'material-ui/styles/colors';

const modalbuttonstyles = {
  radioButton: {
    marginTop: 16,
  },
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
  deselectOnClickaway : false,
  stripedRows : true,
  deselectOnClickaway : false
}

export default class PortfolioDetail extends React.Component {
	render(){
		return(
			<div>
				<h3>Digital Feedstock ID: {this.props.portfolioItemUID}</h3>

              <Paper style={paperstyleDetailPanel} zDepth={1}>
                <h3>Details</h3>
                <p>Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?</p>
              </Paper>

           		<Paper style={paperstyleDetailPanel} zDepth={1}>
              <h3>Transaction Chain of Custody</h3>
                {this.props.dataCustody.map((row, index) => (
                  <Paper style={paperstyleDetailSubPanel} backgroundColor={cyan100} zDepth={1}>
                    <div key={index}>
                      <p className="detail-graycaps">{row.trans_type}: {row.trans_date}</p>
                      <p className="detail-description">Transaction ID: {row.uid}</p>
                      <p className="detail-description blue">{row.enterprise}</p>
                      <p className="detail-bignumber">{row.unit_amt}</p>
                      <p className="detail-description-small">Units LEI</p>

                    </div>
                  </Paper>
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
                  {/*Below returns the data. portUIDAction returns uid to parent state to generate details page*/}

                  {this.props.dataGas.map( (row, index) => (
                    <TableRow key={index}> 
                      <TableRowColumn>{row.Gas_Type}</TableRowColumn>
                      <TableRowColumn>{row.Volume} MCF</TableRowColumn>
                    </TableRow>
                  ))}
                  </TableBody>
                </Table>
            	</Paper>

     </div>
        )};
}