import React from 'react';


export default function HintContent({value}) {
 
  const {volume, production, energy_content} = value;
 
  return (<div>
    <div>{production}</div>
    <div style={{position: 'relative', height: '15px', width: '100%'}}>
      <div style={{position: 'absolute'}}>X-production</div>
      <div style={{position: 'absolute', right: 0}}>{volume}</div>
    </div>
    <div style={{position: 'relative', height: '15px', width: '100%'}}>
      <div style={{position: 'absolute'}}>Y-energy_content</div>
      <div style={{position: 'absolute', right: 0}}>{energy_content}</div>
    </div>
  </div>);
}
