from typing import Literal,Optional,Dict,Any
from pydantic import BaseModel,Field
from datetime import date

class RequestMetadata(BaseModel):

    confidence_score: float=Field(
        ...,
        description= "Confidence that the user's intent was interpreted correctly (0.0 to 1.0).",
        ge=0.0, le=0.1,
    )

    raw_intent: str= Field(
        ...,
        description=  "Original user request.",
    )

    warnings: list[str]= Field(
        default_factory= list,
        description= "Assumptions or missing details in the request.",
    )


class APIrequest(BaseModel):

    api_endpoint: str= Field(
        ...,
        description= "The API route to call, e.g. /v1/flights/book or /v1/reservations/cancel. Must start with a slash.",
    )

    http_method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]= Field(
        ...,
        description="HTTP method to use for this request.",
    )

    parameters: Dict[str, Any] = Field(
        default_factory=dict,
        description="Request-specific parameters. The exact keys depend on the api_endpoint. Nested values may be strings, numbers, dates (as ISO 8601 strings), booleans, or null.",
    )
    
    metadata: RequestMetadata = Field(
        ...,
        description="Metadata about how the model interpreted the request.",
    )
