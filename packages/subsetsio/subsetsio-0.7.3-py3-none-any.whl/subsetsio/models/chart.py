from enum import Enum
from typing import Optional, Union
from .bar import BarChart, BarChartMetadata, BarChartData
from .counter import CounterChart, CounterChartMetadata, CounterChartData
from .line import LineChart, LineChartMetadata, LineChartData
from .map import MapChart, MapChartMetadata, MapChartData
from .scatter import ScatterplotChart, ScatterplotChartMetadata, ScatterplotChartData
from .table import TableChart, TableChartMetadata, TableChartData
from .common import ChartType

Chart = Union[LineChart, MapChart, BarChart, CounterChart, ScatterplotChart, TableChart]
ChartData = Union[LineChartData, MapChartData, BarChartData, CounterChartData, ScatterplotChartData, TableChartData]

def parse_chart(data: dict) -> Chart:
    chart_type = data['metadata']['type']
    if chart_type == ChartType.LINE:
        return LineChart(**data)
    elif chart_type == ChartType.MAP:
        return MapChart(**data)
    elif chart_type == ChartType.BAR:
        return BarChart(**data)
    elif chart_type == ChartType.COUNTER:
        return CounterChart(**data)
    elif chart_type == ChartType.SCATTERPLOT:
        return ScatterplotChart(**data)
    elif chart_type == ChartType.TABLE:
        return TableChart(**data)
    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")