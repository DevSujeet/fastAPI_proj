from typing import Generic, List, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

from pydantic import BaseModel, Field

class PageParams(BaseModel):
    """Request query params for paginated API."""
    page: int = Field(default=1, ge=1, description="Page number (must be greater than or equal to 1)")
    size: int = Field(default=10, ge=1, le=100, description="Page size (must be between 1 and 100)")



T = TypeVar("T")

class PagedResponseSchema(GenericModel, Generic[T]):
    """Response schema for any paged API."""

    total: int
    page: int
    size: int
    results: List[T]


def paginate(page_params: PageParams, query, ResponseSchema: BaseModel) -> PagedResponseSchema[T]:
    """Paginate the query."""

    paginated_query = query.offset((page_params.page - 1) * page_params.size).limit(page_params.size).all()

    # Return the paginated response
    return PagedResponseSchema[T](
        total=query.count(),
        page=page_params.page,
        size=page_params.size,
        results=[ResponseSchema.model_validate(item) for item in paginated_query],
    )