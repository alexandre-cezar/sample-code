__author__ = 'Alexandre S. Cezar - acezar@paloaltonetworks.com'

import sys
import os
import fileinput

# **********************************
# **** Insert the filename here ****
# **********************************
filename = "twistlock_kalilinux_kali_latest.json"
# **********************************

# Read in the file
with open(filename, 'r') as file :
  filedata = file.read()

txt = filedata

file.close()

# Unmount file
x = txt.split(",")

# Update data
i = 0
while i < len(x):
    if x[i] == '"advancedProtection":true':
        x[i] = '"advancedProtection":false'

    elif x[i] == '"processes":{"effect":"alert"':
        i += 1
        while i < len(x) and x[i] != '"checkCryptoMiners":true':

            iposition = 0

            if x[i][1:10] == 'whitelist':
                iposinilist = 14
                txtbase = x[i][0:14]
                txtaux = x[i][14:len(x[i])]
                iposnew = 14
            else:
                txtbase = '"'
                txtaux = x[i]
                iposnew = 0

            iposition = txtaux.rfind('/')

            if iposition == -1:
                txtnew = ""
            else:
                iposnew = iposnew + iposition + 1

                txtnew = x[i][iposnew:len(x[i])]

                x[i] = txtbase + txtnew

            i += 1


    elif x[i] == '"checkLateralMovement":true':
        x[i] = ''

    elif x[i] == '"checkParentChild":true}':
        x[i] = '"checkNewBinaries":true}'

    elif x[i] == '"detectPortScan":true':
        x[i] = '"detectPortScan":false'

    elif x[i] == '"filesystem":{"effect":"alert"':
        x[i] = '"filesystem":{"effect":""'

        i += 2

        while i < len(x) and x[i] != '"checkNewFiles":true':


            if x[i][1:10] == 'whitelist':
                txtnew = '"whitelist":[]'
            else:
                txtnew = ''

            x[i] = txtnew
            i += 1

        i -= 1

    elif x[i] == '"checkNewFiles":true':
        x[i] = '"checkNewFiles":false'

    elif x[i] == '"backdoorFiles":true}':
        x[i] = '"backdoorFiles":false}'

    elif x[i] == '"kubernetesEnforcement":true':
        x[i] = '"kubernetesEnforcement":false'

    elif x[i] == '"cloudMetadataEnforcement":true':
        x[i] = '"cloudMetadataEnforcement":false'

    elif x[i] == '"policyType":"containerRuntime"':
        x[i] = '"policyType":"appEmbeddedRuntime"'

    i += 1

# Mount file

txt2 = ''

i = 0
while i < len(x):
    if x[i] != '':
        if txt2 != '' :
            txt2 = txt2 + ','
        txt2 = txt2 + x[i]
    i += 1


# Create the new file

filename2 = "NewFile_" + filename
with open(filename2, 'w') as file:
  file.write(txt2)

file.close()

