## Make Decrementing For Loops easier
If you're proficient in VS Code & User Snippets, you can ignore this. If you're a little newer to the tool, here an extremely brief tutorial on how to add functionality to the tool.

### Add a reverse for-loop snippet

1. In VSCode, bring up the Command Palette by typing cmd+shift+p 
1. At the > prompt, type `Configure User Snippets`
1. It will list the many Snippets files you could customize.  
If you started from inside a javascript file, it will suggest `javascript.json`, otherwise type this and hit Enter.

    ***
    If this is the first time you're editing this file, you   will see several lines of comments. It's a description and example template.
    ***

1. Add a blank line above the closing curly brace at the end of the file.
1. Insert the following block at that point:

    ```js
    "Reverse For Loop": {
	    "prefix": ["forr", "for-reverse"],
    	"body": ["for (let ${1:i} = ${2:array.length}; ${1} >=   ${3:0}; ${1}-- ) {", "\t$0", "}"],
    	"description": "A decrementing for loop."
	    }
    
    ```
1. Save and close the javascript.json file

### Test drive your new snippet
In your code file, type:

   ```js
    forr(Tab)
    x(Tab)
    3(Tab)
    1(Tab)
    console.log(x)
   ```
If you have questions or problems, give a shout.
