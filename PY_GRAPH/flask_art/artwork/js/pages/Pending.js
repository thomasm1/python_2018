import React, { Component } from 'react';
import View from '../components/View';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';

class Pending extends React.Component {
	render(){
		return (
		<div>
			<MuiThemeProvider>
			<AppBar
			title="Portfolio"

			iconClassNameRight="muidocs-icon-navigation-expand-more"
		  /><View />
		   
			</MuiThemeProvider>
		</div>
			)
	}
}

export default Pending; 