import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import PortfolioTable from '../components/Table';
import PortfolioDetail from '../components/PortfolioDetail';
import PropTypes from 'prop-types';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import api from '../utils/api';


export default class Manage extends React.Component {
	constructor (props){
    	super(props);
    	this.state = {
      	data: null,
      	selectedSet: 'profiletest.json',
      	//Below: table state elements to be passed as props to the table component
      	columns: null,
      	fixedHeader: true,
      	fixedFooter: true,
      	stripedRows: true,
      	showRowHover: false,
      	selectable: true,
      	multiSelectable: false,
      	enableSelectAll: false,
      	deselectOnClickaway: true,
      	showCheckboxes: false,
      	height: '600px',
      	onClick: true,
        //Below: UID var state to display details after clicking a table row
      	portfolioItemUID: null,
        //Below: Modal state
        open: false,
    };
    /*Bind context*/
    this.updateSet = this.updateSet.bind(this);
    this.portfolioItemHandler = this.portfolioItemHandler.bind(this);
    this.onOpenModal = this.onOpenModal.bind(this);
    this.onCloseModal = this.onCloseModal.bind(this);
}

    /*Update the portfolioItemUID state to display details for port item*/
    portfolioItemHandler(passupvar) {
      this.setState({
        portfolioItemUID: `${passupvar}`,
        open: true
      });
    }

    /*Modal handlers*/
    onOpenModal = () => {
      this.setState({ open: true });
    };
    onCloseModal = () => {
      this.setState({ open: false });
    };

    /*Fire AJAX request on component mount*/
    componentDidMount () {
    	this.updateSet(this.state.selectedSet)
  	}

    /*Update views handler*/
  	updateSet(selection){
    	/*Change the state of the selectedSet -- this could show 'active','retired','put to market',etc*/
    	this.setState(function(){
      		return {
        		data: null, /*Kill old data*/
            portfolioItemUID: null, /*nullify the portUID between tab clicks*/
          }
    	});
    	/*Grab data via /utils/api.js AJAX request and change the data state*/
    	api.fetchPopularRepos(selection)
      		.then(function(data){
        	this.setState(function(){
          		return {
            		data: data
          		}
        	})
    	}.bind(this));
  	}

	render(){
    const modalActions = [
      <FlatButton
        label="Close"
        primary={true}
        onClick={this.onCloseModal}
      />,
    ];
    //console.log("testsend:",this.state.portfolioItemUID)
		return (
			<div>
				<h2>Portfolio</h2>
        <MuiThemeProvider>
          <Dialog
            title="Transaction Details"
            actions={modalActions}
            modal={false}
            open={this.state.open}
            onRequestClose={this.onCloseModal}
            autoScrollBodyContent={true}
          > 
            <PortfolioDetail portfolioItemUID={this.state.portfolioItemUID} />
          </Dialog>
					
          <PortfolioTable 
				    data={this.state.data}
						columns={this.state.columns}
      			fixedHeader={this.state.fixedHeader}
      			fixedFooter={this.state.fixedFooter}
      			stripedRows={this.state.stripedRows}
      			showRowHover={this.state.showRowHover}
      			selectable={this.state.selectable}
      			multiSelectable={this.state.multiSelectable}
      			enableSelectAll={this.state.enableSelectAll}
      			deselectOnClickaway={this.state.deselectOnClickaway}
      			showCheckboxes={this.state.showCheckboxes}
      			height={this.state.height}
            portUIDAction={this.portfolioItemHandler}
      		/>
				</MuiThemeProvider>
			</div>
			)
	}
}