from typing import TypeVar, Union, Type, get_args
from pydantic import BaseModel, create_model, ConfigDict, model_validator
from .chart import (
    BarChart, LineChart, MapChart, CounterChart, ScatterplotChart, TableChart
)

def make_optional(model: Type[BaseModel]) -> Type[BaseModel]:
    """Makes all fields except 'type' optional and excluded from the model"""
    fields = {}
    for name, field in model.model_fields.items():
        if name != 'type':  # Skip the type field entirely
            field_info = field.annotation
            fields[name] = (Union[field_info, None], None)
    
    class UpdateModelBase(BaseModel):
        model_config = ConfigDict(extra='forbid')
        
        @model_validator(mode='after')
        def validate_update(self):
            update_fields = {
                k: v for k, v in self.__dict__.items() 
                if v is not None
            }
            if not update_fields:
                raise ValueError("At least one field must be provided for update")
            return self

    model_cls = create_model(
        f'{model.__name__}Update',
        __base__=UpdateModelBase,
        **fields
    )

    return model_cls

# Create update models for each chart type's  using make_optional
BarChartUpdate = make_optional(BarChart)
LineChartUpdate = make_optional(LineChart)
MapChartUpdate = make_optional(MapChart)
CounterChartUpdate = make_optional(CounterChart)
ScatterplotChartUpdate = make_optional(ScatterplotChart)
TableChartUpdate = make_optional(TableChart)

# Map chart types to their update models
UPDATE_MODEL_MAP = {
    'bar': BarChartUpdate,
    'line': LineChartUpdate,
    'map': MapChartUpdate,
    'counter': CounterChartUpdate,
    'scatter': ScatterplotChartUpdate,
    'table': TableChartUpdate
}

ChartUpdate = Union[
    BarChartUpdate,
    LineChartUpdate,
    MapChartUpdate,
    CounterChartUpdate,
    ScatterplotChartUpdate,
    TableChartUpdate
]