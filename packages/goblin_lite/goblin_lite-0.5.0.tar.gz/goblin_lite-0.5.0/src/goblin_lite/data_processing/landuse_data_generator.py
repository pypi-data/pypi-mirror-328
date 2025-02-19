"""
Landuse Data Generator
======================
This module contains the LandUseDataGenerator class, which is responsible for generating landuse data and landcover outputs.
The class leverages the TransitionMatrix, LandCover and Afforestation classes to calculate landuse data and landcover outputs based on scenario-specific and baseline landuse data.

Classes
-------
LandUseDataGenerator
    Manages the generation of land use and land cover data. Leverages TransitionMatrix, 
    LandCover, and Afforestation classes for core calculations.

    Methods
    -------
    generate_transition_matrix()
        Creates a land use transition matrix using the TransitionMatrix class.

    generate_landuse_data()
       Calculates the base and future land use areas using the LandCover class.

    generate_spared_area_category_totals()
        Generates the total spared area by category using the LandCover class.

    generate_afforestation_data()
        Generates afforestation data for the CBM, using the Afforestation class. 
"""
from landcover_assignment.transition_matrix import TransitionMatrix
from landcover_assignment.landcover import LandCover
from landcover_assignment.afforestation import Afforestation


class LandUseDataGenerator:
    """
    Manages the generation of land use and land cover data. Leverages TransitionMatrix, 
    LandCover, and Afforestation classes for core calculations.

    Attributes
    ----------
    goblin_data_manager_class : object
        Instance of the GoblinDataManager class.
    calibration_year : int
        Base year for model calibration.
    target_year : int
        Year of analysis.
    scenario_dataframe : pandas.DataFrame
        Dataframe containing scenario-specific land use parameters.
    grassland_area : pandas.DataFrame 
        Grassland area data.
    spared_area : pandas.DataFrame
        Spared grassland area data (converted to other land uses).
    spared_area_breakdown : pandas.DataFrame
        Breakdown of spared grassland area (e.g., by soil type). 

    Methods
    -------
    generate_transition_matrix()
        Creates a land use transition matrix using the TransitionMatrix class.

    generate_landuse_data()
       Calculates the base and future land use areas using the LandCover class.

    generate_spared_area_category_totals()
        Generates the total spared area by category using the LandCover class.

    generate_afforestation_data()
        Generates afforestation data for the CBM, using the Afforestation class. 
    """
    def __init__(self, 
                 goblin_data_manager, 
                 scenario_dataframe, 
                 grassland_area, 
                 spared_area, 
                 spared_area_breakdown):
        
        self.goblin_data_manager_class = goblin_data_manager
        self.calibration_year = self.goblin_data_manager_class.get_calibration_year()
        self.target_year = self.goblin_data_manager_class.get_target_year()
        self.scenario_dataframe = scenario_dataframe
        self.grassland_area = grassland_area
        self.spared_area = spared_area
        self.spared_area_breakdown = spared_area_breakdown
    

    def generate_transition_matrix(self):

        transition = TransitionMatrix(
            self.calibration_year, self.target_year, self.scenario_dataframe, self.grassland_area, self.spared_area, self.spared_area_breakdown
        )


        transition_matrix = transition.create_transition_matrix()

        return transition_matrix
    
    
    def generate_landuse_data(self):

        land = LandCover(
            self.calibration_year, self.target_year, self.scenario_dataframe, self.grassland_area, self.spared_area, self.spared_area_breakdown
        )

        landuse_data = land.combined_future_land_use_area()

        spared_area_log = land.get_spared_area_log()

        return {"landuse_data": landuse_data, "spared_area_log": spared_area_log}


    def generate_spared_area_category_totals(self):

        land = LandCover(
            self.calibration_year, self.target_year, self.scenario_dataframe, self.grassland_area, self.spared_area, self.spared_area_breakdown
        )

        spared_area_category_totals = land.get_spared_area_log()

        return spared_area_category_totals
    

    def generate_afforestation_data(self):
        
        transition_matrix = self.generate_transition_matrix()
        
        afforestation_class = Afforestation(
            self.calibration_year, self.target_year, self.scenario_dataframe, transition_matrix
        )

        afforestation_data = afforestation_class.gen_cbm_afforestation_dataframe(
            self.spared_area_breakdown
        )

        return afforestation_data