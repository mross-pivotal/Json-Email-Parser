import json
from os import listdir
from os.path import isfile, join
import os.path


# my_keys = {"Email":[],"Category":[],"bcc":[],"MSGID":"","Content":[],"Name":[],"TextParseTime":""}
my_keys = { "NumUsers":"","NumSenders":"","NumRecipients":"","Sender_Internal":"","Sender_External":"","Recipient_Internal":"","Recipient_External":"","Recipient_Private":"","Recipient_AntiTrust":"","Recipient_DoddFrank":"","NumFlaggedUsers":"","Type":"","MsgID":"","FileSize":"","DirName":"","Direction":"","ExclusionScore":"","Exclude":"","Exclude_S6":"","Exclude_Internal_S6":"","DateTime":"","DateTimeUTC":"","Date":"","Time":"","StartTime":"","StartTimeUTC":"","EndTime":"","EndTimeUTC":"","ChatDuration":"","Subject":"","Greeting":"","Content":[[],[]],"SearchContent0":[[],[]],"SearchContent1":"","RegEx_Entities":"","NE":[],"Attatchments":[],"RemovedAttatchments":"","NumAttatchmentsRemoved":"","NumAttatchments":"","Hits0":[],"Hits1":[],"NumHits0":"","NumHits1":""}


search_content = [[],[]]
email_content = [[],[]]
def go_deeper(key,obj):
    if isinstance(obj,list):
        # print "about to iterate over {0}".format(obj)
        if key == "SearchContent0":
            for content in obj:
                search_content[0].append(content["Type"])
                search_content[1].append(content["Content"])
                print "search_content is now {0}".format(search_content)
        else:
            for item in obj:
                print item
                go_deeper(key,item)
    elif isinstance(obj,dict):
        for dict_key, value in obj.iteritems():
            print "Parent key is {0}".format(key)
            print "{0}:{1}".format(dict_key,value)
            if key == "Content":
                print "Content value is {0}".format(value)
                if dict_key == "Type":
                    email_content[0].append(value)
                else:
                    for content in value:
                        print "Appending {0} to {1}".format(content,email_content)
                        email_content[1].append(content["Content"])
            elif dict_key in my_keys:
                #in content block
                go_deeper(dict_key,value)

    else:
        if key in my_keys:
            print "appending {0} to {1}".format(obj,key)
            print my_keys[key]
            my_keys[key].append(obj)
            arr.append(obj)
    return arr

def parse_json_file(my_json):
    for key, value in my_json.iteritems():
        # print key
        if key in my_keys and (isinstance(value,list) == False and isinstance(value,dict) == False):
            # print "extracting top level values for {0}:{1}".format(key,value)
            # print "final value is {0}".format(tuple(go_deeper(value)))
            my_keys[key] = value
            arr = []
        else:
            # print "final value is {0}".format(go_deeper(value))
            # print "extracting values for {0}:{1}".format(key,value)
            go_deeper(key,value)
            arr = []
            # print "Doing nothing with {0}".format(key)
    my_keys["Content"] = email_content
    my_keys["SearchContent0"] = search_content
    print(my_keys)

    print(my_keys)

arr = []
mypath = "."
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for json_file in onlyfiles:
    extension = os.path.splitext(json_file)[1]
    if extension == ".json":
        print json_file
        file = open('data.txt', 'r')

        for line in file:
            my_json = json.loads(line)
        parse_json_file(my_json)
