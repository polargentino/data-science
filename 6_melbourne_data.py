import pandas as pd

melbourne_file_path = "/home/pol/melbourne_data/melb_data.csv"  # Ruta corregida
melbourne_data = pd.read_csv(melbourne_file_path)

print(melbourne_data.describe())
#               Rooms         Price  ...    Longtitude  Propertycount
# count  13580.000000  1.358000e+04  ...  13580.000000   13580.000000
# mean       2.937997  1.075684e+06  ...    144.995216    7454.417378
# std        0.955748  6.393107e+05  ...      0.103916    4378.581772
# min        1.000000  8.500000e+04  ...    144.431810     249.000000
# 25%        2.000000  6.500000e+05  ...    144.929600    4380.000000
# 50%        3.000000  9.030000e+05  ...    145.000100    6555.000000
# 75%        3.000000  1.330000e+06  ...    145.058305   10331.000000
# max       10.000000  9.000000e+06  ...    145.526350   21650.000000

