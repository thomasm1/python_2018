import React from 'react';
const Highcharts = require('highcharts');
const ReactHighcharts = require('react-highcharts');
require('highcharts-release/highcharts-more')(ReactHighcharts.Highcharts);

export default class Chart extends React.Component{

  render() {
    const config = {
    plotOptions: {
      line: {
        marker: {
          enabled: false
        }
      },
      columnrange: {
        negativeColor: '#E9C84A',
        pointWidth: 40,
        marker: { fillColor: 'purple'}
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
        '', '03/01', '03/02', '03/03', '03/04', '03/05', '03/06', '03/07',
        '03/08', '03/09', '03/10', '03/11', '03/12', '03/13', '03/14', '03/15',
        '03/16', '03/17', '03/18', '03/19', '03/20', '03/21', '03/22', '03/23'
      ]
    },
    yAxis: {
      gridLineColor: '#F3F3F3',
      gridLineDashStyle: 'shortdash',
      title: { enabled: false }
    },
    legend: {
      enabled: false
    },
    series: [{
      type: 'columnrange',
      color: '#569AC6',
      data: [
        [0,-450,0], [0,0,950],
        [1,-450,0], [1,0,950], //spliting all data that has negative values using the same index
        [2,-750,0], [2,0,870],
        [3,-450,0], [3,0,950],
        [4,-450,0], [4,0,950],
        [5,-750,0], [5,0,870],
        [6,-450,0], [6,0,950],
        [7,-450,0], [7,0,1025],
        [8,-450,0], [8,0,950],
        [9,-450,0], [9,0,950],
        [10,-610,0],[10,0,950],
        [11,-750,0],[11,0,150],
        [12,-450,0],[12,0,280],
        [13,-1100,0],[13,0,750],
        [14,-450,0],[14,0,910],
        [15,-450,0],[15,0,1025],
        [16,-450,0],[16,0,950],
        [17,-750,0],[17,0,870],
        [18,-750,0],[18,0,1025],
        [19,-450,0],[19,0,950],
        [20,-450,0],[20,0,1025],
        [21,-450,0],[21,0,950],
        [22,-450,0],[22,0,825],
        [23,-450,0],[23,0,1025],

      ]
    },{
      type: 'line',
      color: '#BD0FE1',
      data: [
        350, 450, 450,
        475, 590, 600,
        610, 640, 690,
        760, -100, -300,
        -450, -300, -200,
        -50, 0, 10,
        20, 100, 125,
        150, 175, 150
      ]
    }]
    };
    return <ReactHighcharts config={config}></ReactHighcharts>;
  }
}
