from datetime import datetime
from dateutil import tz, parser
from dateutil.relativedelta import relativedelta


PYCON_DATE = parser.parse("May 12, 2021 8:00 AM")
PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))

def time_amount(time_unit: str, countdown: relativedelta) -> str:
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""

def main():
	now = datetime.now(tz=tz.tzlocal())
    countdown = relativedelta(PYCON_DATE, now)
    time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
	output = []
    for tu in time_units:
		t = time_amount(tu, countdown)
		if t:
			output.append(t)
	pycon_date_str = PYCON_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
    print(f"PyCon US 2021 will start on:", pycon_date_str)
    print("Countdown to PyCon US 2021:", ", ".join(output))

if __name__ == "__main__":
    main()


if __name__ == '__main__':
	# now = datetime.now(tz=tz.tz.UTC)
	PYCON_DATE_ = parser.parse("DEC 20, 2021 8:00 AM")
	PYCON_DATE_ = PYCON_DATE_.replace(tzinfo=tz.gettz("WAT"))
	now = datetime.now(tz=tz.tzlocal())
	# # PYCON_DATE = datetime(year=2021, month=5, day=12, hour=8)
	# countdown = relativedelta(PYCON_DATE_, now)
	# print(countdown)
	#
	# print(type(now), type(PYCON_DATE_))
	#
	#
	# print(f'countdown to pycon US 2021: {countdown}')

	def time_amount(time_unit: str, countdown: relativedelta) -> str:
		t = getattr(countdown, time_unit)
		return f"{t} {time_unit}" if t != 0 else ""


	countdown = relativedelta(PYCON_DATE_, now)
	time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
	output = []
	for tu in time_units:
		t = time_amount(tu, countdown)
		if t:
			output.append(t)
	# output = (t for tu in time_units if (t := time_amount(tu, countdown)))
	print("Countdown to PyCon US 2021:", ", ".join(output))