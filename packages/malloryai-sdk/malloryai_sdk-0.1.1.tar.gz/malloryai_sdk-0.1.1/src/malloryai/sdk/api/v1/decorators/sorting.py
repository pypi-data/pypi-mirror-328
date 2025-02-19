from typing import Callable, Any, Optional
from functools import wraps
from inspect import signature

from pydantic import BaseModel, Field, ValidationError, create_model


class SortParams(BaseModel):
    """Pydantic model for sorting validation."""

    sort: str = Field(..., pattern="^(name|created_at|updated_at)$")
    order: str = Field(..., pattern="^(asc|desc)$")

    model_config = {"extra": "ignore"}


def validate_sorting(
    func: Optional[Callable] = None, *, sort_pattern: Optional[str] = None
) -> Callable:
    """
    Decorator to validate and inject sorting parameters.

    Usage without override:
      @validate_sorting
      async def list_exploits(..., sort: str = "created_at", order: str = "desc"):
          ...

    Or with override:
      @validate_sorting(sort_pattern="^(url|authors|maturity|created_at|updated_at)$")
      async def list_exploits(..., sort: str = "created_at", order: str = "desc"):
          ...
    """

    def decorator(f: Callable) -> Callable:
        @wraps(f)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Retrieve function signature and merge default values with provided kwargs.
            sig = signature(f)
            defaults = {
                name: param.default
                for name, param in sig.parameters.items()
                if param.default is not param.empty
            }
            params = defaults.copy()
            params.update(kwargs)

            # Decide which model to use.
            if sort_pattern is None:
                model_cls = SortParams
            else:
                # Use a configuration dictionary as expected in Pydantic v2.
                config_dict = {"extra": "ignore"}
                model_cls = create_model(
                    "SortParamsCustom",
                    sort=(str, Field(..., pattern=sort_pattern)),
                    order=(str, Field(..., pattern="^(asc|desc)$")),
                    __config__=config_dict,
                )
            try:
                sort_params = model_cls(sort=params["sort"], order=params["order"])
                # Update kwargs with the validated values.
                kwargs.update(sort_params.model_dump(exclude_unset=True))
            except (ValidationError, KeyError) as e:
                raise ValueError(f"Invalid or missing sorting parameters: {e}")

            return await f(*args, **kwargs)

        return wrapper

    # Allow the decorator to be used with or without arguments.
    if func is not None and callable(func):
        return decorator(func)
    return decorator
