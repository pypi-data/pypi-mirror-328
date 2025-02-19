import inspect
import json
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy

import click

from bam_masterdata.utils import delete_and_create_dir, import_module


def entities_to_json(
    module_path: str, export_dir: str, logger: "BoundLoggerLazyProxy"
) -> None:
    """
    Export entities to JSON files. The Python modules are imported using the function `import_module`,
    and their contents are inspected (using `inspect`) to find the classes in the datamodel containing
    `defs` and with a `model_to_json` method defined.

    Args:
        module_path (str): Path to the Python module file.
        export_dir (str): Path to the directory where the JSON files will be saved.
        logger (BoundLoggerLazyProxy): The logger to log messages.
    """
    module = import_module(module_path=module_path)
    # export to specific subfolders for each type of entity (each module)
    module_export_dir = os.path.join(
        export_dir, os.path.basename(module_path).replace(".py", "")
    )
    delete_and_create_dir(directory_path=module_export_dir, logger=logger)

    # Special case of `PropertyTypeDef` in `property_types.py`
    if "property_types.py" in module_path:
        for name, obj in inspect.getmembers(module):
            if name.startswith("_") or name == "PropertyTypeDef":
                continue
            try:
                json_data = json.dumps(obj.model_dump(), indent=2)
                output_file = os.path.join(module_export_dir, f"{obj.code}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(json_data)

                click.echo(f"Saved JSON for class {name} to {output_file}")
            except Exception as err:
                click.echo(f"Failed to process class {name} in {module_path}: {err}")
        return None

    # All other datamodel modules
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Ensure the class has the `model_to_json` method
        if not hasattr(obj, "defs") or not callable(getattr(obj, "model_to_json")):
            continue

        try:
            # Instantiate the class and call the method
            json_data = obj().model_to_json(indent=2)

            # Write JSON data to file
            output_file = os.path.join(module_export_dir, f"{obj.defs.code}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(json_data)

            click.echo(f"Saved JSON for class {name} to {output_file}")
        except Exception as err:
            click.echo(f"Failed to process class {name} in {module_path}: {err}")
