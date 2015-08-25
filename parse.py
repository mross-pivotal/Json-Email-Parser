import json

# print json.dumps(str_email)
import types
# str_email= '{ "TextParseTime": 0.100195, "cc": [], "Reciepient_Internal": 0, "DateTime": "2015/07/21 11:54:47","Body": "","from": [{ "Category": [],"Name": "Brassington","IntExt": "External","Email": "tankers@brassington.com"}],"MsgID": "<000001d0c3ac$0a9b3740$1fd1a5c0$@brassington.com>", "recipient": [],}'
# print json.loads('{ "TextParseTime": 0.100195, "cc": [], "Reciepient_Internal": 0, "DateTime": "2015/07/21 11:54:47","Body": "","from": []}')
# print str_email["from"]
# str_email = '{ "TextParseTime":0.100195, "cc":[], "Receipient_Internal":0,"DateTime":"2015/07/21 11:54:47", "Body":"", "From":[{ "Category": [],"Name": "Brassington","IntExt": "External","Email":"tankers@brassington.com"}], "Content":[], "bcc":[], "Type":"Email", "Sender_DoddFrank":0, "ExclusionScore":0.23414324 }'

str_email ='{ "TextParseTime":0.100195,"cc":[],"Receipient_Internal":0,"DateTime":"2015/07/21 11:54:47","Body":"","From":[{ "Category": ["Big Data","Cloud Cloud Cloud!"],"Name": "Brassington","IntExt": "External","Email":"tankers@brassington.com"},{ "Category": ["Data Resevoirs", "Lakes Lakes Lakes"],"Name": "Brassington","IntExt": "External","Email":"tankers@brassington.com"}],"MSGID":"<000001d0c3ac$0a9b3740$1fd1a5c0$@brassington.com>","recipient":["sdfgfgs"],"Content":[{"Type": "Subject","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","subject"]}]},{"Type": "Body","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","default","text","0.11236187123"]},{"Content": "OPEN VESSEL DWT FLG YR PORT COMMENT FLEET" ,"Type":["text","default","text","0.13719117202061745"]}]}],"bcc":["asfdasdf"],"Type":"Email","Sender_DoddFrank":0,"ExclusionScore":0.23414324}'
my_json = json.loads(str_email)

my_keys = {"TextParseTime": "", "Content": "", "MSGID": "","From":""}
arr = []
def go_deeper(obj):
    if isinstance(obj,list):
        for item in obj:
            go_deeper(item)
    elif isinstance(obj,dict):
        for key, value in obj.iteritems():
            go_deeper(value)
    else:
        #print obj
        arr.append(obj)
    return arr

def parse_string(str_email):
    my_json = json.loads(str_email)
    print my_json
    final_values = []

    for cc in my_json["cc"]:
        print cc

    for sender in my_json["From"]:
        for key, value in sender.iteritems():
            print "{0},{1}".format(key,value)
        for categories in sender["Category"]:
            print categories

    for recipient in my_json["recipient"]:
        print recipient

    for bcc in my_json["bcc"]:
        print bcc

    #Find keys within the Content Array
    for content in my_json["Content"]:
        final_values.append(content["Type"])
        for paragraph in content["Paragraphs"]:
            final_values.append(paragraph["Content"])
            print paragraph["Content"]
            for paragraph_content_type in paragraph["Type"]:
                print paragraph_content_type



    return tuple(final_values)

#parse_string(str_email)
# print go_deeper([0,2])
# print go_deeper(json.loads('{ "Category": ["Im in the array!","Arrays are awesome"], "Nest": {"Category": ["Im in the nest!!","Nested structures are better"]}, "Name": "Brassington","IntExt": "External","Email":"tankers@brassington.com"}'))
for key, value in my_json.iteritems():
    if key in my_keys:
        print go_deeper(value)
    # print key
# parse_string(str_email)
# print my_json["Content"]
