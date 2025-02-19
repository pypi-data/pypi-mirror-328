"""
Goblin Data Manager
===================
This module contains the GoblinDataManager class, which is responsible for managing data for the GOBLIN LCA framework.
"""
class GoblinDataManager:
    """
    Manages data for the GOBLIN LCA framework.

    This class is responsible for managing data for the GOBLIN LCA framework. It provides access to AR values, climate change livestock emissions groups,
    climate change livestock emissions categories, climate change livestock conversion groups, climate change crops emissions groups, 
    climate change crop conversion groups, default urea, and default urea abated.

    Attributes
    ----------
    AR4_values : dict
        The AR4 values for CH4, N2O, and CO2e.

    AR5_values : dict
        The AR5 values for CH4, N2O, and CO2e.

    AR_values : dict
        The AR values for CH4, N2O, and CO2e.

    climate_change_livestock_emissions_groups : dict
        The climate change livestock emissions groups.

    climate_change_livestock_emissions_categories : dict
        The climate change livestock emissions categories.

    climate_change_livestock_conversion_groups : dict
        The climate change livestock conversion groups.

    climate_change_crops_emissions_groups : dict
        The climate change crops emissions groups.

    climate_change_crop_conversion_groups : dict
        The climate change crop conversion groups.

    default_urea : float
        The default urea value.

    default_urea_abated : float
        The default urea abated value.

    Methods
    -------
    get_AR_values()
        Retrieves the AR values for CH4, N2O, and CO2e.

    get_climate_change_livestock_emissions_groups()
        Retrieves the climate change livestock emissions groups.

    get_climate_change_livestock_emissions_categories()
        Retrieves the climate change livestock emissions categories.

    get_climate_change_livestock_conversion_groups()
        Retrieves the climate change livestock conversion groups.

    get_climate_change_crops_emissions_groups()
        Retrieves the climate change crops emissions groups.

    get_climate_change_crop_conversion_groups()
        Retrieves the climate change crop conversion groups.

    get_default_urea()
        Retrieves the default urea value.

    get_default_urea_abated()
        Retrieves the default urea abated value.

    get_calibration_year()
        Retrieves the calibration year.

    get_target_year()
        Retrieves the target year.

    get_configuration_path()
        Retrieves the configuration path.

    get_cbm_configuration_path()
        Retrieves the CBM configuration path.

    get_database_path()
        Retrieves the database path.

    get_ef_country()
        Retrieves the EF country.
    """
    def __init__(self, 
                 ef_country, 
                 calibration_year, 
                 target_year, 
                 configuration_path, 
                 cbm_configuration_path, 
                 DATABASE_PATH=None, 
                 AR_VALUE="AR5"):

        self.AR_VALUE = AR_VALUE
        self.ef_country = ef_country
        self.calibration_year = calibration_year
        self.target_year = target_year
        self.config_path = configuration_path
        self.cbm_config_path = cbm_configuration_path # generate scenario_data
        self.database_path = DATABASE_PATH
    
        self.AR4_values = {"CH4": 25, "N2O": 298, "CO2e": 3.67}

        self.AR5_values = {"CH4": 28, "N2O": 265, "CO2e": 3.67}

        if self.AR_VALUE.upper() == "AR4":
            self.AR_values = self.AR4_values
        elif self.AR_VALUE.upper() == "AR5":
            self.AR_values = self.AR5_values
        else:
            raise ValueError(
                "Invalid AR_VALUE. AR_VALUE must be either 'AR4' or 'AR5'."
            )

        self.climate_change_livestock_emissions_groups = {
            "CH4": ["enteric_ch4", "manure_management_CH4"],
            "N2O": ["soils_N2O", "manure_management_N2O"],
            "CO2": ["soils_CO2"],
        }

        self.climate_change_livestock_emissions_categories = {
            "manure_management": ["manure_management_N2O", "manure_management_CH4"],
            "enteric": ["enteric_ch4"],
            "soils": ["soils_CO2", "soils_N2O"],
        }

        self.climate_change_livestock_conversion_groups = {
            "CH4": ["enteric_ch4", "manure_management_CH4"],
            "N2O": ["soils_N2O", "manure_management_N2O"],
            "CO2": ["soils_CO2"],
        }

        self.climate_change_crops_emissions_groups = {
            "N2O": ["soils_N2O"],
            "CO2": ["soils_CO2"],
        }

        self.climate_change_crop_conversion_groups = {
            "N2O": ["soils_N2O"],
            "CO2": ["soils_CO2"],
        }

        self.default_urea = 0.2
        self.default_urea_abated = 0

    def get_AR_values(self):
        """
        Retrieves the AR values for CH4, N2O, and CO2e.

        Returns:
            dict: The AR values.
        """
        return self.AR_values
    
    def get_climate_change_livestock_emissions_groups(self):
        """
        Retrieves the climate change livestock emissions groups.

        Returns:
            dict: The climate change livestock emissions groups.
        """
        return self.climate_change_livestock_emissions_groups
    
    def get_climate_change_livestock_emissions_categories(self):
        """
        Retrieves the climate change livestock emissions categories.

        Returns:
            dict: The climate change livestock emissions categories.
        """
        return self.climate_change_livestock_emissions_categories
    
    def get_climate_change_livestock_conversion_groups(self):
        """
        Retrieves the climate change livestock conversion groups.

        Returns:
            dict: The climate change livestock conversion groups.
        """
        return self.climate_change_livestock_conversion_groups
    
    def get_climate_change_crops_emissions_groups(self):
        """
        Retrieves the climate change crops emissions groups.

        Returns:
            dict: The climate change crops emissions groups.
        """
        return self.climate_change_crops_emissions_groups
    
    def get_climate_change_crop_conversion_groups(self):
        """
        Retrieves the climate change crop conversion groups.

        Returns:
            dict: The climate change crop conversion groups.
        """
        return self.climate_change_crop_conversion_groups
    
    def get_default_urea(self):
        """
        Retrieves the default urea value.

        Returns:
            float: The default urea value.
        """
        return self.default_urea
    
    def get_default_urea_abated(self):
        """
        Retrieves the default urea abated value.

        Returns:
            float: The default urea abated value.
        """
        return self.default_urea_abated

    def get_calibration_year(self):
        """
        Retrieves the calibration year.

        Returns:
            int: The calibration year.
        """
        return self.calibration_year
    
    def get_target_year(self):
        """
        Retrieves the target year.

        Returns:
            int: The target year.
        """
        return self.target_year
    
    def get_configuration_path(self):
        """
        Retrieves the configuration path.

        Returns:
            str: The configuration path.
        """
        return self.config_path
    
    def get_cbm_configuration_path(self):
        """
        Retrieves the CBM configuration path.

        Returns:
            str: The CBM configuration path.
        """
        return self.cbm_config_path
    
    def get_database_path(self):
        """
        Retrieves the database path.

        Returns:
            str: The database path.
        """
        return self.database_path
    
    def get_ef_country(self):
        """
        Retrieves the EF country.

        Returns:
            str: The EF country.
        """
        return self.ef_country