import pandas as pd

# For each geoId
    # Check against master list of geoId's, take the name of the entity
    # If it doesn't exist, create a Place with that geoId and name, and other Place data from BR
    # If geoId.len == 2
        # Fips state code
    # If geoId.len == 4
        # # (2+2=4)
        # First 2 is the state
        # Next 2 is the congressional district
    # If geoId.len == 5
        # # (2+3=5)
        # First 2 are the state
        # Next 3 are the county or the State Legislative District
    # If geoId.len == 7
        # (2+5=7)
        # First 2 is the state
        # Next 5 is the Place/City/School District
    # if geoId.len == 10
        # # (2+3+5=10)
        # First 2 are the state
        # Next 3 are the county
        # Next 5 is the county subdivision or place
    # If geoId.len == 11
        # # (2+3+6=11)
        # First 2 is the state
        # Next 3 is the county
        # Next 6 is the census tract
    # if geoId.len == 12
        # # (2+3+6+1=12)
        # First 2 is the state
        # Next 3 is the county
        # Next 6 is the Tract
        # Next 1 is the Block Group number

# func splitGeoId(int[] splitIndexes)
    # for each splitIndex
        # Subtract by one for zero-index
        # 