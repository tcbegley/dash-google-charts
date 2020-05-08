import React from 'react';
import PropTypes from 'prop-types';
import Chart from '../private/Chart';

const ColumnChart = props => {
  return <Chart {...props} chartType="ColumnChart" />;
};

ColumnChart.propTypes = {
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

  /**
   * The height of the chart.
   */
  height: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

  /**
   * The width of the chart.
   */
  width: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),

  /**
   * A dictionary of options for the chart
   */
  options: PropTypes.object,

  /**
   * The data for the chart
   */
  data: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.object),
    PropTypes.object
  ]),

  /**
   * Some charts support passing `diffdata` for visualising a change over time
   */
  diffdata: PropTypes.object,

  /**
   * Google maps api key for use with GeoChart
   */
  mapsApiKey: PropTypes.string,

  /**
   * URL to google sheet for pulling data
   */
  spreadSheetUrl: PropTypes.string,

  /**
   * Query parameters for external spreadsheet
   */
  spreadSheetQueryParameters: PropTypes.object,

  /**
   * Data formatting options.
   */
  formatters: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.object),
    PropTypes.object
  ]),

  /**
   * Allow legend to toggle inclusion of data in chart
   */
  legend_toggle: PropTypes.bool,

  /**
   * Data associated to user selection for use in callbacks
   */
  selection: PropTypes.object,

  /**
   * DataTable object, can be combined with selection data for use in callbacks
   */
  dataTable: PropTypes.object
};

export default ColumnChart;
