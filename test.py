import json
c= {"D":["ftoo much nesting"]}
str_email ='{ "TextParseTime":0.100195,"cc":["1123","asd","123123"],"Receipient_Internal":0,"DateTime":"2015/07/21 11:54:47","Body":"","From":[{ "Category": ["Big Data","Cloud Cloud Cloud!"],"Name": "Brats","IntExt": "External","Email":"tankers@brassington.com"},{ "Category": ["Data Resevoirs", "Lakes Lakes Lakes"],"Name": "Brassington","IntExt": "External","Email":"blankers@brass.com"}],"MSGID":"<000001d0c3ac$0a9b3740$1fd1a5c0$@brassington.com>","recipient":["sdfgfgs"],"Content":[{"Type": "Subject","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","subject"]}]},{"Type": "Body","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","default","text","0.11236187123"]},{"Content": "OPEN VESSEL DWT FLG YR PORT COMMENT FLEET" ,"Type":["text","default","text","0.13719117202061745"]}]}],"bcc":["asfdasdf"],"Type":"Email","Sender_DoddFrank":0,"ExclusionScore":0.23414324}'
my_json = json.loads(str_email)

# my_keys = { "Category":"[]","From":"[]","Email":"","TextParseTime":"","Content":""}
my_keys = {"Email":[],"Category":[],"cc":[],"MSGID":"","Content":[],"Name":[],"TextParseTime":""}
# my_keys = {"Email":[],"Content":""}
final_values=[]
# my_json = json.loads(q)
arr = []

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
                #in content block
                go_deeper(key,value)

    else:
        if key in my_keys:
            print "appending {0}".format(obj)
            my_keys[key].append(obj)
            arr.append(obj)
    return arr

for key, value in my_json.iteritems():
    # print key
    if key in my_keys and (isinstance(value,list) == False and isinstance(value,dict) == False):
        print "extracting top level values for {0}:{1}".format(key,value)
        # print "final value is {0}".format(tuple(go_deeper(value)))
        my_keys[key] = value
        # final_values.append(value)
        arr = []
    else:
        # print "final value is {0}".format(go_deeper(value))
        # print "extracting values for {0}:{1}".format(key,value)
        go_deeper(key,value)
        arr = []
        # print "Doing nothing with {0}".format(key)
my_keys["Content"] = email_content

print(my_keys)
