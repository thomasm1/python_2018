import React, {Component} from 'react';
//import PropTypes from 'prop-types';
import {
  Table,
  TableBody,
  //TableFooter,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import ActionInfo from 'material-ui/svg-icons/action/info';
import IconButton from 'material-ui/IconButton';
import Avatar from 'material-ui/Avatar';
import {
  blue300,
  lightBlue200,
  indigo900,
  orange200,
  deepOrange300,
  pink400,
  purple500,
} from 'material-ui/styles/colors';
const iconStyles = {
  marginRight: 20,
};
const style = {margin: 5};


export default class PortfolioTable extends Component {

  render() {
    return (
      <div>
        {/*This should be rebuild for abstraction. Columns should be dynamic based on input data*/}        
        {/*Shows 'Loading' if no data or shows the table below*/}
        {!this.props.data?<p>Loading...</p>:
        <Table
          height={this.props.height}
          fixedHeader={this.props.fixedHeader}
          fixedFooter={this.props.fixedFooter}
          selectable={this.props.selectable}
          multiSelectable={this.props.multiSelectable}
          onRowSelection={this.onRowSelection}
        >
          <TableHeader
            displaySelectAll={this.props.showCheckboxes}
            adjustForCheckbox={this.props.showCheckboxes}
            enableSelectAll={this.props.enableSelectAll}
          >
            <TableRow>
              <TableHeaderColumn tooltip="Units">Units</TableHeaderColumn>
              <TableHeaderColumn tooltip="Type of Units">Type of Units</TableHeaderColumn>
              <TableHeaderColumn tooltip="Producer">Producer</TableHeaderColumn>
              <TableHeaderColumn tooltip="Transfer Date">Transfer Date</TableHeaderColumn>
              <TableHeaderColumn tooltip="Production Date">Production Date</TableHeaderColumn>
              <TableHeaderColumn tooltip="Status">Status</TableHeaderColumn>
              <TableHeaderColumn tooltip="Info"></TableHeaderColumn>
            </TableRow>
          </TableHeader>
          <TableBody
            displayRowCheckbox={this.props.showCheckboxes}
            deselectOnClickaway={this.props.deselectOnClickaway}
            showRowHover={this.props.showRowHover}
            stripedRows={this.props.stripedRows}
            //ref={(tableBody) => { this.tableBody = tableBody; }}
          >
            {/*Below returns the data. portUIDAction returns uid to parent state to generate details page*/}
            {this.props.data.map( (row, index) => (
              <TableRow key={index} onMouseDown={() => this.props.portUIDAction(`${row.uid}`)}> 
                <TableRowColumn>{row.units}</TableRowColumn>
                <TableRowColumn>{row.units_type}</TableRowColumn>
                <TableRowColumn>{row.producer}</TableRowColumn>
                <TableRowColumn>{row.trans_date}</TableRowColumn>
                <TableRowColumn>{row.prod_date}</TableRowColumn>
                <TableRowColumn>{row.status}</TableRowColumn>
                <TableRowColumn>
                    <ActionInfo style={iconStyles} color={lightBlue200} />
                </TableRowColumn>
              </TableRow>
              ))}
          </TableBody>
        </Table>
      }
      </div>
        );
  }
}
