# made this script to search for leaving Annalect employees
# need to get this reviewed to make sure im searching in all 
# the potentials locations

import os

directory = os.listdir("/Users/trenton.ornelas/Documents/gitlab/terraform_live/aws/accounts/ann01-tioprod/global/iam-users")
iam_folder = " $HOME/Documents/gitlab/terraform_live/aws/accounts/ann01-tioprod/global/iam-users"

# store employees who are leaving in array
with open("leaverlist.txt") as userlist:
    mylist = userlist.read().splitlines() 


# search terraform_live repo for files that contain our users:
with open("searchresults.txt", 'w') as report:
    for user in mylist:
        grep_search = 'grep -Hrn ' + user + iam_folder
        stream = os.popen(grep_search)
        output = stream.read()
        report.write(output)
