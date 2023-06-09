# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


def print_date(date):
    print("Linea 16 (Año) ->",date.year)
    print("Linea 17 (Mes) ->",date.month)
    print("Linea 18 (Dia) ->",date.day)
    print("Linea 19 (Hora) ->",date.hour)
    print("Linea 20 (Minuto) ->",date.minute)
    print("Linea 21 (Segundo) ->",date.second)
    print("Linea 22 ->",date.timestamp())


print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time


current_time = time(21, 6, 0)

print("Linea 36 ->",current_time.hour)
print("Linea 37 ->",current_time.minute)
print("Linea 38 ->",current_time.second)

# Date


current_date = date.today()

print("Linea 45 ->",current_date.year)
print("Linea 46 ->",current_date.month)
print("Linea 47 ->",current_date.day)

current_date = date(2022, 10, 6)

print("Linea 51 ->",current_date.year)
print("Linea 52 ->",current_date.month)
print("Linea 53 ->",current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print("Linea 58 ->",current_date.month)

# Operaciones con fechas

diff = year_2023 - now
print("Linea 63 ->",diff)

diff = year_2023.date() - current_date
print("Linea 66 ->",diff)

# Timedelta


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)