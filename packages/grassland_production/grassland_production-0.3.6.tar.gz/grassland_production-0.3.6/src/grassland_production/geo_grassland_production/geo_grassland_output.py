"""
===============================
Grassland Output Manager Module
===============================
This module contains the GrasslandOutput class, which is responsible for managing and
processing various outputs related to grassland production and management. The class
integrates different aspects of grassland management, such as grasslands, farm data,
soil groups, dry matter production, stocking rates, and grass yield, to provide easy retrieval of grassland
scenario results.

Classes:
    GrasslandOutput: Manages and computes outputs for grassland management for catchment analysis.

"""
from grassland_production.geo_grassland_production.geo_spared_area import GeoGrasslands
from grassland_production.geo_grassland_production.geo_farm_data_generation import FarmData
from grassland_production.geo_grassland_production.geo_grassland_soils import GeoSoilGroups
from grassland_production.geo_grassland_production.geo_dry_matter import GeoDryMatter
from grassland_production.geo_grassland_production.geo_stocking_rate import GeoStockingRate
from grassland_production.geo_grassland_production.geo_grass_yield import GeoYield


import pandas as pd

class GrasslandOutput:
    """
    A class to manage and format outputs related to grassland production and management.

    This class integrates several aspects of grassland management, including grasslands,
    farm data, soil groups, dry matter production, stocking rates, and grass yield. It is used to
    format and retrieve various metrics important for grassland management decision-making.

    Args:
        ef_country (str): The country for which the analysis is performed.
        calibration_year (int): The calibration year.
        target_year (int): The target year for future scenario projections.
        scenario_inputs_df (DataFrame): DataFrame containing scenario input variables data.
        scenario_animals_df (DataFrame): DataFrame containing scenario animal data.
        baseline_animals_df (DataFrame): DataFrame containing baseline animal data.

    Attributes:
        grassland_class (Grasslands): An instance of the (geo) Grasslands class.
        farm_data_class (FarmData): An instance of the FarmData class.
        soil_groups_class (GeoSoilGroups): An instance of the GeoSoilGroups class.
        dm_class ( GeoDryMatter): An instance of the DryMatter class.
        stock_class (StockingRate): An instance of the StockingRate class.
        yield_class (GeoYield): An instance of the GeoYield class.

    Methods:
        total_spared_area(): Returns the total area spared (former grassland).
        total_grassland_area(): Returns the total area of grassland (remaining).
        total_spared_area_breakdown(): Provides a breakdown of spared areas by soil group.
        farm_inputs_data(): Computes and returns farm data for different scenarios.
        baseline_farm_inputs_data(): Computes and returns baseline farm data.
        total_concentrate_feed(): formats and returns total concentrate feed data.
        grassland_stocking_rate(): formats and returns the grassland stocking rate.
        grass_yield_per_hectare(): formats and returns the grass yield per hectare.
    """
    def __init__(
        self,
        ef_country,
        calibration_year,
        target_year,
        scenario_data,
        scenario_animals_df,
        baseline_animals_df,
    ):
        self.grassland_class = GeoGrasslands(
            ef_country,
            calibration_year,
            target_year,
            scenario_data,
            scenario_animals_df,
            baseline_animals_df,
        )
        self.farm_data_class = FarmData(
            ef_country,
            calibration_year,
            target_year,
            scenario_data,
            scenario_animals_df,
            baseline_animals_df,
        )

        self.soil_groups_class = GeoSoilGroups(
            ef_country,
            calibration_year,
            target_year,
            scenario_data,
            scenario_animals_df,
            baseline_animals_df,
        )

        self.dm_class = GeoDryMatter(
            ef_country,
            calibration_year,
            target_year,
            scenario_data,
            scenario_animals_df,
            baseline_animals_df,
        )

        self.stock_class = GeoStockingRate(
            ef_country,
            calibration_year,
            target_year,
            scenario_data,
            scenario_animals_df,
            baseline_animals_df,
        )

        self.yield_class = GeoYield(
            ef_country,
            calibration_year,
            target_year,
            scenario_data,
            scenario_animals_df,
            baseline_animals_df,
        )


    def total_spared_area(self):
        """
        Calculate and return the total spared area (grassland no longer stocked).

        This method invokes a function from the Grasslands class to determine the total
        area that is available but not being used for grazing purposes.

        Returns:
            DataFrame: Total area spared from grassland use.
        """

        return self.grassland_class.get_non_grass_total_area()

    def total_grassland_area(self):
        """
        Calculate and return the total area covered by grassland.

        This method retrieves the total area of grassland (in use) from the Grasslands class.

        Returns:
            DataFrame: Total area of grassland.
        """
        return self.grassland_class.get_grass_total_area()
    
    def total_spared_area_breakdown(self):
        """
        Provide a breakdown of the spared areas by soil group.

        This method uses the SoilGroups class to categorize spared areas (destocked) 
        into different soil groups. Provides information on the potential productivity of 
        spared areas.

        Returns:
            DataFrame: A breakdown of spared areas by soil groups.
        """
        return self.soil_groups_class.get_cohort_soil_groups()


    def farm_inputs_data(self):
        """
        Compute and return farm data for various scenarios.

        This method computes detailed farm data based on different scenarios using the
        FarmData class. 

        Returns:
            DataFrame: Farm data computed for different scenarios.
        """
        return self.farm_data_class.compute_farm_data_in_scenarios()


    def baseline_farm_inputs_data(self):
        """
        Compute and return baseline farm data.

        This method calculates farm data for the baseline scenario using the FarmData
        class. 

        Returns:
            DataFrame: Baseline farm data.
        """
        return self.farm_data_class.compute_farm_data_in_baseline()
    

    def total_concentrate_feed(self):
        """
        Calculate and return the total concentrate feed data.

        This method aggregates total concentrate feed data across various parameters,
        utilizing the DryMatter class.

        Returns:
            DataFrame: total concentrate feed data.
        """
        return pd.concat(self.dm_class.get_total_concentrate_feed(), axis=0)
    

    def grassland_stocking_rate(self):    
        """
        Calculate and return the grassland stocking rate per hectare, per system (dairy, beef, sheep).

        Returns:
            DataFrame: Computed grassland stocking rates.
        """
        return pd.concat(self.stock_class.get_stocking_rate(), axis=0)


    def grass_yield_per_hectare(self):
        """
        Calculate and return the grass yield per hectare.

        This method processes the yield data to format it into a more usable structure,
        including scenario, year, system, and grassland type variables.

        Returns:
            DataFrame: Computed grass yield per hectare.
        """
        yield_data = self.yield_class.get_yield()
        formatted_data = []

        for scenario, data in yield_data.items():
            for system, dataframe in data.items():
                for grassland_type in dataframe.columns:
                    for year in dataframe.index:
                        formatted_data.append(
                            {
                                "scenario": scenario,
                                "year": year,
                                "system": system,
                                "grassland_type": grassland_type,
                                "yield": dataframe.loc[year, grassland_type],
                            }
                        )

        return pd.DataFrame(formatted_data)
