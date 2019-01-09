import React from 'react';
import PropTypes from 'prop-types';
import {Chart as GChart} from 'react-google-charts';

const Chart = props => {
  return <GChart {...props} />;
};

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
  mapsApiKey: PropTypes.string
};

// height?: string | number;
//   width?: string | number;
//   graphID?: string;
//   chartType: GoogleChartWrapperChartType;
//   diffdata?: {
//     old: any;
//     new: any;
//   };
//   options?: ChartWrapperOptions["options"];
//   loader?: JSX.Element;
//   errorElement?: JSX.Element;
//   data?: any[] | {};
//   rows?: GoogleDataTableRow[];
//   columns?: GoogleDataTableColumn[];
//   chartActions?: GoogleChartAction[];
//   chartEvents?: ReactGoogleChartEvent[];
//   chartVersion?: GoogleChartVersion;
//   chartPackages?: GoogleChartPackages[];
//   chartLanguage?: string;
//   mapsApiKey?: string;
//   graph_id?: string;
//   legendToggle?: boolean;
//   legend_toggle?: boolean;
//   getChartWrapper?: (
//     chartWrapper: GoogleChartWrapper,
//     google: GoogleViz
//   ) => void;
//   getChartEditor?: (
//     args: {
//       chartEditor: GoogleChartEditor;
//       chartWrapper: GoogleChartWrapper;
//       google: GoogleViz;
//     }
//   ) => void;
//   className?: string;
//   style?: React.CSSProperties;
//   formatters?: {
//     column: number;
//     type:
//       | "ArrowFormat"
//       | "BarFormat"
//       | "ColorFormat"
//       | "DateFormat"
//       | "NumberFormat"
//       | "PatternFormat";
//     options?: {};
//   }[];
//   spreadSheetUrl?: string;
//   spreadSheetQueryParameters?: {
//     headers: number;
//     gid?: number | string;
//     sheet?: string;
//     query?: string;
//     access_token?: string;
//   };
//   rootProps?: any;
//   controls?: GoogleChartControlProp[];
//   render?: ReactGoogleChartDashboardRender;
//   //https://developers.google.com/chart/interactive/docs/gallery/toolbar#example_1
//   toolbarItems?: GoogleChartToolbarItem[];
//   toolbarID?: string;

export default Chart;
