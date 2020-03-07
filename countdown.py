import datetime

CurrentDate = datetime.datetime.now()

Leave = "30/01/2020 15:00"
Leave = datetime.datetime.strptime(Leave, "%d/%m/%Y %H:%M")

countdown = Leave - CurrentDate
#print ("Hello Guilherme! Your leave will be in: ", countdown.days, "days")
#print ("Hello Guilherme! \nYour leave will be in " + str(countdown.days) + " days!")
print ("Hello Guilherme! \nYour leave will be in {} days!".format(countdown.days))
