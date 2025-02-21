import math

class EthiopianDateConverter:
    """
    A utility class to convert dates between the Ethiopian and Gregorian calendars.
    """

    @staticmethod
    def start_day_of_ethiopian_year(year: int) -> int:
        """
        Calculates the starting day of the Ethiopian year in the Gregorian calendar.

        :param year: The Ethiopian year
        :return: The Gregorian calendar start day of the Ethiopian year
        """
        new_year_day = math.floor(year / 100) - math.floor(year / 400) - 4
        return int(new_year_day) + 1 if (year - 1) % 4 == 3 else int(new_year_day)

    @staticmethod
    def to_gregorian_date(year: int, month: int, date: int) -> tuple[int, int, int]:
        """
        Converts an Ethiopian date to the Gregorian calendar.

        :param year: Ethiopian year
        :param month: Ethiopian month
        :param date: Ethiopian day
        :return: Tuple (Gregorian year, Gregorian month, Gregorian day)
        """
        new_year_day = EthiopianDateConverter.start_day_of_ethiopian_year(year)
        gregorian_year = year + 7
        gregor_months = [0, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30]
        next_gregorian_year = gregorian_year + 1

        # Adjust February for leap years
        if (next_gregorian_year % 4 == 0 and next_gregorian_year % 100 != 0) or next_gregorian_year % 400 == 0:
            gregor_months[6] = 29

        until = (month - 1) * 30 + date

        # Special case for dates before 1575
        if until <= 37 and year <= 1575:
            until += 28
            gregor_months[0] = 31
        else:
            until += new_year_day - 1

        gregor_month, gregor_date = 0, 0
        for i, days in enumerate(gregor_months):
            if until <= days:
                gregor_month = i
                gregor_date = until
                break
            until -= days

        if gregor_month > 4:
            gregorian_year += 1

        ordered_gregor_months = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return gregorian_year, ordered_gregor_months[gregor_month], gregor_date

    @staticmethod
    def to_ethiopian_date(year: int, month: int, date: int) -> tuple[int, int, int]:
        """
        Converts a Gregorian date to the Ethiopian calendar.

        :param year: Gregorian year
        :param month: Gregorian month
        :param date: Gregorian day
        :return: Tuple (Ethiopian year, Ethiopian month, Ethiopian day)
        """
        if year == 1582 and month == 5 and 5 <= date <= 14:
            raise ValueError("Invalid date")

        gregor_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ethiopian_months = [0, 30, 30, 30, 30, 30, 30, 30, 30, 30, 5, 30, 30, 30, 30]

        # Adjust February for leap years
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            gregor_months[2] = 29

        ethiopian_year = year - 8
        ethiopian_months[10] = 6 if ethiopian_year % 4 == 3 else 5

        new_year_day = EthiopianDateConverter.start_day_of_ethiopian_year(year - 8)
        until = sum(gregor_months[:month]) + date
        tahissas = 26 if ethiopian_year % 4 == 0 else 25

        if year < 1582 or (until <= 277 and year == 1582):
            ethiopian_months[1] = 0
            ethiopian_months[2] = tahissas
        else:
            tahissas = new_year_day - 3
            ethiopian_months[1] = tahissas

        ethiopian_date, ethiopian_month = 0, 0
        for m in range(1, len(ethiopian_months)):
            if until <= ethiopian_months[m]:
                ethiopian_date = until + (30 - tahissas) if m == 1 or ethiopian_months[m] == 0 else until
                ethiopian_month = m
                break
            until -= ethiopian_months[m]

        if ethiopian_month > 10:
            ethiopian_year += 1

        ordered_ethiopian_months = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4]
        return ethiopian_year, ordered_ethiopian_months[ethiopian_month], ethiopian_date