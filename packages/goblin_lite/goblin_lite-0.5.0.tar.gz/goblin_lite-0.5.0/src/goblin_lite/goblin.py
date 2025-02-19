"""
Goblin module
==============

The Goblin Lite module is designed for running environmental impact scenarios, focusing on agricultural practices and land use.
It is intended to be used in the context of environmental impact assessments, and it generates a series of data tables representing
various aspects of environmental impact under different agricultural and land use scenarios. 

These tables are stored and can be accessed for further analysis and visualization.
"""
from static_scenario_generator.scenarios import ScenarioGeneration
from goblin_lite.data_processing.animal_data_generation import AnimalDataGenerator
from goblin_lite.data_processing.grassland_data_generation import GrasslandDataGenerator
from goblin_lite.data_processing.crop_data_generator import CropDataGenerator
from goblin_lite.data_processing.landuse_data_generator import LandUseDataGenerator
from goblin_lite.data_processing.forest_carbon_generator import ForestCarbonGenerator
from goblin_lite.LCA_processing.crop_lca_generator import CropLCAGenerator
from goblin_lite.LCA_processing.landuse_lca_generator import LandUseLCAGenerator
from goblin_lite.LCA_processing.livestock_lca_generator import LivestockLCAGenerator
from goblin_lite.LCA_processing.lca_total_generator import LCATotalGenerator
from goblin_lite.resource_manager.database_manager import DataManager
from goblin_lite.resource_manager.scenario_data_fetcher import ScenarioDataFetcher
from goblin_lite.resource_manager.directory import Directories
import copy as copy



class ScenarioRunner:
    """
    The ScenarioRunner class is responsible for orchestrating the entire scenario generation process in the context
    of environmental impact assessments, focusing on agricultural practices and land use scenarios.

    Args:
    -----
    ef_country : str
        The country for which the scenario is being run.
    calibration_year : int
        The year for calibration data.
    target_year : int
        The target year for which the scenario is generated.
    config_path : str
        The path to the scenario configuration file.
    cbm_config_path : str
        The path to the CBM CFS3 configuration file.
    DATABASE_PATH : str, optional
        The path to the database. Default is None.
    AR_VALUE : str, optional
        The Assessment Report value. Default is "AR5".
        
    Attributes
    ----------
    ef_country : str
        The country for which the scenario is being run.
    calibration_year : int
        The year for calibration data.
    target_year : int
        The target year for which the scenario is generated.
    config_path : str
        The path to the scenario configuration file.
    cbm_config_path : str
        The path to the CBM CFS3 configuration file.
    DATABASE_PATH : str, optional
        The path to the database. Default is None.
    AR_VALUE : str, optional
        The Assessment Report value. Default is "AR5".
    data_manager_class : DataManager
        An instance of the DataManager class for managing data storage.

    Methods
    -------
    run_scenarios()
        Orchestrates the scenario generation process, encompassing data preparation, analysis, and storage.
        It generates a series of data tables representing various aspects of environmental impact under different
        agricultural and land use scenarios. These tables are stored and can be accessed for further analysis
        and visualization.

    Note:
    -----
        An external database is required for the CBM validation process. If CBM validation is enabled, the DATABASE_PATH must be provided.
    """

    def __init__(
        self,
        goblin_data_manager,
    ):
        self.goblin_data_manager_class = goblin_data_manager
        self.config_path = self.goblin_data_manager_class.get_configuration_path()
        self.DATABASE_PATH = self.goblin_data_manager_class.get_database_path()
        self.data_manager_class = DataManager(self.DATABASE_PATH)
            

    def run_scenarios(self):
        """
        Executes the scenario generation process using provided inputs and configurations.

        This method manages the complete scenario generation process. It prepares and generates data for various scenarios
        and the selected baseline across multiple domains (such as animal data, land use, crop data, carbon flux, etc.),
        encapsulated in 31 distinct data tables. These tables are saved as pandas dataframes and are intended for subsequent
        analysis and visualization.
        """

        self.data_manager_class.create_or_clear_database()
        
        #scenario data 
        scenario_data_generator = ScenarioGeneration()
        scenario_input_dataframe = scenario_data_generator.generate_scenario_dataframe(self.config_path)

        if self.DATABASE_PATH is not None:
            
            sc_ferch_class = ScenarioDataFetcher(scenario_input_dataframe)

            #create directories
            dir_class = Directories(self.DATABASE_PATH)
            dir_class.create_goblin_directory_structure()

        

        # animal data
        animal_data_generator = AnimalDataGenerator(self.goblin_data_manager_class, scenario_input_dataframe
        )

        baseline_animal_data, scenario_animal_data = animal_data_generator.generate_animal_data()

        #Animal Exports 
        protein_and_milk_summary = animal_data_generator.generate_livestock_outputs()

        # Grassland data
        grassland_data_generator = GrasslandDataGenerator(self.goblin_data_manager_class,
                                                          scenario_input_dataframe,
                                                          scenario_animal_data,
                                                          baseline_animal_data)

        # farm inputs data grassland 
        grassland_farm_inputs_baseline, grassland_farm_inputs_scenario = grassland_data_generator.generate_farm_inputs()


        # Grassland data
        (total_spared_area, 
        total_grassland_area, 
        total_spared_area_by_soil_group, 
        per_hectare_stocking_rate,
        per_hectare_grass_yield)= grassland_data_generator.generate_grassland_areas()

        # Crop data
        crop_data_generator = CropDataGenerator(self.goblin_data_manager_class, scenario_input_dataframe)

        crop_input_data = crop_data_generator.generate_crop_data()

        #Crop farm data
        crop_farm_data = crop_data_generator.generate_crop_farm_data()

        # Land use data
        landuse_data_generator = LandUseDataGenerator(self.goblin_data_manager_class,
                                                      scenario_input_dataframe, 
                                                      total_grassland_area, 
                                                      total_spared_area, 
                                                      total_spared_area_by_soil_group)

        transition_matrix = landuse_data_generator.generate_transition_matrix()

        landuse_data = landuse_data_generator.generate_landuse_data()

        spared_area_category_totals = landuse_data_generator.generate_spared_area_category_totals()

        cbm_afforestation_data_derived_input = landuse_data_generator.generate_afforestation_data()

        # Forest carbon data
        forest_data_generator = ForestCarbonGenerator(self.goblin_data_manager_class, 
                                                      scenario_input_dataframe, 
                                                      cbm_afforestation_data_derived_input)

        forest_data = forest_data_generator.generate_forest_carbon()

        forest_carbon_flux = forest_data["forest_flux"]
        forest_carbon_aggregate = forest_data["forest_aggregate"]
        cbm_spared_area_afforestation_time_series_output = forest_data["afforestation_area"]


        #SAVE DATA
        self.data_manager_class.save_goblin_results_to_database(("scenario_input_dataframe",scenario_input_dataframe),
                                                                ("baseline_animal_data",baseline_animal_data),
                                                                ("scenario_animal_data",scenario_animal_data),
                                                                ("grassland_farm_inputs_scenario",grassland_farm_inputs_scenario),
                                                                ("grassland_farm_inputs_baseline",grassland_farm_inputs_baseline),
                                                                ("total_spared_area",total_spared_area),
                                                                ("total_grassland_area",total_grassland_area),
                                                                ("total_spared_area_by_soil_group",total_spared_area_by_soil_group),
                                                                ("per_hectare_stocking_rate",per_hectare_stocking_rate),
                                                                ("per_hectare_grass_yield",per_hectare_grass_yield),
                                                                ("crop_input_data",crop_input_data),
                                                                ("crop_farm_data",crop_farm_data),
                                                                ("transition_matrix",transition_matrix),
                                                                ("landuse_data",landuse_data["landuse_data"]),
                                                                ("spared_area_log",landuse_data["spared_area_log"]),
                                                                ("spared_area_category_totals",spared_area_category_totals),
                                                                ("cbm_afforestation_data_derived_input",cbm_afforestation_data_derived_input),
                                                                ("forest_carbon_flux",forest_carbon_flux),
                                                                ("forest_carbon_aggregate",forest_carbon_aggregate),
                                                                ("cbm_spared_area_afforestation_time_series_output",cbm_spared_area_afforestation_time_series_output),
                                                                ("protein_and_milk_summary",protein_and_milk_summary))

        # Crop LCA
        crop_data_generator = CropLCAGenerator(self.goblin_data_manager_class, 
                                               crop_input_data, 
                                               scenario_input_dataframe)

        crop_data_generator.generate_crop_footprint()

        crop_data_generator.generate_aggregated_crop_footprint()

        # Land use LCA
        landuse_data_generator = LandUseLCAGenerator(self.goblin_data_manager_class,
                                                    landuse_data["landuse_data"], 
                                                    transition_matrix, 
                                                    forest_data["forest_flux"])

        landuse_data_generator.generate_landuse_footprint()

        # Livestock LCA
        livestock_data_generator = LivestockLCAGenerator(self.goblin_data_manager_class,
                                                        baseline_animal_data,
                                                        scenario_animal_data,
                                                        grassland_farm_inputs_baseline,
                                                        grassland_farm_inputs_scenario,
                                                        landuse_data["landuse_data"], 
                                                        transition_matrix,
                                                        crop_input_data)
        
        livestock_data_generator.generate_livestock_footprint()
        livestock_data_generator.generate_aggregated_livestock_footprint()

        # Climate change totals
        climate_change_totals = LCATotalGenerator(
            self.goblin_data_manager_class, scenario_input_dataframe
        )
        climate_change_totals.generate_climate_change_totals()

        climate_change_totals.generate_eutrophication_totals()

        climate_change_totals.generate_air_quality_totals()

        print("Scenario Generation Complete ... \n")
    