from pydantic import BaseModel, Field


class WaterQualityParameters(BaseModel):
    """Pydantic model for water quality parameters with optional fields."""

    temperature: float | None = Field(None, description="Water temperature in Celsius.")
    dissolved_oxygen: float | None = Field(
        None, description="Dissolved oxygen in mg/L."
    )
    conductivity: float | None = Field(None, description="Conductivity in µS/cm.")
    turbidity: float | None = Field(None, description="Turbidity in NTU.")
    ph: float | None = Field(None, description="pH level.")
    salinity: float | None = Field(None, description="Salinity in PSU or ppt.")
    ammonia: float | None = Field(None, description="Ammonia concentration in mg/L.")
    nitrate: float | None = Field(None, description="Nitrate concentration in mg/L.")
    nitrite: float | None = Field(None, description="Nitrite concentration in mg/L.")
    phosphate: float | None = Field(
        None, description="Phosphate concentration in mg/L."
    )
    tds: float | None = Field(None, description="Total Dissolved Solids in mg/L.")
    chlorine: float | None = Field(None, description="Chlorine concentration in mg/L.")
    hardness: float | None = Field(None, description="Water hardness in mg/L as CaCO3.")
    alkalinity: float | None = Field(None, description="Alkalinity in mg/L as CaCO3.")


class WaterQualityResult(BaseModel):
    """Pydantic model for standardized output of water quality analysis."""

    status: str
    explanation: str
    value: float | None = None


class WaterQualityResults(BaseModel):
    """Pydantic model for complete water quality analysis output."""

    temperature: WaterQualityResult | None = None
    dissolved_oxygen: WaterQualityResult | None = None
    conductivity: WaterQualityResult | None = None
    turbidity: WaterQualityResult | None = None
    ph: WaterQualityResult | None = None
    salinity: WaterQualityResult | None = None
    ammonia: WaterQualityResult | None = None
    nitrate: WaterQualityResult | None = None
    nitrite: WaterQualityResult | None = None
    phosphate: WaterQualityResult | None = None
    tds: WaterQualityResult | None = None
    chlorine: WaterQualityResult | None = None
    hardness: WaterQualityResult | None = None
    alkalinity: WaterQualityResult | None = None
