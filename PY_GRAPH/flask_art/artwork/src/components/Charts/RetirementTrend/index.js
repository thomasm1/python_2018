import React from 'react';
const Highcharts = require('highcharts');
const ReactHighcharts = require('react-highcharts');

export default class Chart extends React.Component{

    render() {
      const config = {
        plotOptions: {
          series: {
            pointPadding: 0,
            borderWidth: 0,
            groupPadding: 0.04,
            marker: { fillColor: '#74D9A3' },
            negativeColor: '#569AC6',
            threshold: 1200
          }
        },
        credits: { enabled: false },
        title: { text: false },
        legend: { enabled: false },
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
            categories: [
              '01/16', '02/16',
              '03/16', '04/16', '05/16',
              '06/16', '07/16', '08/16',
              '09/16', '10/16', '11/16',
              '12/16', '01/17', '02/17',
              '03/17', '04/17', '05/17',
              '06/17', '07/17', '08/17',
              '09/17', '10/17', '11/17',
              '12/17'
            ]
          },
          series: [
            {
              type: 'column',
              color: '#74D9A3',
              data: [
                2400, 2150, 610,
                2150, 1950, 610,
                610, 2180, 610,
                280, 110, 1950,
                2200, 1950, 280,
                820, 2210, 2300,
                320, 890, 2150,
                2150, 1940
              ]
            }
          ]
        };

        return <ReactHighcharts config={config}></ReactHighcharts>;
      }
}
