from pkg.divide import Divider
from pkg.multiply import Multiply


class ExtractPercentage:
    @staticmethod
    def extract_percentage(number, percentage):
        result_mul = Multiply.multiply(number, percentage)
        result_div = Divider.divide(result_mul, 100)
        return result_div
