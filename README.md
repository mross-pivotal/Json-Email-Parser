
# Python-Json-Parser
# JPMC Greenplum JSON Parser

This will describe the parsing syntax on how to use the JSON parser that most likely will be executed in a PL/Pyhton script.  

Right now the way the script functions is based on the function find_key(str,str).  The script takes two variables, one the parsing syntax, and an indicator of whether you want the function to return a single value or an array of values.  Let's look at this sympol example.

```
{
"Firstname": "Suzie",
"Lastname": "Q"
}
```

Let's say I wanted to concatonate the first and last name together and print them.  You would do this.

```
print find_key("Firstname","value") + find_key("Lastname","value")
```

The reason we designed it this way was to reach the far down nested values.  By giving a very specific path to our parser, we know we will be recieving exactly what we want.  Let's look at this example.
```
{
"Attatchments":[
    {"ContentType":"Text",
    "FileSize":"234",
    "ID":"124234234234"},
    {"ContentType":"Text",
    "FileSize":"110",
    "ID":"124567987"}
    ]
}
```
In order to access the ID's being held in this Attatchment we will use this function call.
```
find_key("Attatchments:[:{:ID","array")
```
The parsing syntax is very straightforward.  You give the highest level key, and then the values you want to further iterate onto down the data structure.  So since we want the ID values for this object we say for the value of Attatchments, which is an array, look at the dictionary, at key ID.  

Here's another example
```
{
"cc":["bob@pivotal.io","jane@pivotal.io","jeff@pivotal.io"]
}
```


Now while this isn't a nested structure, we are still returning an array of values, so we're going to want to say that we want the top most key, and then decalre the value we want like this.

```
find_key("cc:[","array")
```

The purpose of being this verbose is so that we can be extremely specific in saying what we want from the object, this comes in handy in tricky situations like this.
```
{
"From":
    [
        { "Category": ["Big Data","Cloud Native"],"Name": "tankers","IntExt":  "External","Email":"tankers@brassington.com"},
        { "Category": ["Data Lake", "HDFS"],"Name": "Brassington","IntExt": "External","Email":"blankers@brass.com"}
    ]
}
```
All we have to do to get the Categories is this.
```
find_key("From:[:{:Category","array")
```

And finally sometimes we only want the value based on a conditional value, this comes with it's own syntax.  Consider the following object.
```
{
    "Content":[
        {"Type": "Subject","Paragraphs":[
            {"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" , "Type":["text","subject"]}]}
        ,{"Type": "Body","Paragraphs":[
            {"Content": "OPEN POSITIONS 2855 DWT DPP 21TH JULY" ,"Type":["text","default","text","0.11236187123"]},
            {"Content": "OPEN VESSEL DWT FLG YR PORT COMMENT FLEET" ,"Type":["text","default","text","0.13719117202061745"]}]}]
}
```
If we wanted only the content from this object, contained within the body, we need to tell the parser that.  We can get the all the content within the body of this email using this syntax.  
```
find_key("Content:[:{:Type=Body:Content","array")
```
This specific case is a little less verbose because we needed to hard code in this functionality.  That equals sign syntax does not work for every case, and you will need to hard code it in if you want it to work for any other keys than syntax.  

The purpose of this parser is too be as specific as possible, and while you might need to explicitly give the path to every value you want, you can be sure that you are being returned what you expect.  
