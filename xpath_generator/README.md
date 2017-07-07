# xpath generator
```xml
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>
        <a>Don't forget</a>
        <b>me</b>
        <c>this weekend!</c>
    </body>
</note>
```   
then you can get all xpaths for leaf nodes:
```bash
$ ./xpathgen.py note.xml 
/note/to
/note/from
/note/heading
/note/body/a
/note/body/b
/note/body/c
```