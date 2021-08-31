# sed Commands by RFW

## Using sed

[Sed Command in Linux/Unix with examples](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)

    #! /bin/zsh
    # Script to modify Xview make files
    # using sed
    # 8/30/2021
    # RFW
    
    
    sed -i .bak  's/cc/$(CC) $(CLFAGS)/g' *
