data = "2023-04-24 09:03:32.744178"

split_data = lambda x: x.split(" ")

date_part, time_part = split_data(data)

year = (lambda x: x.split("-")[0])(date_part)
month = (lambda x: x.split("-")[1])(date_part)
day = (lambda x: x.split("-")[2])(date_part)

time = time_part

print(year)
print(month)
print(day)
print(time)