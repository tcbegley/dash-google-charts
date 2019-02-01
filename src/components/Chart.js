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
    const dataTable = chartWrapper.getDataTable()
    const selection = chart.getSelection();
    if (this.props.setProps) {
      this.props.setProps({selection: selection, dataTable: dataTable});
    }
  }

  render() {
    return (
      <GChart
        {...this.props}
        chartEvents={[{eventName: 'select', callback: this.onSelect}]}
      />
    );
  }
}

Chart.propTypes = {
  /**
   * The ID of this component, used to identify dash components
   * in callbacks. The ID needs to be unique across all of the
   * components in an app.
   */
  id: PropTypes.string,

  /**
   * Defines CSS styles which will override styles previously set.
   */
  style: PropTypes.object,

  /**
   * Often used with CSS to style elements with common properties.
   */
  className: PropTypes.string,

  height: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  width: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  graphID: PropTypes.string,
  chartType: PropTypes.oneOf([
    'AnnotationChart',
    'AreaChart',
    'BarChart',
    'BubbleChart',
    'Calendar',
    'CandlestickChart',
    'ColumnChart',
    'ComboChart',
    'DiffChart',
    'DonutChart',
    'Gantt',
    'Gauge',
    'GeoChart',
    'Histogram',
    'LineChart',
    'Line',
    'Bar',
    'Map',
    'OrgChart',
    'PieChart',
    'Sankey',
    'ScatterChart',
    'SteppedAreaChart',
    'Table',
    'Timeline',
    'TreeMap',
    'WaterfallChart',
    'WordTree'
  ]),
  options: PropTypes.object,
  data: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.object),
    PropTypes.object
  ]),
  mapsApiKey: PropTypes.string,
  spreadSheetUrl: PropTypes.string,
  spreadSheetQueryParameters: PropTypes.object,
  formatters: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.object),
    PropTypes.object
  ]),
  legend_toggle: PropTypes.boolean,
  selection: PropTypes.object,
  dataTable: PropTypes.object
};

export default Chart;
