import rioxarray as rxr
from dataconf import BUILDING_AREA, GADM, POPULATION, OPEN_BUILDINGS
import logging

def test_dataconf():
    logging.info(f"Building area: {BUILDING_AREA}")
    rxr.open_rasterio(BUILDING_AREA)