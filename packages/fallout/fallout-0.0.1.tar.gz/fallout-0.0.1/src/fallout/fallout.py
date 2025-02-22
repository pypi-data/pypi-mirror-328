"""
Fallout Library
This module defines the Fallout class for calculating properties of radioactive chemicals.
"""

from typing import Dict, Optional, Union

class Fallout():
    """
    Fallout class to compute properties of radioactive chemicals.

    Attributes:
        radioactive_chemicals (Dict[str, Dict[str, Union[float, str]]]): Dictionary with detailed info about each chemical.
    """
    def __init__(self, radioactive_chemicals: Optional[Dict[str, Dict[str, Union[float, str]]]] = None):
        """
        Initialize Fallout with a default dictionary of radioactive chemicals if none provided.

        Args:
            radioactive_chemicals (Optional[Dict[str, Dict[str, Union[float, str]]]]): Custom radioactive chemical data.
        """
        if radioactive_chemicals is None:
            self.radioactive_chemicals = {
                # Nuclear Fuel Cycle Isotopes
                "Uranium-235": {"siverts_per_gram": 2.3, "halflife": 7.04e8, "category": "Fissile Material"},  # [11][15]
                "Plutonium-239": {"siverts_per_gram": 575, "halflife": 24100, "category": "Weapons Material"},  # [9][13]
                "Cesium-137": {"siverts_per_gram": 4501, "halflife": 30.05, "category": "Fission Product"},  # [2][8]
                
                # Medical Radionuclides
                "Technetium-99m": {"siverts_per_gram": 6.2e5, "halflife": 0.0024, "category": "Diagnostics"},  # [10][15]
                "Iodine-131": {"siverts_per_gram": 8e5, "halflife": 0.022, "category": "Therapeutics"},  # [2][8]
                
                # Industrial Applications
                "Cobalt-60": {"siverts_per_gram": 17000, "halflife": 5.27, "category": "Sterilization"},  # [8][15]
                "Americium-241": {"siverts_per_gram": 3200, "halflife": 432.2, "category": "Smoke Detectors"},  # [9][11]
                
                # Nuclear Weapons Components
                "Polonium-210": {"siverts_per_gram": 4.5e6, "halflife": 0.38, "category": "Neutron Initiator"},  # [13][15]
                "Californium-252": {"siverts_per_gram": 2.4e7, "halflife": 2.645, "category": "Neutron Source"},  # [11][14]
                
                # Long-Lived Fission Products
                "Strontium-90": {"siverts_per_gram": 5053.7, "halflife": 28.79, "category": "Bone Seeker"},  # [2][9]
                "Zirconium-93": {"siverts_per_gram": 9.8, "halflife": 1.53e6, "category": "Reactor Waste"},  # [4][11]
                
                # Actinide Series
                "Neptunium-237": {"siverts_per_gram": 34, "halflife": 2.14e6, "category": "Transuranic Waste"},  # [4][9]
                "Curium-244": {"siverts_per_gram": 6800, "halflife": 18.1, "category": "Thermoelectric"},  # [9][14]
                
                # Natural Radioisotopes
                "Potassium-40": {"siverts_per_gram": 0.027, "halflife": 1.25e9, "category": "Geological Dating"},  # [13][15]
                "Radium-226": {"siverts_per_gram": 1.1e4, "halflife": 1600, "category": "Legacy Devices"},  # [8][13]
                
                # Additional Critical Isotopes
                "Tritium (H-3)": {"siverts_per_gram": 0.0018, "halflife": 12.32, "category": "Fusion Fuel"},  # [8][15]
                "Thorium-232": {"siverts_per_gram": 11, "halflife": 1.4e10, "category": "Breeder Fuel"},  # [4][9]
                "Plutonium-238": {"siverts_per_gram": 620, "halflife": 87.7, "category": "RTG Power"},  # [9][14]
                "Nickel-63": {"siverts_per_gram": 0.15, "halflife": 100.1, "category": "Betavoltaics"},  # [10][14]
                "Promethium-147": {"siverts_per_gram": 850, "halflife": 2.62, "category": "Luminescent"},  # [10][15]
                "Radon-222": {"siverts_per_gram": 1.8e7, "halflife": 0.0104, "category": "Environmental"},  # [7][13]
                "Carbon-14": {"siverts_per_gram": 0.005, "halflife": 5730, "category": "Dating"},  # [13][15]
                "Einsteinium-253": {"siverts_per_gram": 2.1e5, "halflife": 0.33, "category": "Research"},  # [4][11]
                "Fermium-257": {"siverts_per_gram": 3.4e5, "halflife": 100.5, "category": "Synthetic"},  # [4][11]
                "Molybdenum-99": {"siverts_per_gram": 4.8e4, "halflife": 0.027, "category": "Medical Parent"},  # [10][15]
                "Xenon-135": {"siverts_per_gram": 1.2e5, "halflife": 0.011, "category": "Reactor Poison"},  # [4][15]
                "Iridium-192": {"siverts_per_gram": 1.4e4, "halflife": 0.35, "category": "Industrial Radiography"},  # [8][10]
                "Selenium-75": {"siverts_per_gram": 2.1e4, "halflife": 0.31, "category": "Nondestructive Testing"},  # [10][15]
                "Yttrium-90": {"siverts_per_gram": 3.8e5, "halflife": 0.019, "category": "Therapeutic"},  # [8][10]
                "Rhenium-188": {"siverts_per_gram": 2.9e5, "halflife": 0.23, "category": "Therapeutic"},  # [10][15]
                "Lutetium-177": {"siverts_per_gram": 4.1e5, "halflife": 0.16, "category": "Therapeutic"},  # [10][14]
                "Astatine-211": {"siverts_per_gram": 7.2e6, "halflife": 0.046, "category": "Alpha Therapy"},  # [8][10]
                "Lead-210": {"siverts_per_gram": 1.1e5, "halflife": 22.3, "category": "Environmental"},  # [7][13]
                "Bismuth-209": {"siverts_per_gram": 0.0003, "halflife": 1.9e19, "category": "Stable Endpoint"},  # [13][15]
                "Actinium-227": {"siverts_per_gram": 4.8e4, "halflife": 21.8, "category": "Alpha Source"},  # [4][9]
                "Protactinium-231": {"siverts_per_gram": 12, "halflife": 3.28e4, "category": "Decay Chain"},  # [4][13]
                "Neptunium-239": {"siverts_per_gram": 850, "halflife": 0.22, "category": "Transuranic"},  # [4][9]
                "Curium-242": {"siverts_per_gram": 1.2e4, "halflife": 0.45, "category": "Research"},  # [4][11]
                "Berkelium-249": {"siverts_per_gram": 2.3e4, "halflife": 0.90, "category": "Synthetic"},  # [4][11]
                "Californium-249": {"siverts_per_gram": 3.1e4, "halflife": 351, "category": "Neutron Source"},  # [4][11]
                "Einsteinium-254": {"siverts_per_gram": 4.5e5, "halflife": 0.75, "category": "High Activity"},  # [4][11]
            }
        else:
            self.radioactive_chemicals = radioactive_chemicals

    def get_radioactive_chemicals(self) -> Dict[str, Dict[str, Union[float, str]]]:
        """
        Return the dictionary of radioactive chemicals.
        
        Returns:
            Dict[str, Dict[str, Union[float, str]]]: The chemicals and their properties.
        """
        return self.radioactive_chemicals

    def calculate_decay_time(self, type, number_of_halflifes) -> float:
        """
        Calculate the decay time using the inherent half-life.

        Args:
            type (str): Name of the chemical.
            number_of_halflifes (int): Number of half-lives.

        Returns:
            float: The calculated decay time.
        """
        return pow(0.5, number_of_halflifes) * self.radioactive_chemicals[type]["halflife"]

    def calculate_remaining_gram(self, gram, number_of_halflifes) -> float:
        """
        Calculate the remaining mass after a given number of half-lives.

        Args:
            gram (float): Initial mass in grams.
            number_of_halflifes (int): Number of half-lives.

        Returns:
            float: The remaining mass.
        """
        return gram * pow(0.5, number_of_halflifes)

    def calculate_siverts(self, type, gram) -> float:
        """
        Calculate the siverts based on the chemical's properties and mass.

        Args:
            type (str): Name of the chemical.
            gram (float): Mass in grams.

        Returns:
            float: The calculated siverts.
        """
        return self.radioactive_chemicals[type]["siverts_per_gram"] * gram

    def calculate_risk(self, type, gram) -> tuple:
        """
        Determine the risk level based on calculated siverts.

        Args:
            type (str): Name of the chemical.
            gram (float): Mass in grams.

        Returns:
            tuple: A tuple with a string representing risk and the siverts value.
        """
        siverts = self.calculate_siverts(type, gram)
        if siverts < 1:
            return "Safe", siverts
        elif 1 <= siverts < 5:
            return "Unsafe", siverts
        else:
            return "Deadly", siverts

def test():
    """
    Console interface for the Fallout calculations.
    """
    type = input("Chemical type: ")
    gram = float(input("Amount in gram: "))
    number_of_halflifes = int(input("Number of half-lifes: "))

    fallout = Fallout()
    risk, siverts = fallout.calculate_risk(type, fallout.calculate_remaining_gram(gram, number_of_halflifes))
    decay_time = fallout.calculate_decay_time(type, number_of_halflifes)
    print(f"Risk: {risk}")
    print(f"Siverts: {siverts}")
    print(f"Decay time: {decay_time}")

if __name__ == "__main__":
    test()