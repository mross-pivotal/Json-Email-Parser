
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

Now while this isn't a nested structure, we are still returning an array of values, so we're going to want to say that we want the top most key, and then decalre the value we want like this.
```
find_key("cc:[","array")
```
