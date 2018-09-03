import React from 'react';

import { map, random, sortBy, sum, times } from 'lodash';

const  dummyData = [8397,10091,12882,12902,13744,14183,14220,15068,15311,17679,18254,21675,22871,23133,23463,24225,25471,26544,27191,28854,28898,29096,29157,29558,30263,30804,30890,31093,31941,32291,32677,33904,34741,34763,37585,37778,38675,39126,1894108,9252581]

export default class CIFSlider extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      value: [0, 40000],
      rawValue: 0,
      slidePercent: 0

    };
    this.onSliderChange = this.onSliderChange.bind(this);
  }

  onSliderChange(value) {
    this.setState({
      value,
    });
  }

  sliderChange(e) {
    const minp = 0;
    const maxp = 100;
    const minv = Math.log(Math.min(...dummyData));
    const maxv = Math.log(sum(dummyData));
    const scale = (maxv - minv) / (maxp - minp);
    const rawValue = Math.round(Math.exp(minv + scale * (e.target.value - minp)));
    const slidePercent = e.target.value;

    this.setState({ rawValue, slidePercent })
  }

  render() {
      let dummyData = [8397,10091,12882,12902,13744,14183,14220,15068,15311,17679,18254,21675,22871,23133,23463,24225,25471,26544,27191,28854,28898,29096,29157,29558,30263,30804,30890,31093,31941,32291,32677,33904,34741,34763,37585,37778,38675,39126,1894108,9252581]
      const realValues = sortBy(dummyData);
      const breakPoints = realValues.map((number, i) => {
        return (sum(realValues.slice(0, i)) + number);
      });
      dummyData = map(dummyData, (number) => {
        return Math.pow(number, 0.5);
      });

      let ratio = Math.max(...dummyData) / 100;
      dummyData = sortBy(dummyData.map(number => Math.round(number / ratio)));
      // Compare slider value to the sum of the items up to and including the item being mapped. If slider value >= sum, then border = marigold and background color = white,
      // else reverse the color/border.

      const total = sum(dummyData);
      const self = this;
      const bar =() => {
        return(
          <div
            data-value={realValues[i]}
            style={{
              width:`${rawValue}`,
              backgroundColor: `red`,
              height:40
            }}/>
        )
      }
      const yellowBoxes = map(dummyData, (number, i) => {
        const max = self.state.value[1];
        const min = self.state.value[0];
        return (
          <div key={i} style={{
              width: '10px',
              backgroundColor: 'transparent',
              width: `calc(${ number / total * 100 }% - 4.1px)`,
              margin: '0 0 0 2px',
              height: 40,
              border: `1px solid #E9C84A`,
              display: 'inline-block'
            }}>
            <div
              data-value={realValues[i+1]}
              style={{
                backgroundColor: 'white',
                width: `2px`,
                margin: '0 0 0 -3px',
                height: 40,
                border: `none`,
                display: 'inline-block'
              }}/>
          </div>
        )
      });
      return (
        <div style={{width: '100%'}}>
          <div style={{position: 'absolute', width:'100%', margin: '-1px 0 0', maxWidth: '1280px'}}>
            {yellowBoxes}
          </div>
          <div
            style={{height: '39px', backgroundColor: '#E9C84A', width:`${this.state.slidePercent}%`}}
          />
          <input id="slider" defaultValue={0} onChange={(e) => this.sliderChange(e)} type="range" min="0" max="100" />
        </div>
      );
  };
}
