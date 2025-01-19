import schedule
import time
from classes.CsvSource import CsvSource
from classes.TxtSource import TxtSource

# Function that checks for new files
def check_for_new_files():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()

# Scheduling the function exectuion for every 10 seconds
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()

# Creating a loop that will never end to keep checking the addition of new files
while True:
    schedule.run_pending()
    time.sleep(1)  # Wait 1 second for the next iteration
