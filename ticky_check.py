#!/usr/bin/env python3
import sys
import re
import csv
import operator

errors = {}  # number of diff error messages
per_user = {}

errors_report = 'error_message.csv'
per_user_report = 'user_statistics.csv'

logfile = 'syslog.log'

pattern = r'(?P<messageType>INFO|ERROR):?\s*(?P<message>.*?)\((?P<username>\w+)\)$'

with open(logfile, 'r') as file:
    for line in file.readlines():
        regex_result = re.search(pattern, line)
        if regex_result:
            message_type = regex_result.group('messageType')
            message = regex_result.group('message')
            username = regex_result.group('username')
            if message_type == 'ERROR':
                errors.setdefault(message, 0)
                errors[message] += 1
                per_user.setdefault(username, [0, 0])[1] += 1
            else:
                per_user.setdefault(username, [0, 0])[0] += 1
error_sorted = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
per_user_sorted = sorted(per_user.items())

with open(errors_report, 'w', newline='') as error_report:
    writer = csv.writer(error_report)
    writer.writerow(['Error', 'Count'])
    writer.writerows(error_sorted)

with open(per_user_report, 'w', newline='') as user_report:
    writer = csv.writer(user_report)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for item in per_user_sorted:
        onerow = [item[0], item[1][0], item[1][1]]
        writer.writerow(onerow)
        
       sudo chmod +x csv_to_html.py 
       sudo chmod  o+w /var/www/html
       chmod +x ticky_check.py
       ./csv_to_html.py error_message.csv /var/www/html/<html-filename>.html
       [linux-instance-external-IP]/[html-filename].html
       
       Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net
TO RUN
