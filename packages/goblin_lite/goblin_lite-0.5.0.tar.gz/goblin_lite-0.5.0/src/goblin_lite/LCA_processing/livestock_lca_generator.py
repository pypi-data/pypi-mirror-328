"""
Livestock LCA Generator
=======================
This module contains the LivestockLCAGenerator class, which is responsible for generating livestock footprints for climate change,
eutrophication, and air quality.
"""
from goblin_lite.resource_manager.database_manager import DataManager
from goblin_lite.impact_categories.climate_change import ClimateChangeLivestock
from goblin_lite.impact_categories.eutrophication import EutrophicationLivestock
from goblin_lite.impact_categories.air_quality import AirQualityLivestock

class LivestockLCAGenerator:
    """
    Manages the calculation of environmental footprints (climate change, eutrophication, air quality) associated with livestock production. 
    Employs ClimateChangeLivestock, EutrophicationLivestock, and AirQualityLivestock classes.

    Attributes
    ----------
    goblin_data_manager : DataManager
        An instance of the DataManager class for database interactions.
    data_manager_class : DataManager
        An instance of the DataManager class for database interactions.
    ef_country : str
        Country code for emission factors.
    calibration_year : int
        Base year for model calibration.
    target_year : int 
        Year of analysis.
    baseline_animal_data : pandas.DataFrame
        Baseline animal production data.
    scenario_animal_data : pandas.DataFrame
        Scenario-specific animal production data.
    farm_inputs_baseline : pandas.DataFrame
        Farm inputs (e.g., fertilizer) for the baseline.
    farm_inputs_scenario : pandas.DataFrame
        Farm inputs (e.g., fertilizer) for the scenario. 
    landuse_data : pandas.DataFrame
        Land use data.
    transition_matrix : pandas.DataFrame
        Data representing transitions between land use types.
    crop_data : pandas.DataFrame
        Crop-related data.
    DATABASE_PATH : str, optional
        Path to the external database, if None, default internal database used.
    AR_VALUE : str
        IPCC Assessment Report version (e.g., 'AR4', 'AR5') for impact calculations.

    Methods
    -------
    generate_livestock_footprint()
        Calculates disaggregated footprints for climate change, eutrophication, and air quality.
    generate_aggregated_livestock_footprint()
        Calculates aggregated climate change footprints at the national level.
    """
    def __init__(self, goblin_data_manager,
                baseline_animal_data,
                scenario_animal_data,
                farm_inputs_baseline,
                farm_inputs_scenario,
                landuse_data, 
                transition_matrix,
                crop_data):
        """
        Initializes the LivestockLCAGenerator with the provided data.

        Parameters
        ----------
        goblin_data_manager : DataManager
            An instance of the DataManager class for database interactions.
        baseline_animal_data : pandas.DataFrame
            Baseline animal production data.
        scenario_animal_data : pandas.DataFrame
            Scenario-specific animal production data.
        farm_inputs_baseline : pandas.DataFrame
            Farm inputs (e.g., fertilizer) for the baseline.
        farm_inputs_scenario : pandas.DataFrame
            Farm inputs (e.g., fertilizer) for the scenario. 
        landuse_data : pandas.DataFrame
            Land use data.
        transition_matrix : pandas.DataFrame
            Data representing transitions between land use types.
        crop_data : pandas.DataFrame
            Crop-related data.
        """
        self.goblin_data_manager_class = goblin_data_manager

        self.DATABASE_PATH = self.goblin_data_manager_class.get_database_path()
        
        self.data_manager_class = DataManager(self.DATABASE_PATH)
        
        self.baseline_animal_data = baseline_animal_data
        self.scenario_animal_data = scenario_animal_data
        self.farm_inputs_baseline = farm_inputs_baseline
        self.farm_inputs_scenario = farm_inputs_scenario
        self.landuse_data = landuse_data
        self.transition_matrix = transition_matrix
        self.crop_data = crop_data
    

    def generate_livestock_footprint(self):
        """
        Calculates disaggregated environmental footprints (climate change, eutrophication, air quality) for livestock production.

        Details 
        -------
        * Leverages ClimateChangeLivestock, EutrophicationLivestock, and AirQualityLivestock classes.
        * Utilizes baseline and scenario animal data, and farm input data.
        * Saves results to a database via the DataManager class.

        Returns
        -------
        None
        """  

        climate_change_livestock_class = ClimateChangeLivestock(self.goblin_data_manager_class,
                                                                self.transition_matrix, 
                                                                self.landuse_data, 
                                                                self.crop_data)
                                                            


        climate_change_livestock_disaggregated = (
            climate_change_livestock_class.climate_change_livestock_dissagregated(
                self.baseline_animal_data,
                self.scenario_animal_data,
                self.farm_inputs_baseline,
                self.farm_inputs_scenario,
            )
        )

        eutrophication_livestock_class = EutrophicationLivestock(self.goblin_data_manager_class)

        eutrophication_livestock_disaggregated = (
            eutrophication_livestock_class.eutrophication_livestock_dissagregated(
                self.baseline_animal_data,
                self.scenario_animal_data,
                self.farm_inputs_baseline,
                self.farm_inputs_scenario,
            )
        )

        air_quality_livestock_class = AirQualityLivestock(self.goblin_data_manager_class)

        air_quality_livestock_disaggregated = air_quality_livestock_class.air_quality_livestock_dissagregated(
            self.baseline_animal_data,
            self.scenario_animal_data,
            self.farm_inputs_baseline,
            self.farm_inputs_scenario,
        )

        self.data_manager_class.save_goblin_results_to_database(("climate_change_livestock_disaggregated", climate_change_livestock_disaggregated),
                                                                ("eutrophication_livestock_disaggregated", eutrophication_livestock_disaggregated),
                                                                ("air_quality_livestock_disaggregated", air_quality_livestock_disaggregated))
        

    def generate_aggregated_livestock_footprint(self):
        """
        Calculates aggregated climate change footprints associated with livestock production at the national level.

        Details 
        -------
        * Leverages the ClimateChangeLivestock class.
        * Utilizes baseline and scenario animal data, and farm input data.
        * Saves results to a database via the DataManager class.

        Returns
        -------
        None
        """  

        climate_change_livestock_class = ClimateChangeLivestock(self.goblin_data_manager_class,
                                                                self.transition_matrix, 
                                                                self.landuse_data, 
                                                                self.crop_data)

        climate_change_livestock_aggregated = (
            climate_change_livestock_class.climate_change_livestock_aggregated(
                self.baseline_animal_data,
                self.scenario_animal_data,
                self.farm_inputs_baseline,
                self.farm_inputs_scenario,
            )
        )
        climate_change_livestock_categories_as_co2e = (
            climate_change_livestock_class.climate_change_livestock_categories_as_co2e(
                self.baseline_animal_data,
                self.scenario_animal_data,
                self.farm_inputs_baseline,
                self.farm_inputs_scenario,
            )
        )

        self.data_manager_class.save_goblin_results_to_database(("climate_change_livestock_aggregated", climate_change_livestock_aggregated),
                                                                ("climate_change_livestock_categories_as_co2e", climate_change_livestock_categories_as_co2e))
