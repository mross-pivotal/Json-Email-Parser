import json
c= {"D":["ftoo much nesting"]}
str_email ='{ "TextParseTime":0.100195,"cc":["1123","123123"],"Receipient_Internal":0,"DateTime":"2015/07/21 11:54:47","Body":"","From":[{ "Category": ["Big Data","Cloud Cloud Cloud!"],"Name": "Brassington","IntExt": "External","Email":"tankers@brassington.com"},{ "Category": ["Data Resevoirs", "Lakes Lakes Lakes"],"Name": "Brassington","IntExt": "External","Email":"blankers@brass.com"}],"MSGID":"<000001d0c3ac$0a9b3740$1fd1a5c0$@brassington.com>","recipient":["sdfgfgs"],"Content":[{"Type": "Subject","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","subject"]}]},{"Type": "Body","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","default","text","0.11236187123"]},{"Content": "OPEN VESSEL DWT FLG YR PORT COMMENT FLEET" ,"Type":["text","default","text","0.13719117202061745"]}]}],"bcc":["asfdasdf"],"Type":"Email","Sender_DoddFrank":0,"ExclusionScore":0.23414324}'
my_json = json.loads(str_email)

# my_keys = {"TextParseTime": "", "Content": "", "MSGID": ""}
# def go_deeper(obj):
#     if isinstance(obj,list):
#         for item in obj:
#             go_deeper(item)
#             return ( 44, item ,["hello","world"])
#     #elif isinstance(obj,dict):
#      #   for key, value in obj.iteritems():
#       #      go_deeper(value)
#        #     #return value
#     else:
#         return ( 7, "return" ,["hello","world"])
arr = []


q = '{"cc": ["123","456"], "From":[{ "Category": ["Big Data","Cloud Cloud Cloud!"],"Name": "Brassington","IntExt": "External","Email":"tankers@brassington.com"},{ "Category": ["Data Resevoirs", "Lakes Lakes Lakes"],"Name": "Brassington","IntExt": "External","Email":"blankers@brass.com"}]}'

my_keys = { "Category":"[]","From":"[]","Email":"","TextParseTime":"","Content":""}
# my_keys = { "cc": "","From":"","Email":"[]"}


# my_json = json.loads(q)
arr = []

email_content = []
def go_deeper(obj):
    if isinstance(obj,list):
        print "about to iterate over {0}".format(obj)
        for item in obj:
            # print item
            go_deeper(item)
    elif isinstance(obj,dict):
        for key, value in obj.iteritems():
            print "{0}:{1}".format(key,value)
            if key in my_keys and  key == "Content":
                print "Content value is {0}".format(value)
                email_content.append(value)

            else:
                #in content block
                go_deeper(value)

    else:
        print "appending {0}".format(obj)
        arr.append(obj)
    return arr

for key, value in my_json.iteritems():
    if key in my_keys:
        print "final value is {0}".format(tuple(go_deeper(value)))


print(email_content)
# print(my_keys["cc"])
