#9. Write a python program to add some days to your present date and print the date added
from datetime import datetime, timedelta
print(datetime.today())
new_date=datetime.today()+timedelta(12)
print(new_date)