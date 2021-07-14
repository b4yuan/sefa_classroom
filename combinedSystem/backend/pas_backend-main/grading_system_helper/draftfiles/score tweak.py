from datetime import date


def tweak(score, year_sub, month_sub, day_sub, year_due, month_due, day_due):
    date_sub = date(year_sub, month_sub, day_sub)
    date_due = date(year_due, month_due, day_due)
    date_diff = (date_due - date_sub).days
    # print(date_diff)
    if date_diff >= 7:
        score = 1.1 * score
    elif 0 <= date_diff < 7:
        score = score * (1 + date_diff * 0.01)
    else:
        score = score * (1 + date_diff * 0.2)
    if score < 0:
        score = 0
    return int(score)

score = 100
year_sub = 2021
month_sub = 3
day_sub = 22
year_due = 2021
month_due = 3
day_due = 22
final_score = tweak(score, year_sub, month_sub, day_sub, year_due, month_due, day_due)
print(final_score)