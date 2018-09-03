import React from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {Tabs, Tab} from 'material-ui/Tabs';
import Slider from 'material-ui/Slider';
import Paper from 'material-ui/Paper';  // Top Navs 
import Menu from 'material-ui/Menu';
import MenuItem from 'material-ui/MenuItem';

import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme'; 
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import AppBar from 'material-ui/AppBar';
import {
  cyan50,
} from 'material-ui/styles/colors';

//import PortfolioTable from '../components/Table';
import PortfolioExpand from '../components/PortfolioExpansion';
//import PortfolioDetail from '../components/PortfolioDetail';
import PropTypes from 'prop-types';
//import Dialog from 'material-ui/Dialog';
//import FlatButton from 'material-ui/FlatButton';
import api from '../utils/api';

const nolist = {
  listStyleType:'none',
  display:'hidden'
}
const styles = { 
    fontSize: '1.2rem',
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
    textAlign: 'center'
  }
  const stylePaper = { 
      fontSize: '1.2em',
      paddingTop: 16,
      marginBottom: 12,
      minHeight:30,
      fontWeight: 400,
      textAlign: 'center'
   
}
/*This test (DetailsExist) was created to keep from sending null data to Portfolio Detail when then page loads.
  The initial state is to have null data for details when the modal is opened.
  When updateDetails is called, it will load the proper data, but not without throwing an error for the initial null data.*/
/*function DetailsExist(props) {
  const dataCustody = props.dataCustody;
  const dataGas = props.dataGas;
  const portfolioItemUID = props.portfolioItemUID;
    if (dataCustody!==null && dataGas!==null && portfolioItemUID!==null) {
          return <PortfolioDetail dataCustody={dataCustody} dataGas={dataGas} portfolioItemUID={portfolioItemUID} />;
    }
    return null;
}*/

function SelectDataSet (props) {
   //var dataViews = ['Active','Retired','On Market']; //This will become params instead of file names -- see utils/api.js  ////  function SelectDataSet PROPS ADJUSTMENT
   var dataViews = ['profiletest.json','profiletest2.json','profiletest3.json']; //This will become params instead of file names -- see utils/api.js
                                                                                                                            ////   function SelectDataSet PROPS ADJUSTMENT
       /*build tabs to navigate between views*/
    return(
      <MuiThemeProvider>  

         <Paper >
        <Tabs style={styles}  className='datatables'   > 
        {dataViews.map(function(portView){ 
    
          return (
          < Tab 
          label={portView} 
          style={stylePaper}
          onClick={props.onSelect.bind(null, portView)} 
          key={portView} 
          >
               </Tab> 
        
        )
     }
   
          )}   
        </Tabs> 
      </Paper>
     </MuiThemeProvider>  
      ) 
}
SelectDataSet.propTypes = {
  selectedSet: PropTypes.string.isRequired,
  onSelect: PropTypes.func.isRequired,
}

export default class Portfolio extends React.Component {
	constructor (props){
    	super(props);
    	this.state = {
      	portfolioListData: null,
        custodyListData: null,
        gasMakeupData: null,
       //selectedSet: 'Active',                                  //// selectedSet     DATA SOURCE ADJUSTMENT HERE
  selectedSet: 'profiletest.json',                                  //// selectedSet      DATA SOURCE ADJUSTMENT
        portfolioItemUID: null,
        //Below: Modal state
        open: false,
    };
    /*Bind context*/
    this.updateSet = this.updateSet.bind(this);
    this.onOpenModal = this.onOpenModal.bind(this);
    this.onCloseModal = this.onCloseModal.bind(this);
}
    /*Update the portfolioItemUID state to display details for port item////////*/
   /* portfolioItemHandler(passupvar) {
      this.setState({
        portfolioItemUID: `${passupvar}`,
        open: true,
      });
      this.updateDetails(passupvar);
    }*/

    /*Modal handlers////////////////////////////////////////////////////////////*/
    onOpenModal = () => {
      this.setState({ open: true });

    };
    onCloseModal = () => {
      this.setState({ open: false });
    };

    /*Fire AJAX request on component mount/////////////////////////////////////*/
    componentDidMount = () => {
      this.setState({ open: true });
    	this.updateSet(this.state.selectedSet)
  	}

    /*Update views handler/////////////////////////////////////////////////////*/
  	updateSet(selection){
    	/*Change the state of the selectedSet -- this could show 'active','retired','put to market',etc*/
    	this.setState(function(){
      		return {
        		selectedSet: selection,
        		portfolioListData: null, /*Kill last tab data*/
            //portfolioItemUID: null, /*Nullify the portUID between tab clicks*/
      		}
    	});
    	/*Grab data via /utils/api.js AJAX request and change the data state*/
    	api.fetchPortfolioList(selection)
      		.then(function(data){
        	this.setState(function(){
          		return {
            		portfolioListData: data
          		}
        	})
    	}.bind(this));
  	}


	render(){
    /*const modalActions = [
      <FlatButton
        label="Close"
        primary={true}
        onClick={this.onCloseModal}
      />,
    ];*/
		return (
      <MuiThemeProvider   >
   
			<div>
				<h2>Portfolio</h2>                   
        {/*<MuiThemeProvider>
          <Dialog
            title="Transaction Details"
            actions={modalActions}
            modal={false}
            open={this.state.open}
            onRequestClose={this.onCloseModal}
            autoScrollBodyContent={true}
          > 
            <DetailsExist dataCustody={this.state.custodyListData} dataGas={this.state.gasMakeupData} portfolioItemUID={this.state.portfolioItemUID} />
          </Dialog>
        </MuiThemeProvider>*/}

				  <SelectDataSet 
            selectedSet={this.state.selectedSet}
            onSelect={this.updateSet}
          />
          

  <br /><br />
  <PortfolioExpand    onSelect={this.state.data}  />
  
          <PortfolioExpand data={this.state.portfolioListData}/> 
			</div>
      </MuiThemeProvider>
			)
	}
}