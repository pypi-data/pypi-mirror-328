"""
Geo Distribution
================
This module is designed to manage and process land distribution scenarios, particularly focusing on adjustments 
in land use areas based on various scenario inputs. It integrates with land cover data management,
scenario-specific data fetching, and catchment area analysis to provide a comprehensive tool for land distribution analysis.

Features:
---------
- **Land Distribution Analysis**: Manages the calculation and distribution of land areas across different land use types 
  based on scenario-driven changes.
- **Grassland Distribution Management**: Specifically handles the redistribution of grassland areas, taking into account
  changes in mineral and organic components.

Dependencies:
-------------
- ``landcover_assignment.landcover_data_manager.DistributionManager``
- ``geo_landcover_assignment.catchment_landcover.CatchmentLandCover``
- ``resource_manager.scenario_data_fetcher.ScenarioDataFetcher``
- ``pandas`` for data manipulation and analysis.

Classes:
--------
.. class:: LandDistribution(scenario_data)
   :noindex:

   Handles the distribution of land areas for various land use types under different scenarios, adjusting for changes in
   areas and soil composition.

   .. method:: land_distribution(land_use, new_area)
      Calculates and updates the distribution of land based on land use type and the area change. It supports special 
      handling for grassland, wetland, and forest types, among others, adjusting shares of mineral, organic, and other 
      soil types accordingly.

   .. method:: grassland_distribution(mineral_area, organic_area, organic_mineral_area, grassland_area)
      Specifically handles the distribution and adjustment of grassland areas, considering changes in mineral and organic
      components, and recalculates the total remaining grassland area along with its composition.

"""

from landcover_assignment.resource_manager.landcover_data_manager import DistributionManager
from landcover_assignment.geo_landcover_assignment.catchment_landcover import CatchmentLandCover
from landcover_assignment.resource_manager.scenario_data_fetcher import ScenarioDataFetcher

class LandDistribution:
    """
    Handles the distribution of land areas for various land use types under different scenarios,
    adjusting for changes in areas and soil composition.

    This class provides methods to calculate and update land distribution based on changes in land use
    types, including special considerations for grassland, wetland, and forest. It utilizes data from
    land cover data managers, catchment analysis, and scenario-specific data fetchers to accurately
    model land distribution adjustments under various scenarios.

    Parameters
    ----------
    scenario_data : pd.DataFrame
        A DataFrame containing scenario-specific data inputs. This data is used to fetch catchment
        names and drive the scenario-based calculations for land distribution adjustments.

    Attributes
    ----------
    data_manager_class : DistributionManager
        An instance of DistributionManager for managing land distribution data.
    catchment_class : CatchmentLandCover
        An instance of CatchmentLandCover for accessing and analyzing catchment land cover data.
    sc_fetcher_class : ScenarioDataFetcher
        An instance of ScenarioDataFetcher initialized with scenario data for fetching scenario-specific information.
    catchment_name : str
        The name of the catchment area fetched based on the scenario data, used to identify the area of interest
        for land distribution calculations.

    Methods
    -------
    land_distribution(land_use, new_area)
        Calculates and updates the distribution of land based on land use type and the area change.
        It supports special handling for grassland, wetland, and forest types, among others, adjusting shares
        of mineral, organic, and other soil types accordingly.

    grassland_distribution(mineral_area, organic_area, organic_mineral_area, grassland_area)
        Specifically handles the distribution and adjustment of grassland areas, considering changes in mineral
        and organic components, and recalculates the total remaining grassland area along with its composition.
    """
    def __init__(self, scenario_data):
        self.data_manager_class = DistributionManager()
        self.catchment_class = CatchmentLandCover()
        self.sc_fetcher_class = ScenarioDataFetcher(scenario_data, validate_on_init=True)
        self.catchment_name = self.sc_fetcher_class.get_catchment_name()


    def land_distribution(self, land_use, new_area):
        """
        Calculates and updates the land distribution based on land use type and area change.

        :param land_use: The type of land use to calculate distribution for.
        :type land_use: str
        :param new_area: The area change to be applied to the land use type.
        :type new_area: float
        :return: A dictionary containing updated land distribution details.
        :rtype: dict
        """
        if land_use == "grassland":
            return None
        else:
            
            land = {key: 0 for key in self.data_manager_class.get_geoland_distribution_keys()}

            current_area = self.catchment_class.get_landuse_area(land_use, self.catchment_name) or 0

            shares = {
                key: self.catchment_class.get_land_shares(key, land_use, self.catchment_name) or 0
                for key in self.data_manager_class.get_geoland_share_keys()
            }
            # Calculate total area
            land["area_ha"] = current_area + (new_area or 0)


            # Calculate shares
            if land["area_ha"] != 0:
                for key, share_value in shares.items():
                    if key == "share_mineral" and land_use != "wetland":                    
                        land[key] = ((current_area * share_value) + (new_area or 0)) / land["area_ha"]
                    else:
                        # Calculate other shares proportionally
                        land[key] = (current_area * share_value) / land["area_ha"]
            else:
                # If area is zero, retain current shares
                for key, share_value in shares.items():
                    land[key] = share_value

            return land


    def grassland_distribution(self, mineral_area, organic_area, organic_mineral_area, grassland_area):
        """
        Manages the distribution of grassland areas, taking into account changes in mineral and organic areas.

        :param mineral_area: The area of grassland to be converted to mineral soil.
        :type mineral_area: float
        :param organic_area: The area of grassland to be converted to organic soil.
        :type organic_area: float
        :param organic_mineral_area: The area of grassland to be converted to organic-mineral soil.
        :type organic_mineral_area: float
        :param grassland_area: The total initial grassland area before distribution.
        :type grassland_area: float
        :return: A dictionary containing updated grassland distribution details.
        :rtype: dict
        """
        land = {key: 0 for key in self.data_manager_class.get_geoland_distribution_keys()}

        current_grassland_area = self.catchment_class.get_landuse_area("grassland", self.catchment_name, grassland_area)

        # Fetch all relevant shares dynamically
        shares = {
            key: self.catchment_class.get_grassland_shares(key, self.catchment_name, grassland_area) or 0
            for key in self.data_manager_class.get_geoland_share_keys()
        }

        # Calculate areas
        grass_mineral_area = current_grassland_area * shares["share_mineral"]
        grass_organic_area = current_grassland_area * shares["share_organic"]
        grass_organic_mineral_area = current_grassland_area * shares["share_organic_mineral"]


        grass_remaining_mineral = grass_mineral_area - mineral_area
        grass_remaining_organic = grass_organic_area - organic_area
        grass_remaining_organic_mineral_area = grass_organic_mineral_area - organic_mineral_area
        grass_rewetted_in_organic = organic_area
        grass_rewetted_in_organic_mineral = organic_mineral_area

        grass_total_remaining = grass_remaining_mineral + grass_remaining_organic + grass_remaining_organic_mineral_area + grass_rewetted_in_organic + grass_rewetted_in_organic_mineral

        if grass_total_remaining > 0:
            land["area_ha"] = grass_total_remaining
            land["share_organic"] = grass_remaining_organic / grass_total_remaining
            land["share_organic_mineral"] = grass_remaining_organic_mineral_area/ grass_total_remaining
            land["share_mineral"] = grass_remaining_mineral / grass_total_remaining
            land["share_rewetted_in_mineral"] = 0
            land["share_rewetted_in_organic"] = grass_rewetted_in_organic / grass_total_remaining
            land["share_rewetted_in_organic_mineral"] = grass_rewetted_in_organic_mineral / grass_total_remaining
            land["share_peat_extraction"] = 0
            land["share_burnt"] = shares["share_burnt"]
        else:

            # Set everything to zero to reflect no remaining grassland
            land = {key: 0 for key in land.keys()}

        return land
