import json

str_email ='{"SearchContent0":[{"Type":"Email","Content":"Hi mom"}], "TextParseTime":0.100195,"cc":["1123","asd","123123"],"Receipient_Internal":0,"DateTime":"2015/07/21 11:54:47","Body":"","From":[{ "Category": ["Big Data","Cloud Cloud Cloud!"],"Name": "Brats","IntExt": "External","Email":"tankers@brassington.com"},{ "Category": ["Data Resevoirs", "Lakes Lakes Lakes"],"Name": "Brassington","IntExt": "External","Email":"blankers@brass.com"}],"MSGID":"<000001d0c3ac$0a9b3740$1fd1a5c0$@brassington.com>","recipient":["sdfgfgs"],"Content":[{"Type": "Subject","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","subject"]}]},{"Type": "Body","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","default","text","0.11236187123"]},{"Content": "OPEN VESSEL DWT FLG YR PORT COMMENT FLEET" ,"Type":["text","default","text","0.13719117202061745"]}]}],"bcc":["asfdasdf","hardy","harr"],"Type":"Email","Sender_DoddFrank":0,"ExclusionScore":0.23414324}'
# str_email = '{"SearchContent0":[{Type:"Email":"Content":"Hi mom"}]}'
my_json = json.loads(str_email)

# my_keys = { "Category":"[]","From":"[]","Email":"","TextParseTime":"","Content":""}
# my_keys = {"Email":[],"Category":[],"cc":[],"MSGID":"","Content":[],"Name":[],"TextParseTime":"","SearchContent0":[]}
my_keys = { "NumUsers":"","NumSenders":"","NumRecipients":"","Sender_Internal":"","Sender_External":"","Recipient_Internal":"","Recipient_External":"","Recipient_Private":"","Recipient_AntiTrust":"","Recipient_DoddFrank":"","NumFlaggedUsers":"","Type":"","MsgID":"","FileSize":"","DirName":"","Direction":"","ExclusionScore":"","Exclude":"","Exclude_S6":"","Exclude_Internal_S6":"","DateTime":"","DateTimeUTC":"","Date":"","Time":"","StartTime":"","StartTimeUTC":"","EndTime":"","EndTimeUTC":"","ChatDuration":"","Subject":"","Greeting":"","Content":[[],[]],"SearchContent0":[[],[]],"SearchContent1":"","RegEx_Entities":"","NE":[],"Attatchments":[],"RemovedAttatchments":"","NumAttatchmentsRemoved":"","NumAttatchments":"","Hits0":[],"Hits1":[],"NumHits0":"","NumHits1":""}

# print my_keys

# my_keys = {"Email":[],"Content":""}
arr = []

search_content = [[],[]]
email_content = [[],[]]
# def go_deeper(key,obj):
#     if isinstance(obj,list):
#         # print "about to iterate over {0}".format(obj)
#         if key == "SearchContent0":
#             for content in obj:
#                 search_content[0].append(content["Type"])
#                 search_content[1].append(content["Content"])
#                 print "search_content is now {0}".format(search_content)
#         else:
#             for item in obj:
#                 print item
#                 go_deeper(key,item)
#     elif isinstance(obj,dict):
#         for dict_key, value in obj.iteritems():
#             print "Parent key is {0}".format(key)
#             print "{0}:{1}".format(dict_key,value)
#             if key == "Content":
#                 print "Content value is {0}".format(value)
#                 if dict_key == "Type":
#                     email_content[0].append(value)
#                 else:
#                     for content in value:
#                         print "Appending {0} to {1}".format(content,email_content)
#                         email_content[1].append(content["Content"])
#             elif dict_key in my_keys:
#                 #in content block
#                 go_deeper(dict_key,value)
#
#     else:
#         if key in my_keys:
#             print "appending {0} to {1}".format(obj,key)
#             print my_keys[key]
#             my_keys[key].append(obj)
#             arr.append(obj)
#     return arr
#
# for key, value in my_json.iteritems():
#     # print key
#     if key in my_keys and (isinstance(value,list) == False and isinstance(value,dict) == False):
#         print "extracting top level values for {0}:{1}".format(key,value)
#         print my_keys[key]
#         # print "final value is {0}".format(tuple(go_deeper(value)))
#         my_keys[key] = value
#         arr = []
#     else:
#         # print "final value is {0}".format(go_deeper(value))
#         print "extracting values for {0}:{1}".format(key,value)
#         go_deeper(key,value)
#         arr = []
#         # print "Doing nothing with {0}".format(key)
# my_keys["Content"] = email_content
# my_keys["SearchContent0"] = search_content
# print(my_keys)
#"SearchContent0":[{"Type":"Email","Content":"Hi mom"}]
def find_key(my_key,data_type):
    results = []
    tree = my_key.split(":")
    print tree
    if data_type =="array":
        for index,val in enumerate(tree):
            current_index = index +1
            next_index = index +1
            print "val is {0}".format(val)
            print "At index:{0} of tree size:{1} looking at val:{2}".format(next_index,len(tree),val)
            if val == "[":
                if len(tree) == next_index:
                    for obj in my_json[tree[0]]:
                        print "Looking at {0}".format(obj)
                        results.append(obj)
                    return results
                else:
                    for obj in my_json[tree[0]]:
                        if tree[0] != "Content":
                            results.append(obj[tree[-1]])
                        elif isinstance(obj,dict) and "Type" in obj:
                            print next_index
                            print len(tree)


                            print "my obj is {0}".format(obj)

                            type_index = next_index +1

                            print obj["Type"]
                            content_type = tree[type_index]
                            x= content_type.split("=")
                            print x
                            print obj["Type"]
                            print"compare"
                            if x[1] == obj["Type"]:
                                for para in obj["Paragraphs"]:
                                    results.append(para["Content"])
                                return results
                            print "Looking at {0}".format(obj)
                    return results
                next_index += 1
                if len(tree) == current_index:
                    print "hi"
                    return my_json[tree[index-1]]
                elif tree[current_index] == "{":
                    next_index +=1
                    print "At index:{0} of tree size:{1} looking at val:{2}".format(next_index,len(tree),val)
                    print my_json[tree[0]][0]["Content"]
                    print "!!!!"
                    if len(tree) == next_index:
                        return my_json[tree[0]]
            elif val == "{":
                if len(tree) == next_index:
                    print "hi"
                    return my_json[tree[index-1]]
            else:
                if len(tree) == next_index:
                    return my_json[tree[index]]
    else:
        return my_json[tree[0]]

#"Content":[{"Type": "Subject","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","subject"]}]},{"Type": "Body","Paragraphs":[{"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","default","text","0.11236187123"]},{"Content": "OPEN VESSEL DWT FLG YR PORT COMMENT FLEET" ,"Type":["text","default","text","0.13719117202061745"]}]}]
print find_key("Content:[:{:Type=Subject","array")
# print find_key("SearchContent0:[:{:Content","array")
# print find_key("cc:[")
# print find_key("bcc:[","array")
my_json["SearchContent0"][0]["Content"]
