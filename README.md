# dash-google-charts

[![CircleCI](https://circleci.com/gh/tcbegley/dash-google-charts/tree/master.svg?style=shield)](https://circleci.com/gh/tcbegley/dash-google-charts/tree/master)

Google Charts components for Plotly Dash built on top of [react-google-charts][rgc].

**Warning**: *dash-google-charts* is still pretty experimental, the interface and
features could change, and some components may not be fully functional yet. Use
with caution.

## Getting started

Install with `pip`:

```
pip install dash-google-charts
```

See [the examples][examples] for basic usage. Some examples make use of the
`gviz_api` helper library, available [here][gviz]. This is useful for
serialising your data in a JSON format ready for passing to Google Charts. The
`gviz_api` library can be installed with `pip`:

```
pip install gviz_api
```

[rgc]: https://react-google-charts.com/
[gviz]: https://github.com/google/google-visualization-python
[examples]: https://github.com/tcbegley/dash-google-charts/tree/master/examples
