import React from 'react';
const Highcharts = require('highcharts');
const ReactHighcharts = require('react-highcharts');
import { map, times, constant } from 'lodash';

export default class Chart extends React.Component{

  componentDidMount() {
    this.chart = this.refs.chart.getChart();
  }

  render() {
    const self = this;
    const data = [
      650, 800, 610,
      750, 675, 925,
      910, 1050, 700,
      1500, 1650, 1900,
      1200, 1500, 1400,
      1800, 1700, 2000,
      2100, 1950, 2150,
      2300, 2100, 1800
    ]
    const categories = [
      '', '01:00', '02:00',
      '03:00', '04:00', '05:00',
      '06:00', '07:00', '08:00',
      '09:00', '10:00', '11:00',
      '12:00', '13:00', '14:00',
      '15:00', '16:00', '17:00',
      '18:00', '19:00', '20:00',
      '21:00', '22:00', '23:00',
    ]

    const config = {
      animation: false,
      credits: { enabled: false },
      tooltip: {
        crosshairs: {
          width: 1.5,
          color: '#9eeec5',
          dashStyle: 'solid'
        },
        formatter: () => {return false;}
      },
      title: { text: false },
      legend: false,
      yAxis: {
        tickInterval: 300,
        gridLineDashStyle: 'shortdash',
        title: { enabled: false },
        gridLineColor: '#F3F3F3',
      },
      xAxis: {
        tickInterval: 1,
        tickmarkPlacement: 'on',
        gridLineWidth: 1,
        gridLineDashStyle: 'shortdash',
        gridLineColor: '#F3F3F3',
        categories
      },
      plotOptions: {
        area: {
          fillOpacity: 0.2,
          animation: false
        },
        line: {
          animation: false
        },
        series: {

          marker: {
            enabled: false,
            symbol: 'circle',
            radius: 3,
            states: {
              hover: {
                fillColor: 'white',
                lineColor: 'rgba(0, 0, 0, .4)',
                lineWidth: 4
              }
            }
          },
          point: {
            events: {
              mouseOver: function() {
                const { index, series } = this;
                let firstHalf1 = map(data.slice(0, index + 1), (value, i) => {
                  return {x: i, y: null}
                });

                let secondHalf1 = map(data, (value, i) => {
                  return {x: i, y: value}
                }).slice(index, data.length);

                let firstHalf0 = map(data.slice(0, index + 1), (value, i) => {
                  return {x: i, y: value}
                });

                let secondHalf0 = map(data, (value, i) => {
                  return {x: i, y: null}
                }).slice(index, data.length);

                self.chart.series[0].setData(firstHalf0.concat(secondHalf0), false, false);
                self.chart.series[1].setData(firstHalf1.concat(secondHalf1), true, false);
              }
            }
          }
        }
      },
      series: [
        {
          type: 'area',
          color: '#86E9B7',
          fill: '#7FDEAD',
          shadow: {color: '#86E9B7', width: '13', opacity: '0.05'},
          data: times(data.length, constant(null))
        }, {
          type: 'line',
          color: '#569AC6',
          shadow: {color: '#569AC6', width: '13', opacity: '0.05'},
          data: data
        }, {
          type: 'line',
          color: 'transparent',
          data: data,
          showInLegend: false
        }
      ]
    };
    return <ReactHighcharts config={config} ref="chart"></ReactHighcharts>;
  }
}
