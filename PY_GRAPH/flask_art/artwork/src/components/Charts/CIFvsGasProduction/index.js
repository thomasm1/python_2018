import React from 'react';
const Highcharts = require('highcharts');
const ReactHighcharts = require('react-highcharts');
require('highcharts-release/highcharts-more')(ReactHighcharts.Highcharts);
import { times, random } from 'lodash';

export default class Chart extends React.Component{
  render() {
    const config = {
      chart: { type: 'column' },
      plotOptions: {
        series: {
          pointWidth: 10
        },
        column: {
          pointPadding: 0,
          borderWidth: 0,
          groupPadding: 0
        }
      },
      legend: { enabled: false },
      title: { text: null },
      xAxis: {
        gridLineWidth: 1,
        gridLineDashStyle: 'shortdash',
        gridLineColor: '#F3F3F3',
        categories: [
          '', '01:00', '02:00',
          '03:00', '04:00', '05:00',
          '06:00', '07:00', '08:00',
          '09:00', '10:00', '11:00',
          '12:00', '13:00', '14:00',
          '15:00', '16:00', '17:00',
          '18:00', '19:00', '20:00',
          '21:00', '22:00', '23:00',
        ],
        crosshair: true
      },
      yAxis: {
        startOnTick: false,
        endOnTick: false,
        title: { text: null },
        maxPadding: 0.2
      },
      credits: { enabled: false },
      tooltip: {
        pointFormat: '{point.x: %m/%d}: {point.y} units at ${point.z}',
      },
      series: [{
        name: 'Tokyo',
        color: '#74D9A3',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
      }, {
        name: 'New York',
        color: '#4C8FBF',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]
      }, {
        name: 'London',
        color: '#9D82E6',
        data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]
      }, {
        name: 'Berlin',
        color: '#E6C041',
        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]
      }]
    }
    return <ReactHighcharts config = {config}></ReactHighcharts>;
  }
}
