import React, { Component } from 'react';
import cn from 'classnames';
import { ExpansionList, ExpansionPanel } from 'react-md';
import PortfolioExpandDetail from './PortfolioExpansionDetail';
import {
  cyan50, cyan100
} from 'material-ui/styles/colors';
import inkContextTypes from 'react-md/lib/Inks/inkContextTypes';

const portHead  = {  
    fontSize: '1.2rem',
    paddingTop: 15,
    fontWeight: 400,
marginLeft:0,
paddingLeft:0,  
maxWidth:500
} 
const portHeader = { 
textAlign:'center',  
paddingRight:5, 
paddingTop: 15, 
listStyleType:'none',
display:'inline-block',
}
export default class PortfolioExpand extends Component {
  render() {
    return (
      <div>
     
        {!this.props.data?<p> </p>:  
        <div style={{'minWidth':'800px'}}> 
        
         <ExpansionPanel  footer="" style={{textAlign:'center',listStyleType:'none',}} className={ cn({  'md-cell md-cell--12': true },{'col-width':'20%'},) }
                       headerStyle={{fontSize:'1.2em',paddingBottom:15,paddingTop:10,backgroundColor: cyan50}}       
              label={''} secondaryLabel={[ 'Producer',,,,,,,' Quantity ',,,,,,,'Type',,,,,,,'Vintage',,,,,,,'Date']}  
        /> 
        
        
          <ExpansionList style={{ TextAlign:'right'}}  className={cn({ 'md-cell  md-cell--12': true })}>
            {this.props.data.map( (row, index) => (
         
              <ExpansionPanel 
                children={  
                  <PortfolioExpandDetail 
                  key={index} 
                  detailFeedstockUID={row.uid} /*hash*/
                  detailFeedstockStatus={row.status} /*active,retired,market,etc.*/
                  />
                } 
                key={index} 
                headerStyle={{backgroundColor: cyan50,textAlign:'right'}} 
                footer=" "  
                label={''} secondaryLabel={[row.status
                ,,,,,,,row.producer
                ,,,,,,,row.units
                ,,,,,,,row.units_type
                ,,,,,,,row.trans_date]} 
                
                />
            ))}
          </ExpansionList>
        </div>
        }
      </div>
    )
  }
}