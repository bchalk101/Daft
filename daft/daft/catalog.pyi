from typing import TYPE_CHECKING

from daft.daft import LogicalPlanBuilder as PyLogicalPlanBuilder

if TYPE_CHECKING:
    from daft.catalog.python_catalog import PythonCatalog

def read_table(name: str) -> PyLogicalPlanBuilder: ...
def register_table(name: str, plan_builder: PyLogicalPlanBuilder) -> str: ...
def register_python_catalog(catalog: PythonCatalog, catalog_name: str | None) -> str: ...
def unregister_catalog(catalog_name: str | None) -> bool: ...
