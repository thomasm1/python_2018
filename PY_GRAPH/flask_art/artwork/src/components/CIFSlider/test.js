import React from 'react';

import { map, random, sortBy, sum, times } from 'lodash';

const  dummyData = [8397,10091,12882,12902,13744,14183,14220,15068,15311,17679,18254,21675,22871,23133,23463,24225,25471,26544,27191,28854,28898,29096,29157,29558,30263,30804,30890,31093,31941,32291,32677,33904,34741,34763,37585,37778,38675,39126,1894108,9252581]

export default class CIFSlider extends React.Component{

    constructor(props) {
      super(props);
      this.state = {
        value: [0, 40000],
        rawValue: 0

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

      // calculate adjustment factor
      const scale = (maxv - minv) / (maxp - minp);
      // console.log('scale: ', scale);
      // console.log('Dummy data: ', dummyData);
      //console.log('minv: ', minv);
      //console.log('maxv: ', maxv);
      const rawValue = Math.round(Math.exp(minv + scale * (e.target.value - minp)));
      //console.log('Raw Value: ', rawValue);
      this.setState({ rawValue })
    }

    render() {
        // let dummyData = times(2, random.bind(5000000, 10000000))
        // dummyData = sortBy(dummyData.concat(times(38, () => {
        //   return random(8000, 40000)
        // })));

        // Hard coded dummy data to get consistent behavior for now
        let dummyData = [8397,10091,12882,12902,13744,14183,14220,15068,15311,17679,18254,21675,22871,23133,23463,24225,25471,26544,27191,28854,28898,29096,29157,29558,30263,30804,30890,31093,31941,32291,32677,33904,34741,34763,37585,37778,38675,39126,1894108,9252581]

        // Subtracts lowest value from array;
        const nMinusOne = dummyData.map((number, i) => {
          return number - Math.min(...dummyData);
        });

        // Removes first item in array
        nMinusOne.shift();

        const arrayOfDifferences = nMinusOne.map((number, i) => {
          if (i > 0 ) return nMinusOne[i] - nMinusOne[i - 1];
        })
        // Gets the log of each value
        const logOfEach = arrayOfDifferences.map((number, i) => {
          return Math.log(number);
        });

        console.log(logOfEach);

        // Gets the cumulative sum of each value in the logOfEach array
        const cumulativeSum = logOfEach.map((number, i) => {
          return (sum(logOfEach.slice(0, i + 1)));
        })

        console.log(cumulativeSum);

        const widths  =
          [0].concat(cumulativeSum.map((number, i) => { return Math.ceil(number * 100 / Math.max(...cumulativeSum))}));

        console.log(widths);

        dummyData = map(dummyData, (number) => {
          return Math.pow(Math.log(number), 4);
        });
       // console.log('DummyData: ')
        //console.log(dummyData)
        let ratio = Math.max(...dummyData) / 100;
        dummyData = sortBy(dummyData.map(number => Math.round(number / ratio)));
        //console.log(dummyData);
        // Compare slider value to the sum of the items up to and including the item being mapped. If slider value >= sum, then border = marigold and background color = white,
        // else reverse the color/border.

        const total = sum(dummyData);
        const self = this;
        const yellowBoxes = map(widths, (number, i) => {
          const max = self.state.value[1];
          const min = self.state.value[0];
          //console.log('i: ', i, '   ', realValues[i], '  ', sum(realValues));
          return (
            <div
              style={{
                //backgroundColor: `${ (breakPoints[i] <= max && breakPoints[i] >= min) ? '#E9C84A' : '#FFFFFF'}`,
                //backgroundColor: `${ (breakPoints[i] <= this.state.rawValue) ? '#E9C84A' : '#FFFFFF'}`,
                width: `calc(${ widths[i] - widths[i - 1] }% - 2px)`,
                margin: '0 1px',
                height: 40,
                border: `1px solid #E9C84A`,
                display: 'inline-block'
              }}
            />
          )
        });
        return (
          <div style={{width: '100%'}}>
            { yellowBoxes }
            <input id="slider" defaultValue={0} onChange={(e) => this.sliderChange(e)} type="range" min={dummyData[0]} max="100" />
            <div>{this.state.rawValue}</div>
          </div>
        );
    };
}
