# tests/test_chronos.py
import unittest
# from .aion_xtensions_chronos.mapper.chronos_mapper import ChronosMappingBuilder
from ..aion_xtensions_chronos.mapper.chronos_mapper import ChronosMappingBuilder
class TestAionXtensionsChronos(unittest.TestCase):

    def test_generate_mappings(self):
        data = {
            "incident": {
                "group_prediction": ["group_prediction", "agent_prediction", "exp_resolution_time", "fcr", "re_open", "dsat"]
            }
        }
        ax_mapper = ChronosMappingBuilder(data)
        result = ax_mapper.generate_mappings()
        self.assertEqual(result["status"], "success")
        self.assertEqual(len(result["data"]), 1)  # Check if one module is processed
        self.assertIn("AX1", result["data"][0]["incident"]["group_prediction"])

if __name__ == '__main__':
    unittest.main()
