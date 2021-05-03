months = {
    "jan":31,
    "feb": 28,
    "mar":31,
    "april":30,
    "may":31,
    "jun":30,
    "july":31,
    "aug":31,
    "sep":30,
    "oct":31,
    "nov":30,
    "dec":31
}

def get_days_count_of_year(month, days):
    day_count = days
    for key, value in months.items():
        print(key, value)
        if key == month:
            return day_count
        else:
            day_count += value
    return day_count


if __name__ == '__main__':
    print(get_days_count_of_year('jan', 1))