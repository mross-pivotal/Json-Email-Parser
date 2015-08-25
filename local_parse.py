import json
from os import listdir
from os.path import isfile, join
import os.path


my_keys = {"Email":[],"Category":[],"bcc":[],"MSGID":"","Content":[],"Name":[],"TextParseTime":""}

email_content = []
def go_deeper(key,obj):
    if isinstance(obj,list):
        # print "about to iterate over {0}".format(obj)
        for item in obj:
            # print item
            go_deeper(key,item)
    elif isinstance(obj,dict):
        for key, value in obj.iteritems():
            # print "{0}:{1}".format(key,value)
            if key == "Paragraphs":
                # print "Content value is {0}".format(value)
                for content in value:
                    email_content.append(content["Content"])
            elif key in my_keys:
                go_deeper(key,value)
    else:
        if key in my_keys:
            # print "appending {0}".format(obj)
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
