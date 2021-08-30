# Setting up my SDF account to use GitHub ssh

## Make a rsa ssh key


    -bash-5.1$ ssh-keygen -t rsa -f sdfkeyforgit -b 4096 -C "rw36626+github.gmail.com"
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in sdfkeyforgit
    Your public key has been saved in sdfkeyforgit.pub
    The key fingerprint is:
    SHA256: (redacted)  rw36626+github.gmail.com
    The key's randomart image is:
    +---[RSA 4096]----+
    (redacted)
    +----[SHA256]-----+
    -bash-5.1$ 
    -bash-5.1$ ls -al
    total 56
    drwx------   2 cowccca  arpa   512 Aug 25 20:09 .
    drwx------  34 cowccca  arpa  1536 Aug 25 19:37 ..
    -rw-------   1 cowccca  arpa  1776 Jun 14 20:13 authorized_keys
    -rw-------   1 cowccca  arpa  4738 Aug 21  2020 known_hosts
    -rw-------   1 cowccca  arpa  3389 Aug 25 20:09 sdfkeyforgit
    -rw-------   1 cowccca  arpa   750 Aug 25 20:09 sdfkeyforgit.pub


## Starting the ssh agent on MacOs

The following will start ssh-agent as a background process.

	eval "$(ssh-agent)"

## Add the private key to ssh agent

**ssh-add -k keytforgit**
    
    rfwoods@crane xview % ssh-add -k ~/.ssh/keyforgit
    Identity added: /Users/rfwoods/.ssh/keyforgit (rw36626+github@gmail.com)
    rfwoods@crane xview % ssh-add -L
    ssh-rsa AAAAB


## Test access to GitHub


    rfwoods@crane xview % ssh -T git@github.com
    Warning: Permanently added the RSA host key for IP address '140.82.113.4' to the list of known hosts.
    Hi COBRCTEAM! You've successfully authenticated, but GitHub does not provide shell access.

