import React from 'react';
import PropTypes from 'prop-types';
import {Chart as GChart} from 'react-google-charts';

class Chart extends React.Component {
  constructor(props) {
    super(props);

    this.onSelect = this.onSelect.bind(this);
  }

  onSelect(selectData) {
    const {chartWrapper} = selectData;
    const chart = chartWrapper.getChart();
    const dataTable = chartWrapper.getDataTable();
    const selection = chart.getSelection();
    if (this.props.setProps) {
      this.props.setProps({selection: selection, dataTable: dataTable});
    }
  }

  render() {
    const {legend_toggle, ...otherProps} = this.props;
    return (
      <GChart
        legendToggle={legend_toggle}
        {...otherProps}
        chartEvents={[{eventName: 'select', callback: this.onSelect}]}
      />
    );
  }
}

export default Chart;
