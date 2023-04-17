"""This file defines the schemas for the provider and requirer sides of the `fiveg_nrf` interface.
It exposes two interfaces.schema_base.DataBagSchema subclasses called:
- ProviderSchema
- RequirerSchema
Examples:
    ProviderSchema:
        unit: <empty>
        app: {"url": "http://nrf-example.com:1234"}
    RequirerSchema:
        unit: <empty>
        app:  <empty>
"""

from pydantic import BaseModel, AnyHttpUrl

from interface_tester.schema_base import DataBagSchema


class MyProviderAppData(BaseModel):
    url: AnyHttpUrl


class ProviderSchema(DataBagSchema):
    """Provider schema for fiveg_nrf."""
    app: MyProviderAppData


class RequirerSchema(DataBagSchema):
    """Requirer schema for fiveg_nrf."""
