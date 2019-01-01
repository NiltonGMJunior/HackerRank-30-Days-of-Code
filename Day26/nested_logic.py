def calculateFine(actual_date, expected_date):
    year_diff = actual_date[2] - expected_date[2]
    month_diff = actual_date[1] - expected_date[1]
    day_diff = actual_date[0] - expected_date[0]
    if year_diff > 0:
        return 10000
    if month_diff > 0 and year_diff == 0:
        return 500 * month_diff
    if day_diff > 0 and month_diff == 0 and year_diff == 0:
        return 15 * day_diff
    return 0


if __name__ == '__main__':
    # actual_date = list(map(int, input().split()))
    # expected_date = list(map(int, input().split()))
    actual_date = list(map(int, "31 12 2009".split()))
    expected_date = list(map(int, "1 1 2010".split()))
    print(calculateFine(actual_date, expected_date))
