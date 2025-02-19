from .models import WaterQualityParameters, WaterQualityResult, WaterQualityResults


def check_water_quality(params: WaterQualityParameters) -> WaterQualityResults:
    """Checks water quality parameters and returns a WaterQualityResults object."""
    results = WaterQualityResults()

    if params.temperature is not None:
        results.temperature = WaterQualityResult(
            status="OK" if 0 <= params.temperature <= 35 else "Alert",
            explanation="Temperature is within range."
            if 0 <= params.temperature <= 35
            else "Temperature is outside the normal range.",
            value=params.temperature,
        )

    if params.dissolved_oxygen is not None:
        results.dissolved_oxygen = WaterQualityResult(
            status="OK" if 5 <= params.dissolved_oxygen <= 14 else "Alert",
            explanation="Dissolved oxygen is within range."
            if 5 <= params.dissolved_oxygen <= 14
            else "Dissolved oxygen is outside the normal range.",
            value=params.dissolved_oxygen,
        )

    if params.conductivity is not None:
        results.conductivity = WaterQualityResult(
            status="OK" if 50 <= params.conductivity <= 1500 else "Alert",
            explanation="Conductivity is within range."
            if 50 <= params.conductivity <= 1500
            else "Conductivity is outside the normal range.",
            value=params.conductivity,
        )

    if params.turbidity is not None:
        results.turbidity = WaterQualityResult(
            status="OK" if 0 <= params.turbidity <= 5 else "Alert",
            explanation="Turbidity is within range."
            if 0 <= params.turbidity <= 5
            else "Turbidity is outside the normal range.",
            value=params.turbidity,
        )

    if params.ph is not None:
        results.ph = WaterQualityResult(
            status="OK" if 6.5 <= params.ph <= 8.5 else "Alert",
            explanation="pH is within range."
            if 6.5 <= params.ph <= 8.5
            else "pH is outside the normal range.",
            value=params.ph,
        )

    if params.salinity is not None:
        results.salinity = WaterQualityResult(
            status="OK" if 0 <= params.salinity <= 35 else "Alert",
            explanation="Salinity is within range."
            if 0 <= params.salinity <= 35
            else "Salinity is outside the normal range.",
            value=params.salinity,
        )

    if params.ammonia is not None:
        results.ammonia = WaterQualityResult(
            status="OK" if 0 <= params.ammonia <= 0.05 else "Alert",
            explanation="Ammonia is within range."
            if 0 <= params.ammonia <= 0.05
            else "Ammonia is outside the normal range.",
            value=params.ammonia,
        )

    if params.nitrate is not None:
        results.nitrate = WaterQualityResult(
            status="OK" if 0 <= params.nitrate <= 10 else "Alert",
            explanation="Nitrate is within range."
            if 0 <= params.nitrate <= 10
            else "Nitrate is outside the normal range.",
            value=params.nitrate,
        )

    if params.nitrite is not None:
        results.nitrite = WaterQualityResult(
            status="OK" if 0 <= params.nitrite <= 1 else "Alert",
            explanation="Nitrite is within range."
            if 0 <= params.nitrite <= 1
            else "Nitrite is outside the normal range.",
            value=params.nitrite,
        )

    if params.phosphate is not None:
        results.phosphate = WaterQualityResult(
            status="OK" if 0 <= params.phosphate <= 0.1 else "Alert",
            explanation="Phosphate is within range."
            if 0 <= params.phosphate <= 0.1
            else "Phosphate is outside the normal range.",
            value=params.phosphate,
        )

    if params.tds is not None:
        results.tds = WaterQualityResult(
            status="OK" if 0 <= params.tds <= 1000 else "Alert",
            explanation="TDS is within range."
            if 0 <= params.tds <= 1000
            else "TDS is outside the normal range.",
            value=params.tds,
        )

    if params.chlorine is not None:
        results.chlorine = WaterQualityResult(
            status="OK" if 0 <= params.chlorine <= 4 else "Alert",
            explanation="Chlorine is within range."
            if 0 <= params.chlorine <= 4
            else "Chlorine is outside the normal range.",
            value=params.chlorine,
        )

    if params.hardness is not None:
        results.hardness = WaterQualityResult(
            status="OK" if 0 <= params.hardness <= 180 else "Alert",
            explanation="Hardness is within range."
            if 0 <= params.hardness <= 180
            else "Hardness is outside the normal range.",
            value=params.hardness,
        )

    if params.alkalinity is not None:
        results.alkalinity = WaterQualityResult(
            status="OK" if 20 <= params.alkalinity <= 200 else "Alert",
            explanation="Alkalinity is within range."
            if 20 <= params.alkalinity <= 200
            else "Alkalinity is outside the normal range.",
            value=params.alkalinity,
        )

    return results
