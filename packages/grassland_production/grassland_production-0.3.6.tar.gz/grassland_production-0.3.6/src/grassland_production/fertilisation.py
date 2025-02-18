"""
======================
Fertilisation Module
======================

This module encompasses the Fertilisation class, which is focused on computing various fertilization 
rates and their distribution across different farm systems and scenarios. This class is used in the calculation of 
grassland production.

Classes:
    Fertilisation: Manages the computation of fertilization-related data for different farm systems and scenarios.
"""

from itertools import product
import pandas as pd
from grassland_production.resource_manager.data_loader import Loader
from grassland_production.resource_manager.grassland_data_manager import DataManager
from grassland_production.resource_manager.scenario_data_fetcher import ScenarioDataFetcher
from grassland_production.grassland_area import Areas
from cattle_lca.lca import DailySpread


class Fertilisation:
    """
    The Fertilisation class is responsible for calculating both inorganic and organic fertilization rates 
    and their application across various farm systems and scenarios. This class plays a role in the calculation of
    grassland production.

    Args:
        ef_country (str): The country for which the analysis is performed.
        calibration_year (int): The calibration year.
        target_year (int): The target year for future scenario projections.
        scenario_inputs_df (DataFrame): DataFrame containing scenario input variables data.
        scenario_animals_df (DataFrame): DataFrame containing scenario animal data.
        baseline_animals_df (DataFrame): DataFrame containing baseline animal data.

    Attributes:
        sc_class (ScenarioDataFetcher): Instance of ScenarioDataFetcher for fetching scenario data.
        scenario_list (list): List of scenarios for the analysis.
        data_manager_class (DataManager): Instance of DataManager for managing data related to fertilization.
        loader_class (Loader): Instance of Loader to load various datasets.
        areas_class (Areas): Instance of Areas for calculating area-related data.
        cattle_spread_class (DailySpread): Instance for handling daily spread rates of fertilizers.
        calibration_year (int): The base year for data calibration.
        target_year (int): The target year for future scenario projections.

    Methods:
        compute_inorganic_fertilization_rate():
            Calculates the inorganic fertilization rate for various farm systems and scenarios.

        compute_organic_fertilization_rate():
            Computes the rate of organic fertilizer application for different farm systems.

        organic_fertilisation_per_ha():
            Calculates the organic fertilization rate per hectare for different farm systems and scenarios.
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
        self.sc_class = ScenarioDataFetcher(scenario_data)
        self.scenario_list = self.sc_class.get_scenario_list()
        self.data_manager_class = DataManager(
            calibration_year,
            target_year,
            scenario_animals_df,
            baseline_animals_df,
        )

        self.calibration_year = self.data_manager_class.get_calibration_year()
        self.default_calibration_year = self.data_manager_class.get_default_calibration_year()
        self.default_grassland_year = self.data_manager_class.get_default_grassland_year()
        self.target_year = self.data_manager_class.get_target_year()

        self.loader_class = Loader()
        self.areas_class = Areas(
            self.target_year, calibration_year, self.default_calibration_year
        )

        self.cattle_spread_class = DailySpread(ef_country)

    def _cached_fertilization(self, fertilization_data_frame, fertilization_cache, grassland_type, system, year):
        """
        Fetch fertilization data from the DataFrame with caching.

        Args:
            fertilization_data_frame (DataFrame): Fertilization data by system.
            fertilization_cache (dict): Cache dictionary to store/retrieve computed results.
            grassland_type (str): The grassland type.
            system (str): The system (e.g., Dairy, Beef).
            year (int): The year.

        Returns:
            float: Cached or computed fertilization value.
        """
        key = (grassland_type, system, year)
        if key not in fertilization_cache:
            fertilization_cache[key] = fertilization_data_frame.loc[(grassland_type, system), str(year)]
        return fertilization_cache[key]


    def compute_inorganic_fertilization_rate(self):
        """
        Calculates the inorganic fertilization rate for various farm systems (dairy, beef, sheep) across 
        different scenarios. This method determines the average fertilization rate per grassland type 
        (Pasture, Silage, Hay) within each farm system, considering both historical data and future scenario 
        projections.

        The computation uses fertilization data by system and farm numbers to estimate the average fertilization 
        rate. For the target year, scenario-specific values are used for dairy and beef systems, while sheep 
        systems use an average value based on historical data.

        Returns:
            dict: A dictionary with keys for each farm system ('dairy', 'beef', 'sheep'), containing DataFrames 
                with fertilization rates for each grassland type. Each DataFrame is indexed by grassland type 
                and contains columns for the calibration year and the target year.

        Notes:
            - The method uses scenario-specific fertilization values for 'Pasture' and 'Grass silage' types in dairy 
            and beef systems. For sheep and other grassland types, average historical values are used.
        """

        fertilization_by_system_data_frame = (
            self.loader_class.grassland_fertilization_by_system()
        )

        # Initialize cache for fertilization data
        fertilization_cache = {}

        fert_rate = {"dairy": {}, "beef": {}, "sheep": {}}

        scenarios = self.scenario_list
        scenario_column = self.sc_class.get_scenarios_col()
        cattle_system_column = self.sc_class.get_cattle_system_col()
        manure_system_column = self.sc_class.get_manure_system_col()

        # for each scenario
        for sc in scenarios:
            # Cache masks for this scenario
            mask_cache = {
                "beef": (scenario_column == sc) & (cattle_system_column == "Beef") & (manure_system_column == "tank liquid"),
                "dairy": (scenario_column == sc) & (cattle_system_column == "Dairy") & (manure_system_column == "tank liquid"),
            }

            # Initialize DataFrames for this scenario
            dairy_data = {}
            beef_data = {}
            sheep_data = {}

            # for each grassland type
            for grassland_type in fertilization_by_system_data_frame.index.levels[0]:

                # Use the calibration year for calibration, or the default year if not available
                year_for_calibration = (
                    self.calibration_year 
                    if self.calibration_year > self.default_calibration_year 
                    else self.default_calibration_year
                )

                # Use cached data for past and target years
                dairy_data[grassland_type] = {
                    str(self.calibration_year): self._cached_fertilization(
                        fertilization_by_system_data_frame,
                        fertilization_cache,
                        grassland_type,
                        "Dairy",
                        year_for_calibration,
                    ),

                    str(self.target_year): (
                        self.sc_class.get_dairy_fertilisation_value(mask_cache["dairy"])
                        if grassland_type in ["Pasture", "Grass silage"]
                        else fertilization_by_system_data_frame.loc[(grassland_type, "Dairy"), :].mean()
                    ),
                }

                beef_data[grassland_type] = {
                    str(self.calibration_year): self._cached_fertilization(
                        fertilization_by_system_data_frame,
                        fertilization_cache,
                        grassland_type,
                        "Cattle",
                        year_for_calibration,
                    ),
                    str(self.target_year): (
                        self.sc_class.get_beef_fertilisation_value(mask_cache["beef"])
                        if grassland_type in ["Pasture", "Grass silage"]
                        else fertilization_by_system_data_frame.loc[(grassland_type, "Cattle"), :].mean()
                    ),
                }

                sheep_data[grassland_type] = {
                    str(self.calibration_year): self._cached_fertilization(
                        fertilization_by_system_data_frame,
                        fertilization_cache,
                        grassland_type,
                        "Sheep",
                        year_for_calibration,
                    ),
                    str(self.target_year): (
                        fertilization_by_system_data_frame.loc[(grassland_type, "Sheep"), :].mean()
                    ),
                }

            # Convert dictionaries to DataFrames and store in fert_rate
            fert_rate["dairy"][sc] = pd.DataFrame.from_dict(dairy_data, orient="index")
            fert_rate["beef"][sc] = pd.DataFrame.from_dict(beef_data, orient="index")
            fert_rate["sheep"][sc] = pd.DataFrame.from_dict(sheep_data, orient="index")

        return fert_rate
    

    def compute_organic_fertilization_rate(self):
        """
        Computes the rate of organic fertilizer application (primarily cattle slurry) for different farm systems. 
        This calculation is based on the net excretion rate of nutrients from cattle, as determined by the DailySpread 
        class. The method considers the nutrient content in the cattle slurry and its spread rate across various farm 
        systems. Notably, sheep systems are excluded from this calculation, assuming that slurry consists only of cattle 
        slurry.

        The method calculates organic fertilization rates for both the calibration year and the target year under 
        different scenarios, considering the changes in livestock populations and management practices.

        Returns:
            dict: A dictionary with keys for different scenarios. Each entry contains a DataFrame with columns 
                representing different farm systems ('dairy', 'beef', 'sheep') and rows representing years 
                (calibration year, target year). Each cell in the DataFrame represents the total organic 
                nitrogen spread for that farm system and year.

        Notes:
            - Sheep systems are excluded from this calculation.
        """

        cols = self.data_manager_class.get_farming_systems()

        year_list = list(
            (
                self.calibration_year,
                self.target_year,
            )
        )

        animal_list = list(self.data_manager_class.get_cohorts()["Cattle"]) + list(
            self.data_manager_class.get_cohorts()["Sheep"]
        )

        scenario_list = self.scenario_list

        spread_dict = {}

        N_spread_past = pd.DataFrame(0.0, columns=cols, index=year_list)

        baseline_animals_df = self.data_manager_class.get_baseline_animals_dataframe()
        scenario_animals_df = self.data_manager_class.get_scenario_animals_dataframe()

        for animal_name in animal_list:
            animal_past = getattr(
                self.data_manager_class.get_baseline_animals_dict()[self.calibration_year][
                    "animals"
                ],
                animal_name,
            )
            mask_validation = (baseline_animals_df["year"] == self.calibration_year) & (
                baseline_animals_df["cohort"] == animal_name
            )

            if animal_name in self.data_manager_class.get_dairy_beef_cohorts()["Dairy"]:
                N_spread_past.loc[int(self.calibration_year), "dairy"] += (
                    self.cattle_spread_class.net_excretion_SPREAD(animal_past)
                    * baseline_animals_df.loc[mask_validation, "pop"].item()
                )

            elif animal_name in self.data_manager_class.get_dairy_beef_cohorts()["Beef"]:
                N_spread_past.loc[int(self.calibration_year), "beef"] += (
                    self.cattle_spread_class.net_excretion_SPREAD(animal_past)
                    * baseline_animals_df.loc[mask_validation, "pop"].item()
                )

            elif animal_name in self.data_manager_class.get_cohorts()["Sheep"]:
                N_spread_past.loc[int(self.calibration_year), "sheep"] = 0

        # Scenario future inputs
        for scenario in scenario_list:
            N_spread = N_spread_past.copy(deep=True)

            farm_mask = (
                self.data_manager_class.get_scenario_aggregation()["Scenarios"] == scenario
            )

            for farm_name in self.data_manager_class.get_scenario_aggregation().loc[
                farm_mask, "farm_id"
            ].unique():
                for animal_name in animal_list:
                    if (
                        animal_name
                        in self.data_manager_class.get_scenario_animals_dict()[farm_name][
                            "animals"
                        ].__dict__.keys()
                    ):
                        animal = getattr(
                            self.data_manager_class.get_scenario_animals_dict()[farm_name][
                                "animals"
                            ],
                            animal_name,
                        )
                        mask = (scenario_animals_df["farm_id"] == farm_name) & (
                            scenario_animals_df["cohort"] == animal_name
                        )

                        if (
                            animal_name
                            in self.data_manager_class.get_dairy_beef_cohorts()["Dairy"]
                        ):
                            N_spread.loc[int(self.target_year), "dairy"] += (
                                self.cattle_spread_class.net_excretion_SPREAD(animal)
                                * scenario_animals_df.loc[mask, "pop"].item()
                            )
                        elif (
                            animal_name
                            in self.data_manager_class.get_dairy_beef_cohorts()["Beef"]
                        ):
                            N_spread.loc[int(self.target_year), "beef"] += (
                                self.cattle_spread_class.net_excretion_SPREAD(
                                    animal,
                                )
                                * scenario_animals_df.loc[mask, "pop"].item()
                            )

                        elif (
                            animal_name in self.data_manager_class.get_cohorts()["Sheep"]
                        ):
                            N_spread.loc[int(self.target_year), "sheep"] = 0

            spread_dict[scenario] = N_spread

        return spread_dict


    def organic_fertilisation_per_ha(self):
        """
        Calculates the rate of organic fertilization per hectare for dairy and beef farm systems. This method 
        adjusts the total organic nitrogen spread calculated in 'compute_organic_fertilization_rate' to a per 
        hectare basis, considering the area of different types of grasslands (Pasture, Grass silage) and the 
        proportion of these grasslands within each farm system.

        The calculation is performed for both the calibration year and the target year across various scenarios. 
        It provides a detailed view of how organic fertilization is distributed across different types of 
        grasslands within dairy and beef systems.

        Returns:
            dict: A dictionary with keys for different scenarios. Each entry contains a DataFrame with columns 
                for 'dairy' and 'beef' systems and rows for the calibration year and the target year. Each cell 
                in the DataFrame represents the organic nitrogen spread per hectare for that system and year.

        Notes:
            - Sheep systems are excluded from this calculation.
            - If data for the calibration year is not present, a default year is used.
        """
        spread_dict = self.compute_organic_fertilization_rate()
        grassland_areas = self.loader_class.cso_grassland_areas()
        nfs_system_proportions = self.areas_class.get_nfs_system_proportions()

        dairy_nfs_system_proportions = nfs_system_proportions[0]
        beef_nfs_system_proportions = nfs_system_proportions[1]

        systems_dict = {
            "dairy": dairy_nfs_system_proportions,
            "beef": beef_nfs_system_proportions,
        }

        default_year_flag = True
        for _dict in spread_dict:
            for sys, year in product(
                spread_dict[_dict].columns, spread_dict[_dict].index[:-1]
            ):
                if sys != "sheep":
                    try:
                        organic_input = spread_dict[_dict].loc[int(year), sys]

                        spread_dict[_dict].loc[int(year), sys] = organic_input / (
                            (
                                grassland_areas.loc[int(year), "Pasture"]
                                * systems_dict[sys].loc[int(year), "Pasture"]
                            )
                            + (
                                grassland_areas.loc[int(year), "Grass silage"]
                                * systems_dict[sys].loc[int(year), "Grass silage"]
                            )
                        )
                    except KeyError:
                        if default_year_flag == True:
                            print(
                                f"... calibration year not present, {self.default_calibration_year} default year used for Spread Manure Dictionary..."
                            )
                            default_year_flag = False

                        organic_input = spread_dict[_dict].loc[int(year), sys]
                        spread_dict[_dict].loc[int(year), sys] = organic_input / (
                            (
                                grassland_areas.loc[
                                    self.default_calibration_year, "Pasture"
                                ]
                                * systems_dict[sys].loc[
                                    self.default_calibration_year, "Pasture"
                                ]
                            )
                            + (
                                grassland_areas.loc[
                                    self.default_calibration_year, "Grass silage"
                                ]
                                * systems_dict[sys].loc[
                                    self.default_calibration_year, "Grass silage"
                                ]
                            )
                        )

                spread_dict[_dict].loc[int(self.target_year), sys] = spread_dict[
                    _dict
                ].loc[int(self.calibration_year), sys]

        return spread_dict
