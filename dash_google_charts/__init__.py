import os

from . import _components
from ._components import *  # noqa
from ._version import __version__  # noqa

_current_path = os.path.dirname(os.path.abspath(__file__))

METADATA_PATH = os.path.join(_current_path, "_components", "metadata.json")

_js_dist = [
    {
        "relative_package_path": ("_components/dash_google_charts.min.js"),
        "namespace": "dash_google_charts",
    }
]

_css_dist = []


for _component_name in _components.__all__:
    _component = getattr(_components, _component_name)
    _component._js_dist = _js_dist
    _component._css_dist = _css_dist
