import React from 'react';
const Highcharts = require('highcharts');
const ReactHighcharts = require('react-highcharts');

export default class Chart extends React.Component {

  render() {
    const config = {
      chart: {
        type: 'column'
      },
      plotOptions: {
        column: {
          stacking: 'normal'
        },
        series: {
          pointWidth: 40,
          marker: { fillColor: 'purple' }
        }
      },
      credits: { enabled: false },
      title: { text: false },
      legend: { enabled: false },
      xAxis: {
        gridLineWidth: 1,
        gridLineDashStyle: 'shortdash',
        gridLineColor: '#F3F3F3',
        categories: [
          ' ', '01:00', '02:00',
          '03:00', '04:00', '05:00',
          '06:00', '07:00', '08:00',
          '09:00', '10:00', '11:00',
          '12:00', '13:00', '14:00',
          '15:00', '16:00', '17:00',
          '18:00', '19:00', '20:00',
          '21:00', '22:00', '23:00']
      },

      yAxis: {
        allowDecimals: false,
        min: 0,
        title: false
      },
      series: [
      {
        name: 'Missed CIFs',
        color: '#E6C041',
        data: [300, 300, 450, 300, 300, 450, 300, 300, 300, 300, 400, 450, 300, 600, 300, 300, 300, 450, 300, 300, 300, 300, 300],
        stack: 'CIF'
      },
      {
        name: 'Total CIFs',
        color: '#4C8FBF',
        data: [2100, 2100, 1950, 2100, 2100, 1950, 2100, 2100, 2100, 2100, 2000, 1950, 2100, 1800, 2100, 2100, 2100, 1950, 2100, 2100, 2100, 2100, 2100],
        stack: 'CIF'
      }
      ]
    };

    return <ReactHighcharts config = { config } > < /ReactHighcharts>;
  }
}
