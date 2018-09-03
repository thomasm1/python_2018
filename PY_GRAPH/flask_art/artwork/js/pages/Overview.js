import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Paper from 'material-ui/Paper';
import RaisedButton from 'material-ui/RaisedButton';
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

const paperstyle0 = {
  width: '100%',
  margin: 0,
  textAlign: 'center',
  display: 'inline-block',
};
const paperstyle1 = {
  width: 320,
  margin: 20,
  padding: 40,
  textAlign: 'center',
  verticalAlign: 'top',
  display: 'inline-block',
  borderRadius: 40,
   backgroundColor: cyan50,
};

const btnstyle = {
  margin: 12,
};

class Overview extends React.Component {
	render(){
		return (
			<MuiThemeProvider>
				<Paper style={paperstyle0} zDepth={0}>
					<Paper style={paperstyle1} backgroundColor={cyan100} zDepth={1}>
						<p className="overview-heading">Your Portfolio</p>
						<p className="overview-bignumber">9</p>
						<p className="overview-bignumber-desc">Active Holdings</p>
						<p className="overview-bignumber">86,000</p>
						<p className="overview-bignumber-desc">Units LEI</p>
						<RaisedButton href="moms-organic-grocery/portfolio" label="Go to Portfolio" style={btnstyle} />
					</Paper>
					<Paper style={paperstyle1} backgroundColor={cyan100} zDepth={1}>
						<p className="overview-heading">Your Portfolio</p>
						<p className="overview-bignumber">9</p>
						<p className="overview-bignumber-desc">Active Holdings</p>
						<p className="overview-bignumber">86,000</p>
						<p className="overview-bignumber-desc">Units LEI</p>
						<RaisedButton href="moms-organic-grocery/portfolio" label="Go to Portfolio" style={btnstyle} />
					</Paper>
					<Paper style={paperstyle1} backgroundColor={cyan100} zDepth={1}>
						<p className="overview-heading">Your Portfolio</p>
						<p className="overview-bignumber">9</p>
						<p className="overview-bignumber-desc">Active Holdings</p>
						<p className="overview-bignumber">86,000</p>
						<p className="overview-bignumber-desc">Units LEI</p>
						<RaisedButton href="moms-organic-grocery/portfolio" label="Go to Portfolio" style={btnstyle} />
					</Paper>
				</Paper>
			</MuiThemeProvider>
			)
	}
}

export default Overview;