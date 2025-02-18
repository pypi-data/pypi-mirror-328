"""
Parser
======
The parser module contains functions for parsing the classifiers dictionary.
"""

def get_classifier_list(classifiers):
    """
    Get a list of classifiers.

    Args:
        classifiers (dict): A dictionary containing classifiers.

    Returns:
        list: A list of classifiers.
    """
    classifier_list = []

    for num, _ in enumerate(classifiers.keys()):
        classifier_list.append(f"Classifier{num+1}")

    classifier_list.append("LeadSpecies")

    return classifier_list


def get_age_classifier(classifiers):
    """
    Get the age classifier.

    Args:
        classifiers (dict): A dictionary containing classifiers.

    Returns:
        dict: A dictionary representing the age classifier.
    """
    max_age = classifiers["age_classes"]["max_age"]
    interval = classifiers["age_classes"]["age_interval"]

    age_id = []
    ages = []

    for year, value in enumerate(range(0, (max_age + 1), interval)):
        age_id.append("AGEID" + str(year))
        if year == 0:
            ages.append(0)
        else:
            ages.append(interval)

    age_dict = dict(zip(age_id, ages))

    return age_dict


def get_inventory_species(classifiers):
    """
    Get the inventory species.

    Args:
        classifiers (dict): A dictionary containing classifiers.

    Returns:
        list: A list of inventory species.
    """
    species = []

    for s in classifiers["Classifiers"]["species"]:
        species.append(s)

    return species


def get_species_yield_category(classifiers, species_name):
    """
    Get the species yield category.

    Args:
        classifiers (dict): A dictionary containing classifiers.
        species_name (str): The name of the species.

    Returns:
        dict: A dictionary representing the species yield category.
    """
    yield_category = []
    for i in classifiers["Classifiers"]["yield_class"][species_name]:
        for key, _ in i.items():
            yield_category.append(key)

    return yield_category


def get_yield_class_proportions(classifiers, species_name, yield_class):
    """
    Get the yield class proportions for a given species and yield class.

    Args:
        classifiers (dict): A dictionary containing classifiers.
        species_name (str): The name of the species.
        yield_class (str): The yield class.

    Returns:
        float: The yield class proportions.
    """
    for i in classifiers["Classifiers"]["yield_class"][species_name]:
        for key, value in i.items():
            if key == yield_class:
                return value


def get_disturbance_type(classifiers):
    """
    Get the disturbance types.

    Args:
        classifiers (dict): A dictionary containing classifiers.

    Returns:
        dict: A dictionary representing the disturbance types.
    """
    disturbance_type = {}
    for value, _ in enumerate(classifiers["Classifiers"]["distubance_type"]["id"]):
        disturbance_type[
            classifiers["Classifiers"]["distubance_type"]["id"][value]
        ] = classifiers["Classifiers"]["distubance_type"]["name"][value]

    return disturbance_type

def get_runner_clearfell_baseline(classifiers, species_type):
    """
    Get the clearfell baseline.

    Args:
        classifiers (dict): A dictionary containing classifiers.
        species_type (str): The species type.

    Returns:
        float: The clearfell baseline value for the specified species type.
    """
    try:
        clearfell_list = classifiers["Classifiers"]["baseline"]["harvest"]["clearfell"]
        for item in clearfell_list:
            if species_type in item:
                return item[species_type]
        print(f"Error: '{species_type}' is not found in the clearfell list.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def get_runner_clearfell_scenario(classifiers, species_type):
    """
    Get the clearfell scenario.

    Args:
        classifiers (dict): A dictionary containing classifiers.
        species_type (str): The species type.

    Returns:
        float: The clearfell scenario value for the specified species type.
    """
    try:
        clearfell_list = classifiers["Classifiers"]["scenario"]["harvest"]["clearfell"]
        for item in clearfell_list:
            if species_type in item:
                return item[species_type]
        print(f"Error: '{species_type}' is not found in the clearfell list.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_runner_thinning_baseline(classifiers, species_type):
    """
    Get the thinning baseline.

    Args:
        classifiers (dict): A dictionary containing classifiers.
        species_type (str): The species type.

    Returns:
        float: The thinning baseline value for the specified species type.
    """
    try:
        clearfell_list = classifiers["Classifiers"]["baseline"]["harvest"]["thinning"]
        for item in clearfell_list:
            if species_type in item:
                return item[species_type]
        print(f"Error: '{species_type}' is not found in the thinning list.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def get_runner_thinning_scenario(classifiers, species_type):
    """
    Get the thinning scenario.

    Args:
        classifiers (dict): A dictionary containing classifiers.
        species_type (str): The species type.

    Returns:
        float: The thinning scenario value for the specified species type.
    """
    try:
        clearfell_list = classifiers["Classifiers"]["scenario"]["harvest"]["thinning"]
        for item in clearfell_list:
            if species_type in item:
                return item[species_type]
        print(f"Error: '{species_type}' is not found in the thinning list.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def get_afforest_delay(Dynamic_Afforestation_config):
    """
    Get the afforestation delay.

    Args:
        Dynamic_Afforestation_config (dict): A dictionary containing configuration.
    
    Returns:
        int: The afforestation delay value.
    """
    return Dynamic_Afforestation_config["Dynamic_Afforestation"]["afforest_delay"]


def get_annual_afforestation_rate(Dynamic_Afforestation_config):
    """
    Get the annual afforestation rate for delay years.

    Args:
        Dynamic_Afforestation_config (dict): A dictionary containing configuration.
    
    Returns:
        float: The annual afforestation rate value for delay years.
    """
    return Dynamic_Afforestation_config["Dynamic_Afforestation"]["annual_afforestation_rate_pre_delay"]


def get_afforestation_species_distribution(Dynamic_Afforestation_config, species):
    """
    Get the afforestation rate species distribution.

    Args:
        Dynamic_Afforestation_config (dict): A dictionary containing configuration.
        species (str): The species to get the distribution for.
    
    Returns:
        float: The afforestation rate species distribution value.
    """
    try:
        _list = Dynamic_Afforestation_config["Dynamic_Afforestation"]["species_distribution"]
        for item in _list:
            if species in item:
                return item[species]
        print(f"Error: '{species}' is not found in the list.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_forest_management_intensity(config_data):
    """
    Get the forest management intensity.

    Args:
        config_data (dict): A dictionary containing configuration data.
    
    Returns:
        float: The forest management intensity value.
    """
    return config_data["Forest_management"]["intensity"]