# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import csv


# Your Account SID from twilio.com/console
account_sid = 'xxxx'
# Your Auth Token from twilio.com/console
auth_token = 'xxxx'

client = Client(account_sid, auth_token)

print('Ready to work.')

# Open CSV file with SMS numbers to check
with open('smsnumbers.csv') as csvfile:
    ## Open or create the file to write the output data from twilio
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvfile)
        
        arr = []
        row = reader
        
        for row in reader:
            cardnumber = row[0]
            smsnumber = row[1]
            
            # try to fetch carrier name from twilio api
            try:
                phone_number = client.lookups \
                     .phone_numbers(smsnumber) \
                     .fetch(type=['carrier'])
               
                # append carrier name from fetch
                row.append(phone_number.carrier['name'])
                arr.append(row)
                
                # prints results in console log to confirm its working
                print(smsnumber, phone_number.carrier['name'])
                
            # catch exceptions and errors from twilio lookup
            except Exception as err:
                row.append('invalid')
                arr.append(row)
                print('invalid')
        
        writer.writerows(arr)
        
print('Jobs done.')