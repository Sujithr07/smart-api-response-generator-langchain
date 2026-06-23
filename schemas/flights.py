from typing import Literal, Optional
from pydantic import BaseModel, Field
from datetime import date


class FlightBookingParameters(BaseModel):

    origin: str = Field(
        ...,
        description="Departure airport code (e.g., DEL, BOM, MAA, BLR).",
    )

    destination: str = Field(
        ...,
        description="Arrival airport code (e.g., DEL, BOM, MAA, BLR).",
    )

    departure_date: str = Field(
        ...,
        description="Departure date in YYYY-MM-DD format. Resolve relative phrases like 'next Tuesday' to an absolute date before send",
    )

    return_date: Optional[str] = Field(
        None,
        description="Return date in YYYY-MM-DD format. Leave null for one-way trips.",
    )

    passenger_count: int = Field(
        1,
        description="Number of passengers. Defaults to 1 if not specified.",
        ge=1,
        le=20,
    )

    cabin_class: Literal[
        "economy",
        "premium_economy",
        "business",
        "first"
    ] = Field(
        "economy",
        description="Travel class. Defaults to economy if not specified.",
    )

    trip_type: Literal["one_way", "round_trip"] = Field(
        "one_way",
        description="one_way if no return date is given, round_trip otherwise.",
    )