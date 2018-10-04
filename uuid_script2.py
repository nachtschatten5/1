#!/usr/bin/python
# -*-coding: utf8 -*-

import uuid
import datetime


var_your_uuid = uuid.uuid4()
print ('Here We Go:', var_your_uuid)
var_clean_uuid = str(var_your_uuid)
print ('Your UUID:', var_clean_uuid)
var_uuid_hex = var_your_uuid.hex
print ('Your UUID in Hex:', var_uuid_hex)
#above is self explanitory below we are writing to a file.
#unique dattime filename
epoch_time = datetime.datetime.now().timestamp()
var_easydate = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
var_datefile_output = ('your_UUID_Generated_On--' + var_easydate + '.txt')
with open(var_datefile_output, 'w', newline='\n') as uuid_file: #the w option overwrite the file. look at open() documentation
    uuid_file.write('Epoch Time: ' + str(epoch_time) + '\n')
    uuid_file.write('UUID: ' + str(var_your_uuid) + '\n')
    uuid_file.write('Clean UUID: ' + str(var_clean_uuid) +'\n')
    uuid_file.write('Your Hex UUID: ' + str(var_uuid_hex) + '\n')
    uuid_file.write('Date: ' + str(var_easydate) + '\n')
print('A file has been created in the the folder your ran this script from. The filname is:   ' + var_datefile_output)