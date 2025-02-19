# Water Quality Analysis Utils

This Python package provides tools for analyzing water quality parameters such as temperature, dissolved oxygen, conductivity, turbidity, and pH using Pydantic for validation.

## Features
- Pydantic models for input validation
- Functions to check if parameters are within safe ranges
- Detailed messages explaining out-of-range values
- Test suite included with pytest

## Installation
```bash
poetry install
```

## Usage
```python
from wqautils import WaterQualityParameters, check_water_quality
params = WaterQualityParameters(temperature=20, dissolved_oxygen=8, conductivity=500, turbidity=2, ph=7)
results = check_water_quality(params)
print(results)
```

## Tests
Run tests with:
```bash
pytest
```
