import sys
import itertools

lines = sys.stdin.readlines()
#with open("input.txt", "r") as file:
 #  lines = file.readlines()

lines = [l.strip() for l in lines]

tests = lines[0]
lines.remove(lines[0])

lines = [l.replace(" ", "") for l in lines]

def leap_year(yer):
   bool = False
   if not yer % 4 and yer % 100:
      bool = True
   elif not yer % 400:
      bool = True
   return bool


for line in lines:
   date_counter = 0
   first_date = (13, 32, 9999)
   dates = []
   for y in list(set(itertools.permutations(line))):
      year = int(y[4] + y[5] + y[6] + y[7])
      day = int(y[0] + y[1])
      month = int(y[2] + y[3])
      if 0 < month <= 12:
         if 0 < day <= 31:
            if month == 2:
               if day <= 29:
                  if not leap_year(year):
                     if day <= 28:
                        if year >= 2000:
                           date_counter += 1
                           dates.append((month, day, year))
                           if year < first_date[2]:
                              first_date = (day, month, year)
                           elif month < first_date[1] and year <= first_date[2]:
                              first_date = (day, month, year)
                           elif day < first_date[0] and month <= first_date[1] and year <= first_date[2]:
                              first_date = (day, month, year)
                  else:
                     if year >= 2000:
                        date_counter += 1
                        dates.append((month, day, year))
                        if year < first_date[2]:
                           first_date = (day, month, year)
                        elif month < first_date[1] and year <= first_date[2]:
                           first_date = (day, month, year)
                        elif day < first_date[0] and month <= first_date[1] and year <= first_date[2]:
                           first_date = (day, month, year)

            elif month in [4, 6, 9, 11]:
               if day <= 30:
                  if year >= 2000:
                     date_counter += 1
                     dates.append((month, day, year))
                     if year < first_date[2]:
                        first_date = (day, month, year)
                     elif month < first_date[1] and year <= first_date[2]:
                        first_date = (day, month, year)
                     elif day < first_date[0] and month <= first_date[1] and year <= first_date[2]:
                        first_date = (day, month, year)

            else:
               if year >= 2000:
                  date_counter += 1
                  dates.append((month, day, year))
                  if year < first_date[2]:
                     first_date = (day, month, year)
                  elif month < first_date[1] and year <= first_date[2]:
                     first_date = (day, month, year)
                  elif day < first_date[0] and month <= first_date[1] and year <= first_date[2]:
                     first_date = (day, month, year)

   if date_counter > 0:
      print(f"{date_counter} {str(first_date[0]).zfill(2)} {str(first_date[1]).zfill(2)} {first_date[2]}")
   else:
      print(date_counter)
