############  GIT   ################################
*master
 remotes/origin/DMX-18109_DataFunnelUI
  remotes/origin/DMX-24108_Merge_to_1_git
  remotes/origin/DMX-24264_Oracle_to_Kafka_CDC
  remotes/origin/HEAD -> origin/master
  remotes/origin/build-test
  remotes/origin/master
https://github.com/dornellaskj/react-SEO-starter.git

We now have a new 1.3.0 branch in the data-funnel-ui GIT repository. This branch is for the production version of the DataFunnel UI. This branch should only be used for checking in bug fixes directly related to that version number, all other changes such as new functionality should be checked into the master branch. 
 
# GIT ADVANCED 2 ##############
 
alias graph="git log --all --decorate --oneline --graph"
graph
git add file; git commit -m "added file"
git commit -a -m "added file"
//fast forward merge 
//master and branche have direct path, master moves up to branch.
git checkout master
git diff master..branche
$ git branch --merged
git branch -d branche
git branch -d 
//3-way merge ->make a merge commit

## GIT INIT 2 #####
git init //initialize
git add  . // <file> add files.
git status
git commit -m "first tmm commit"  //first commit
git push // push to remote repo
git pull // pull latest from remote
git clone //
git log --oneline
git push origin --force // local overwrites remote 
##### merge the master branch into the feature branch 
git checkout <branchname>
git merge master 
##### shorter: git merge master feature
##### rebase option: alt.to merge, rebase feature branch onto master branch
##### rebase moves entire feature branch to begin on the tip of the master branch, #####including all of new commits in master (re-writes project history 
git checkout feature 
##### 
git rebase master
	First, rewinding head to replay your work on top of it...
	Applying:  On branch testbranch
	error: Failed to merge in the changes.
	Using index info to reconstruct a base tree...
	M       index.html
	Falling back to patching base and 3-way merge...
	Auto-merging index.html
	CONFLICT (content): Merge conflict in index.html
	Patch failed at 0001  On branch testbranch
	The copy of the patch that failed is found in: .git/rebase-appl
	y/patch
When you have resolved this problem, run "git rebase --continue
".If you prefer to skip this patch, run "git rebase --skip" inste
ad.To check out the original branch and stop rebasing, run "git re
base --abort".
]] 



###DIFF  
git diff // compares working directory with index, i.e. shows the changes that are not staged yet.
git diff HEAD // compares working directory with local repository. shows the list of changes after your last commit. 
git diff HEAD [filename] //  compare the working directory with local repository.
git diff [filename] // compare the working directory with index.
git diff --cached [filename] // compare the index with local repository; shows the diff between your last commit and changes to be committed next  

C:\vraa\projects\helloworld> edit .\helloworld.txt
C:\vraa\projects\helloworld> git diff HEAD .\helloworld.txt
diff --git a/helloworld.txt b/helloworld.txt
 
git clone --depth=16 https://github.com/angular/angular-phonecat.git
git config --global url."https://".insteadOf git://


###BRANCH -REMOTE
git branch --all   
--> see remotes
git checkout -f step-0
-->You are in 'detached HEAD' state. You can look around, make experimental
	changes and commit them, and you can discard any commits you make in this state without impacting any branches by performing another checkout.  If you want to create a new branch to retain commits you create, you may  do so (now or later) by using -b with the checkout command again. Example:
git checkout -b branchxyz  origin/branchxyz
-->Branch 'branchxyz' set up to track remote branch 'branchxyz' from 'origin'.
git branch branchxyz origin/branchxyz
//
 git checkout -b feature_branch_name.
 --->make branch locally, edit, add, commit
 git push -u origin feature_branch_name
 -->push branch to remote repo
//
git pull origin master , tells git to fetch and merge specifically the master branch (from the remote named origin , to be even more precise).
git pull fetches updates for all local branches, which track remote branches, and then merges the current branch

#### GIT   REMOTE 2 #################################:
git clone https://github.com/thomasm1/AddHealthParenWorkWave1_4
git remote -v1
git branch -a


Cloning repo into 'ticgit'...
git clone https://github.com/thomasm1/ticgit 
$ cd ticgit
$ git remote
origin
$ git remote -v
origin	https://github.com/thomasm1/ticgit (fetch)
origin	https://github.com/thomasm1/ticgit (push)
$ cd grit
$ git remote -v
bakkdoor  https://github.com/bakkdoor/grit (fetch)
bakkdoor  https://github.com/bakkdoor/grit (push) 
origin    git@github.com:mojombo/grit.git (fetch)
origin    git@github.com:mojombo/grit.git (push)	
 
echo "# AddHealthParenWorkWave1_4" >> README.md 
git remote add origin https://github.com/thomasm1/AddHealthParenWorkWave1_4.git
git push -u origin master 
https://github.com/thomasm1/AddHealthParenWorkWave1_4.git  
#### Omit --global to set the identity only in this repository. 
 Either specify the URL from the command-line or configure a remote repository using:
  git remote add origin https://github.com/thomasm1.git  # and then push using the remote name
  git push --set-upstream origin master.  
  git push <name>
# git untracking 
  git rm --cached FILENAME
  git config --global core.excludesfile ~/.gitignore_global 
#git submodule ## for embedded repositories within existing repository
 git submodule add "https://github.com/d3/d3.git" d3
###STASH
git stash list [<options>]
git stash show [<stash>]
git stash drop [-q|--quiet] [<stash>]
git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
git stash branch <branchname> [<stash>]
git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
	     [-u|--include-untracked] [-a|--all] [-m|--message <message>]
	     [--] [<pathspec>…​]]
git stash clear
git stash create [<message>]
git stash store [-m|--message <message>] [-q|--quiet] <commit>

##################### GIT 2 ... ###########################

#### 	UNSTAGE:  
git rm --cached index.html 
git add app.html 
git rm --cached app.html  //	UNSTAGE:  
git status
git add *.html   //both index and app staged, not yet committed
git add . // seems to update everything
git branch d3
git commit -m 'd3'
git checkout branch 

#### GIT DAILY-TECH    
core.symlinks=false
core.autocrlf=input
core.fscache=true
color.diff=auto
color.status=auto
color.branch=auto
color.interactive=true
help.format=html
rebase.autosquash=true
http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
http.sslbackend=openssl
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
credential.helper=manager
gui.recentrepo=C:/wamp64/www/juillet
user.email=thomas76milton@gmail.com
user.name=Thomas Maestas
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
remote.origin.url=https://github.com/thomasm1/dailytech.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
#######################  VISUAL STUDIO  GIT REMOTE INTEGRATION ###########
1.  In Visual studio 2017 – download/install GitExtensions.
2.  From the VS menu, select Tools/’Extensions and Updates’, and from the menu install from the ‘online’ option the GitExtensions:
3.  You will need to exit VS so that the GitExtension can be installed.
4.  To verify GitExt is installed, you should see "GITEXT" in  the menu item:
5.  In Visual studio 2017 – download/install GitFlow. 
6.  From the VS menu, select Tools/’Extensions and Updates’, and from the menu install from the ‘online’ option the GitFlow:
7.  You will need to exit VS so that the GitFlow can be installed. 
To verify GitFlow extension is installed, you should see in the ‘Team Explorer’:
8.  The first time this is displayed there will only be an ‘Initialize’ option which you will need to select.  This sets up the initial default branching labels.
9.  Clone the remote repository - ssh://proddigit.us.syncsort.com/git/datafunnel-ui.git
If your windows logged in user is not your Syncsort domain user. Then you need to add your Syncsort domain user name in the URI. ssh://<user name>@proddigit.us.syncsort.com/git/trillium-discovery.git
e.g. ssh://proddigit.us.syncsort.com/git/datafunnel-ui.git 
In Repository settings, add the following Remotes:
10. In Branches display, you should see something like: (develop in bold indicates that is the current branch dev studio is set to work with)
11. For the thirdparty libs--> 
From https://jfrog.com/getcli/ download the windows 64-bit of jfrog.exe
mkdir <Path_to_Repo>\git\trillium-quality\thirdparty
Deploy the artifacts by copying from windows explorer using:
XXX
http://devblda2k8-vm.us.syncsort.com:8081/artifactory/ext-release-local/Trillium-Quality 
Copy the Win64 and Linux64 to your repo thirdparty directory
XXX
############## END GIT #########################################

###########################################################################################################################################################
##################################################################
DOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOSDOS
DOSDOSDOSDOSDOSDOSDOSDOSDOS
###########################################################################################################################################################
################################################################## 
netstat -a -o -n  | findstr 0.0:3000
TASKKILL /PID 820 /PID xxx /F  

 dir > filename.txt  === make file called filename.txt
  
	x /? 	=== provides syntax info and complete list of all parameters for x (a command, like “cd”) 
	cd\ 	=== move to the root of current drive
	cd x 	=== move to the current\x directory
	cd z:	 === change to the z root directory (as opposed to c:)
	copy x y 	=== copy file x to directory y (Ex: D:\games\galaga.exe C:\programs[\awesome.exe]), [] === optional
	copy file con 	=== display file contents in console
	copy con file.txt 	=== create text file in the console window, end with ctrl+z (^z or F6)
	date 	=== change the date
	del 	=== delete/erase
	del x 	=== deletes all files/folders fitting x
	del . 	=== deletes all files within current directory
	del *.* 	=== deletes all files within current directory
	dir 	=== display contents of current directory (Ex: dir [c:][\programs]), []	 === optional
	dir *.txt	 === list all .txt files in current directory
	dir *.? 	=== list all files with extensions one character in length in current directory
	dir /w /p *.* 	=== display all contents one screen at a time
	dir | more	 === display all contents one line at a time
	dir /? 	=== provides syntax info and complete list of all dir parameters
	echo	 === send command line input to display (by default)
	echo sometext » somefile.txt 	=== append line(s) of text to any file
	echo sometext > somefile.txt	 === overwrites file with sometext
	erase 	=== delete/erase
	exit	 === exit the command prompt
	filename.txt 	=== opens filename.txt in current directory in Notepad (or default .txt program)
	format z:	 === format z drive [Ex: use to format a disc or flash drive]
	mkdir x 	=== make directory x in current directory
	move x y 	=== move or rename x to y
	q 	=== escapes sequential display of contents (i.e. the more parameter)
	rd x 	=== remove/delete directory x if it’s empty
	ren x y 	=== rename file x to y
	time 	=== change the time
	type file 	 === display the contents of the file ‘file’ (displays file contents in console)
	type file |more  === display the contents one line at a time
Command Prompt Commands
	ipconfig [/all] 	=== display network adapter information (advanced)
	netstat –n 	 === display local address and addresses you are connected to (advanced)
	netstat –nb	  === above with name of foreign addresses (advanced) (this shows your private IP, if you are behind a router or proxy, then your public IP address will be different)
Convert output of one process into the input of another process
Send contents of script.js to the system debug.exe file:
	type script.js | c:\programs]debug.exe
	programs\debug.exe < script.js
Send directory listing to a printer or file
	dir > prn (theoretically to a printer)
	dir > somefile.txt
	dir *.mp3 > c:\Users\Dan\Desktop\musiclist.txt  === print all .mp3 files in current directory to musiclist.txt
Customize the DOS command prompt
	prompt /?  === display prompt options
	prompt $p$g  === display current directory followed by a greater-than symbol (Windows default)
	prompt $p$g$t  === display time after the default prompt
	prompt [%computername%][%username%] $g  === display computer name followed by username
	prompt  === reset prompt to default
	color 0a  === change prompt color to matrix green and screen color to black
	color 84  === change colors to red on grey
	0  === black
	1  === blue
	2  === green
	3  === cyan
	4  === red
	5  === magenta
	6  === yellow
	7  === white
	8  === grey
	9  === bright blue
	a  === bright green
	b  === bright cyan
	c  === bright red
	d  === bright magenta
	e  === bright yellow
	f  === bright white
Modify any file extension associations
	[assoc .extension=fileType]
	assoc /?  === prints this information
	assoc  === display list of current file extensions recognized by your computer (any fileType value may be used)
	assoc > fileextensions.txt  === print list to somefile.txt in current directory
	assoc .txt  === displays current file association of .txt (.docx, .html, .zip, .htaccess, assoc textfile, et cetera)
	assoc .txt =  === will delete the association for the given file extension
File Extension Tips/Ideas:
	- Windows by default doesn’t know the following extensions, but check anyways with “assoc .”, “assoc .htaccess” and “assoc .xml” anyways just to be sure. If the extension is defined already, then you may not need to change it.
	assoc .=txtfile  === associate extensionless files with Notepad
	assoc .htaccess=txtfile  === associate nameless .htaccess files with Notepad
	assoc .xml=txtfile  === associate XML files with Notepad
Miscellaneous
	Acceptable characters: A-Z a-z 0-9 $ # & @ ! ( ) – { } ‘ ` _ ~
	Unacceptable characters: | < > \ ^ + = ? / [ ] ” ; , * : %
	?  === wildcard for any single character
	*  === wildcard for any/all characters/files
	>  === redirects output to (overwrite) a file or device
	»  === redirects output to (append to) a file or device
	<  === directs data from a file or device to a program or device
	«  === directs additional data from a file or device to a program or device
	nul  === black hole
Environmental Variables via the DOS command prompt
	System-generated upon Windows startup:
	%DATE%  === Tue 08/02/2011
	%TIME%  === 14:23:33.37
	%SYSTEMROOT%  === C:\Windows
	%COMPUTERNAME%  === DAN-PC
	System-generated upon user login:
	%USERNAME%  === Dan
	%USERDOMAIN%  === Dan-PC
	Local machine variables for all users:
	%PATH%  === C:\Windows\system32
	%HOMEPATH%  === \Users\Dan
	%HOMEDRIVE%  === C:
	(Hint: Use echo)
Function Keys
	F1  === Sequential, individual repeat of previously entered characters
	F2  === Copies any number of characters from the previous command line
	F3  === Repeats the contents of the previous command line
	F4  === Deletes any number of characters from the previous command line
	F5  === Return to the previous command line
	F6  === Enters the characters ^z (CTRL+z), indicating “end of file”
	F7  === Displays a history of command-line entries for the current session (50-line cache)
	F8  === Sequentially displays previous command-line entries
	F9  === Enables user to recall previous command lines by number (0  === first line)


##  CONTINUE 		DOS  ###################
######################################################

###### USE POWERSHELL ###################
netstat -o -n -a 
TASKKILL /PID 13536 /PID 15508 /F  

ipconfig/all
systeminfo
tree
tasklist
driverquery 
 
ipconfig
“ipconfig /release” followed by “ipconfig /renew” = force search of new IP address
ipconfig /flushdns = refresh dns
netstat -an
ping + IP address or web domain
pathping  about route  test packets  
tracert  also tracks time
powercfg energy use
powercfg/hibernate on
powercfg/a  (lists states available) 

### Encrypt: from folder type,
cipher - wipe free space 
Cipher /E

### change color in CMD:
help color
color 02

help prompt
prompt tmaestas@dailytech$G 
title Death Star Console

### Wifi hotspot
netsh wlan set hostednetwork mode=allow ssid=HotspotName key=Password
netsh wlan start hostednetwork
netsh wlan stop hostednetwork

### to-hide folder:
Attrib +h +s +r name_of_folder
un-hide:
Attrib -h -s -r name_of_folder

### copy output of any command into ..
ipconfig | clip (onto clipboard, next paste!)

### List all programs on computer:
wmic product get name

### To uninstall: 
wmic product where “name like iTunes” call uninstall /noInteractive

### GO TO EXPLORER, THEN TYPE CMD 
list all previously used commands in session
While in CMD, type F7 

##  END DOS  
######################################################
### 	
	

###########################################################################################################################################################
##################################################################   BASH SHELL    BASH SHELL     BASH SHELL     BASH SHELL     BASH SHELL  
###########################################################################################################################################################
##################################################################

sudo apt-get update && sudo apt-get dist-upgrade
 
## Linux NODE INSTALL #####################
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install npm
sudo npm install -g yarn
sudo yarn add npm
npm install @babel/preset-env


cat [OPTION] [FILE]...
# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
narad:x:500:500::/home/narad:/bin/bash
# cat test test1
Hello everybody
Hi world,
We will create a file called test2 file with below command. 
# cat >test2
# cat test2
hello everyone, how do you do?
# cat song.txt | more
# cat song.txt | less
# cat -n song.txt
1  "Heal The World"
2  There's A Place In
3  Your Heart
# cat -e test
hello everyone, how do you do?$
$
# cat -T test
hello ^Ieveryone, how do you do?
# cat test; cat test1; cat test2
This is test file
This is test1 file.
This is test2 file.
# cat test >> test1 (APPEND)
# cat test > test1 (OVERWRITE)
# cat < test2
This is test2 file. write console
# cat test test1 test2 test3 | sort > test4 (SORT)
 

/////////BY TOPIC
File
    ls -F === list all items in current directory and show directories with a slash and executables with a star
    ln -s file link   === create symbolic link to file 
    tail -f file   === output the contents of file as it grows, starting with the last 10 lines
    alias name 'command'   === create an alias for a command
System  
    du   === show directory space usage
     free   === show memory and swap usage
    whereis app   === show possible locations of app
     which app   === show which app will be run by default
Process Management
    ps   === display your currently active processes
    top   === display all running processes
    kill pid   === kill process id pid
    kill -9 pid   === force kill process id pid
Permissions
    7   === full permissions
    6   === read and write only
    5   === read and execute only
    4   === read only
    3   === write and execute only
    2   === write only
    1   === execute only
    0   === no permissions
    chmod 600 file   === you can read and write - good for files
    chmod 700 file   === you can read, write, and execute - good for scripts
    chmod 644 file   === you can read and write, and everyone else can only read - good for web pages
    chmod 755 file   === you can read, write, and execute, and everyone else can read and execute - good for programs that you want to share
Networking
    wget file   === download a file 
    curl file   === download a file
    scp user@host:file dir   === secure copy a file from remote server to the dir directory on your machine
    scp file user@host:dir   === secure copy a file from your machine to the dir directory on a remote server
    scp -r user@host:dir dir   === secure copy the directory dir from remote server to the directory dir on your machine
    ssh user@host   === connect to host as user
    ssh -p port user@host   === connect to host on port as user
    ssh-copy-id user@host   === add your key to host for user to enable a keyed or passwordless login
    ping host   === ping host and output results
    whois domain   === get information for domain
    dig domain   === get DNS information for domain
    dig -x host   === reverse lookup host
    lsof -i tcp:1337   === list all processes running on port 1337
Searching
    grep pattern files   === search for pattern in files
    grep -r pattern dir   === search recursively for pattern in dir
    grep -rn pattern dir   === search recursively for pattern in dir and show the line number found
    grep -r pattern dir --include='*.ext   === search recursively for pattern in dir and only search in files with .ext extension
    command | grep pattern   === search for pattern in the output of command
    find file   === find all instances of file in real system
    locate file   === find all instances of file using indexed database built from the updatedb command. Much faster than find
    sed -i 's/day/night/g' file   === find all occurrences of day in a file and replace them with night - s means substitude and g means global - sed also supports regular expressions
Compression
    tar cf file.tar files   === create a tar named file.tar containing files
    tar xf file.tar   === extract the files from file.tar
    tar czf file.tar.gz files   === create a tar with Gzip compression
    tar xzf file.tar.gz   === extract a tar using Gzip
    gzip file   === compresses file and renames it to file.gz
    gzip -d file.gz   === decompresses file.gz back to file
Shortcuts
    ctrl+a   === move cursor to beginning of line
    ctrl+f   === move cursor to end of line
    alt+f   === move cursor forward 1 word
    alt+b   === move cursor backward 1 word
#################################################
#########Basic Shell Commands ###################
#################################################
This document was generated using the LaTeX2HTML translator Version 2008 (1.71)
The command line arguments were: 
latex2html -split 0 -font_size 10pt -no_navigation commands_basic.tex
######################
acroread - Read or print a PDF file.
########
cat - Send a file to the screen in one go. Useful for piping to other pnrograms
cat file1                       # list file1 to screen
cat file1 file2 file3 > outfile # add files together into outfile
cat *.txt > outfile             # add all .txt files together
cat file1 file2 | grep fred     # pipe files
########
cc - Compile a C program
cc test1.c                     # compile test1.c to a.out
cc -O2 -o test2.prog test2.c   # compile test2.c to test2.prog
########
cd - Change current directory
cd                     # go to home directory
cd ~/papers            # go to /home/user/papers
cd ~fred               # go to /home/fred
cd dir                 # go to directory (relative)
cd /dir1/dir2/dir3...  # go to directory (absolute)
cd -                   # go to last directory you were in
########
cp - Copy file(s)
cp file1 file2                      # copy file1 to file2
cp file1 directory                  # copy file1 into directory
cp file1 file2 file3 ... directory  # copy files into directory
cp -R dir1 dir2/  # copy dir1 into dir2 including subdirectries
cp -pR dir1 dir2/ # copy directory, preserving permissions
########
date - Shows current date
> date
Sat Aug 31 17:18:53 BST 2002
########
dvips - Convert a dvi file to PostScript
dvips document.dvi        # convert document.dvi to document.ps
dvips -Ppdf document.dvi  # convert to ps, for conversion to pdf
########
emacs - The ubiquitous text editor
emacs foo.txt             # open file in emacs
emacsclient foo.txt       # open file in existing emacs (need to use
                          # M-x start server first)						  

########
file - Tells you what sort of file it is
> file temp_70.jpg 
temp_70.jpg: JPEG image data, JFIF standard 1.01,
resolution (DPI), 72 x 72
########
firefox - Start Mozilla Firefox
f77/f90 - Compile a Fortran 77/99 program
f77 -O2 -o testprog testprog.f
gedit - Gnome text editor
gnuplot - A plotting package.
########
grep - Look for text in files. List out lines containing text (with filename if more than one file examined).
grep "hi there" file1 file2 ... # look for 'hi there' in files
grep -i "hi there" filename     # ignore capitals in search
cat filename | grep "hi there"  # use pipe
grep -v "foo" filename          # list lines that do not include foo
########
gtar - GNU version of the tar utility (also called tar on Linux). Store directories and files together into a single archive file. Use the normal tar program to backup files to a tape. See info tar for documentation.
gtar cf out.tar dir1    # put contents of directory into out.tar
gtar czf out.tar.gz dir1 # write compressed tar, out.tar.gz
gtar tf in.tar          # list contents of in.tar
gtar tzf in.tar.gz      # list contents of compressed in.tar.gz
gtar xf in.tar          # extract contents of in.tar here
gtar xzf in.tar.gz      # extract compressed in.tar.gz
gtar xf in.tar file.txt ... # extract file.txt from in.tar
########
gv - View a Postscript document with Ghostscript.
########
gzip / gunzip - GNU Compress files into a smaller space, or decompress .Z or .gz files.
gzip file.fits          # compresses file.fits into file.fits.gz
gunzip file.fits.gz     # recovers original file.fits
gzip *.dat              # compresses all .dat files into .dat.gz
gunzip *.dat.gz         # decompresses all .dat.gz files into .dat
########
program | gzip > out.gz # compresses program output into out.gz
program | gunzip > out  # decompresses compressed program output
########
info - A documentation system designed to replace man for GNU programs (e.g. gtar, gcc). Use cursor keys and return to go to sections. Press b to go back to previous section. A little hard to use.
info gtar               # documentation for gtar
########
kill - Kill, pause or continue a process. Can also be used for killing daemons.
> ps -u jss
...
 666  pts/1        06:06:06  badprocess 
> kill 666        # this sends a ``nice'' kill to the
                  # process. If that doesn't work do
> kill -KILL 666   # (or equivalently)
> kill -9 666     # which should really kill it!

> kill -STOP 667  # pause (stop) process 
> kill -CONT 667  # unpause process
########
latex - Convert a tex file to dvi
########
logout - Closes the current shell. Also try ``exit''.
########
lp - Sends files to a printer
lp file.ps  # sends postscript file to the default printer
lp -dlp2 file.ps           # sends file to the printer lp2
lp -c file.ps    # copies file first, so you can delete it
lpstat -p lp2         # get status and list of jobs on lp2
cancel lp2-258                  # cancel print job lp2-258 

lpr -Plp2 file.ps                    # send file.ps to lp2
lpq -Plp2                        # get list of jobs on lp2
lprm -Plp2 1234                   # delete job 1234 on lp2
########
ls - Show lists of files or information on the files
ls file     # does the file exist?
ls -l file  # show information about the file
ls *.txt    # show all files ending in .txt
ls -lt      # show information about all files in date order
ls -lrt     # above reversed in order
ls -a       # show all files including hidden files
ls dir      # show contents of directory
ls -d dir   # does the directory exist?
ls -p       # adds meaning characters to ends of filenames
ls -R       # show files also in subdirectories of directory
ls -1       # show one file per line
########
man - Get instructions for a particular Unix command or a bit of Unix. Use space to get next page and q to exit.
man man      # get help on man
man grep     # get help on grep
man -s1 sort # show documentation on sort in section 1
########
more - Show a file one screen at a time
more file                # show file one screen at a time
grep 'frog' file | more  # Do it to output of other command
########
mv - Move file(s) or rename a file
mv file1 file2                     # rename file1 to file2
mv dir1 dir2                       # rename directory dir1 to dir2
mv file1 file2 file3 ... directory # move files into directory
########
nano - very simple text editor. Warning - this program can introduce extra line breaks in your file if the screen is too narrow!
########
nice - Start a process in a nice way. Nice levels run from -19 (high priority) to 19 (low priority). Jobs with a higher priority get more CPU time. See renice for more detail. You should probably be using the grid-engine to run long jobs.
nice +19 myjob1   # run at lowest priority
nice +8 myjob2    # run at lowish priority
########
openoffice.org - a free office suite available for Linux/Unix, Windows and Mac OS X.
passwd - change your password
pine - A commonly used text-based mail client. It is now called alpine. Allows you to send and receive emails. Configuration options allow it to become quite powerful. Other alternatives for mail are mozilla mail and mutt, however I suggest you stick to alpine or thunderbird.
########
printenv - Print an environment variable in tcsh
setenv MYVARIABLE Fred
printenv MYVARIABLE
printenv # print all variables
########
ps - List processes on system
> ps -u jss          # list jss's processes
  934 pts/0    00:00:00 bash
^^^^^ ^^^^^    ^^^^^^^^ ^^^^^^^
PID   output   CPU time name
> ps -f      # list processes started here in full format
> ps -AF     # list all processes in extra full format
> ps -A -l            # list all processes in long format
> ps -A | grep tcsh   # list all tcsh processes
########
pwd - Show current working directory
> pwd
/home/jss/writing/lecture
quota - Shows you how much disk space you have left
> quota -v
...


rand=5
rand+=4
echo "$rand" 
echo "rand++ = $(( rand++ ))" 
echo "++rand = $(( ++rand ))"
echo "rand-- = $(( rand-- ))"
echo "--rand = $(( --rand ))"
num7 = 1.2
num8 = 3.4	 
########
renice - Renice a running process. Make a process interact better with other processes on the system (see top to see how it is doing). Nice levels run from -19 (high priority) to 19 (low priority). Only your own processes can be niced and they can only be niced in the positive direction (unless you are root). Normal processes start at nice 0.
> ps -u jss | grep bigprocess      # look for bigprocess
 1234 pts/0    99:00:00 bigprocess
> renice 19 1234                   # renice PID 1234 to 19
########
rm - Delete (remove) files
rm file1     # delete a file (use -i to ask whether sure)
rm -r dir1   # delete a directory and everything in it (CARE!)
rm -rf dir1  # like above, but don't ask if we have a -i alias
rmdir - Delete a directory if it is empty (rm -r dirname is useful if it is not empty)
rmdir dirname
########
staroffice - An office suite providing word processor, spreadsheet, drawing package. See Users' Guide on how to install this. This is a commercial version of the openoffice office package - use openoffice.org on linux.
########
setenv - Set an environment variable in tcsh.
setenv MYVARIABLE Fred
########
echo Hi there $MYVARIABLE
tar - Combine files into one larger archive file, or extract files from that archive (same as gtar on Linux).
tar cvf /dev/rmt/0 ./      # backup cwd into tape
tar tvf /dev/rmt/0         # list contents of tape
tar xvf /dev/rmt/0         # extract contents of tape
########
thunderbird - Start mozilla thunderbird.
########
top - Interactively show you the ``top'' processes on a system - the ones consuming the most computing (CPU) time. Press the ``q'' key in top to exit. Press the ``k'' key to kill a particular process. Press ``r'' to renice a process.

#########################################################################
END   BASH SHELL   BASH SHELL   BASH SHELL   BASH SHELL ##################################################################################
##################################################################

#########################################################################################################################################################
#####################################################################################SHELL SCRIPTING  SHELL SCRIPTING   SHELL SCRIPTING   SHELL SCRIPTING   SHELL SCRIPTING   SHELL SCRIPTING  
###############################################################################################################################################################################################################################################################  
#!/usr/bin/env python2
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)
	
	
 #################http://www.newthinktank.com/2016/06/shell-scripting-tutorial/
I. Intro

1. A shell script contains commands that are executed as if you typed them in the terminal.

2. We'll be using Vim for this tutorial

	a. Install Vim : sudo apt-get install vim
	
	b. Vim Commands
	
		1. i : insert mode

		2. <ESC> : enter command mode
			i. w : Save / Don't Exit
			ii. wq : Save / Quit
			iii. q! : Quit / Discard Changes
			iv. w : Move to front of next word
			v. b : Move backwards to front of word
			vi. 0 : Move to start of line
			vii. $ : Move to end of line
			viii. G : Jump to last line
		
		3. Move around with arrows
		
		4. :set number : Displays line numbers
		
		5. :syntax on : Syntax Highlighting
		
		6. :set tabstop=2 : Spaces in tab
		
		7. :set autoindent : Indent new lines
		
		8. Save these in your home/~/.vimrc file
		
			a. Find out what vimrc file you are using with this command in Vim :echo $MYVIMRC

3. Hello World Script
# The #! shebang tells the system the interpreter to use for the script
#!/bin/bash
# Comment
echo 'Hello World' # Print the string to the screen

	a. To make it executable chmod 755 hello_world
	
	b. Execute with ./hello_world
	
	c. The numbers after chmod define who can do what with the file
	
	d. The numbers represent the Owner, the Group and Everyone else
	
	e. What the numbers mean
	
		1. 7 : Read, Write & Execute
		2. 6 : Read & Write
		3. 5 : Read & Execute
		4. 4 : Read Only
		5. 3 : Write & Execute
		6. 2 : Write Only
		7. 1 : Execute Only
		8. 0 : None
		
4. We define variables like this myName="Derek"

	a. The variable name starts with a letter or _ and then can also contain numbers
	
	b. The shell treats all variables as strings
	
	c. When declaring a variable you can't have whitespace on either side of the =
	
	d. 
	#!/bin/bash
	declare -r NUM1=5 # Declare a constant
	num2=4
	
	# Use arithmetic expansion for adding
	num3=$((NUM1+num2))
	num4=$((NUM1-num2))
	num5=$((NUM1*num2))
	num6=$((NUM1/num2))
	
	# Place variables in strings with $
	echo "5 + 4 = $num3"
	echo "5 - 4 = $num4"
	echo "5 * 4 = $num5"
	echo "5 / 4 = $num6"
	echo $(( 5**2 ))
	echo $(( 5%4 ))
	
	# Assignment operators allow for shorthand arithmetic 
	# +=, -=, *=, /=
	rand=5
	let rand+=4
	echo "$rand"
	
	# Shorthand increment and decrement
	echo "rand++ = $(( rand++ ))"
	echo "++rand = $(( ++rand ))"
	echo "rand-- = $(( rand-- ))"
	echo "--rand = $(( --rand ))"
	
	# Use Python to add floats
	num7=1.2
	num8=3.4
	num9=$(python -c "print $num7+$num8")
	echo $num9
	
	# You can print over multiple lines with a Here Script
	# cat prints a file or any string past to it
	cat << END
	This text
	prints on
	many lines
	END

 II. Functions
 
 	1. You can use functions to avoid the need to write duplicate code
 	
 	2. Delete all code in Vim with gg then dG
 	
 	3. #!/bin/bash
 	# Define function
 	getDate() {
 		
 		# Get current date and time
 		date
 		
 		# Return returns an exit status number between 0 - 255
 		return
 	}
 	
 	getDate
 	
 	# This is a global variable
 	name="Derek"
 	
 	# Local variable values aren't available outside of the function
 	demLocal() {
 		local name="Paul"
 		return
 	}
 	
 	demLocal
 	
 	echo "$name"
 	
 	# A function that receives 2 values and prints a sum
 	getSum() {
 	
 		# Attributes are retrieved by referring to $1, $2, etc.
 		local num3=$1
 		local num4=$2
 		
 		# Sum values
 		local sum=$((num3+num4))
 		
 		# Pass values back with echo
 		echo $sum
 	}
 	
 	num1=5
 	num2=6
 	
 	# You pass atributes by separating them with a space
 	# Surround function call with $() to get the return value
 	sum=$(getSum num1 num2)
 	echo "The sum is $sum"
 	
III. Conditionals / Input 

	1. 
	#!/bin/bash
	
	# You can use read to receive input which is stored in name
	# The p option says that we want to prompt with a string
  	read -p "What is your name? " name
  	echo "Hello $name"
  
  	read -p "How old are you? " age
  	 
  	# You place your condition with in []
  	# Include a space after [ and before ]
  	# Integer Comparisons: eq, ne, le, lt, ge, gt
  	if [ $age -ge 16 ]
  	then
  		echo "You can drive"
  	
  	# Check another condition
  	elif [ $age -eq 15 ]
  	then
  		echo "You can drive next year"
  		
  	# Executed by default
 	else
 	  echo "You can't drive"
 	  
 	# Closes the if statement
 	fi
 	
 	2. Extended integer test
 	#!/bin/bash
 	
 	read -p "Enter a number : " num
 	
 	if ((num == 10)); then
 		echo "Your number equals 10"
 	fi
 	
 	if ((num > 10)); then
 		echo "It is greater then 10"
 	else
 		echo "It is less then 10"
 	fi
 	
 	if (( ((num % 2)) == 0 )); then
 		echo " It is even"
 	fi
 	
 	# You can use logical operators like &&, || and !
 	if (( ((num > 0)) && ((num < 11)) )); then
 		echo "$num is between 1 and 10"
 	fi
 	
 	# && and || can be used as control structures
 	
 	# Create a file and then if that worked open it in Vim
 	touch samp_file && vim samp_file
 	
 	# If samp_dir doesn't exist make it
 	[ -d samp_dir ] || mkdir samp_dir
 	
 	# Delete file rm samp_file
 	# Delete directory rmdir samp_dir

	3. Testing strings
	#!/bin/bash
	str1=""
	str2="Sad"
	str3="Happy"
	
	# Test if a string is null
	if [ "$str1" ]; then
		echo "$str1 is not null"
	fi
	
	if [ -z "$str1" ]; then
		echo "str1 has no value"
	fi
	
	# Check for equality
	if [ "$str2" == "$str3" ]; then
		echo "$str2 equals $str3"
	elif [ "$str2" != "$str3" ]; then
		echo "$str2 is not equal to $str3"
	fi
	
	if [ "$str2" > "$str3" ]; then
		echo "$str2 is greater then $str3"
	elif [ "$str2" < "$str3" ]; then
		echo "$str2 is less then $str3"
	fi
	
	# Check the file test_file1 and test_file2
	file1="./test_file1"
	file2="./test_file2"
	
	if [ -e "$file1" ]; then
		echo "$file1 exists"
		
		if [ -f "$file1" ]; then
			echo "$file1 is a normal file"
		fi
		
		if [ -r "$file1" ]; then
			echo "$file1 is readable"
		fi
		
		if [ -w "$file1" ]; then
			echo "$file1 is writable"
		fi
		
		if [ -x "$file1" ]; then
			echo "$file1 is executable"
		fi
		
		if [ -d "$file1" ]; then
			echo "$file1 is a directory"
		fi
		
		if [ -L "$file1" ]; then
			echo "$file1 is a symbolic link"
		fi
		
		if [ -p "$file1" ]; then
			echo "$file1 is a named pipe"
		fi
		
		if [ -S "$file1" ]; then
			echo "$file1 is a network socket"
		fi
		
		if [ -G "$file1" ]; then
			echo "$file1 is owned by the group"
		fi
		
		if [ -O "$file1" ]; then
			echo "$file1 is owned by the userid"
		fi
		
	fi
	
	4. With extended test [[ ]] you can use Regular Expressions
	#!/bin/bash
	
	read -p "Validate Date : " date
	
	pat="^[0-9]{8}$"
	
	if [[ $date =~ $pat ]]; then
		echo "$date is valid"
	else
		echo "$date is not valid"
	fi
	
	5. # Read multiple values
	#!/bin/bash
	
	read -p "Enter 2 Numbers to Sum : " num1 num2
	
	sum=$((num1+num2))
	
	echo "$num1 + $num2 = $sum"
	
	# Hide the input with the s code
	read -sp "Enter the Secret Code" secret
	
	if [ "$secret" == "password" ]; then
		echo "Enter"
	else
		echo "Wrong Password"
	fi
	
	6. You can set what separates the values with IFS
	#!/bin/bash
	
	# Store the original value of IFS
	OIFS="$IFS"
	
	# Set what separates the input values
	IFS=","
	
	read -p "Enter 2 numbers to add separated by a comma" num1 num2
	
	# Use the parameter expansion ${} to substitute any whitespace
	# with nothing
	num1=${num1//[[:blank:]]/}
	num2=${num2//[[:blank:]]/}

	sum=$((num1+num2))
	
	echo "$num1 + $num2 = $sum"
	
	# Reset IFS to the original value
	IFS="$OIFS"
	
	# Parameter expansion allows you to do this
	name="Derek"
	echo "${name}'s Toy"
	
	# The search and replace allows this
	samp_string="The dog climbed the tree"
	echo "${samp_string//dog/cat}"
	
	# You can assign a default value if it doesn't exist
	echo "I am ${name:-Derek}"
	
	# This uses the default if it doesn't exist and assigns the value
	# to the variable
	echo "I am ${name:=Derek}"
	echo $name
	
	7. Use case to when it makes more sense then if
	#!/bin/bash
	
	read -p "How old are you : " age
	
	# Check the value of age
	case $age in
	
	# Match numbers 0 - 4
	[0-4]) 
		echo "To young for school"
		;; # Stop checking further
		
	# Match only 5
	5)
		echo "Go to kindergarten"
		;;
		
	# Check 6 - 18
	[6-9]|1[0-8])
		grade=$((age-5))
		echo "Go to grade $grade"
		;;
		
	# Default action
	*)
		echo "You are to old for school"
		;;
	esac # End case
	
	8. Ternary Operator performs different actions based on a condition
	#!/bin/bash
	can_vote=0
	age=18
	
	((age>=18?(can_vote=1):(can_vote=0)))
	echo "Can Vote : $can_vote"
	
	
IV. Parameter Expansions and Strings

	1. Strings
	#!/bin/bash
	
	rand_str="A random string"
	
	# Get string length
	echo "String Length : ${#rand_str}"
	
	# Get string slice starting at index (0 index)
	echo "${rand_str:2}"
	
	# Get string with starting and ending index
	echo "${rand_str:2:7}"
	
	# Return whats left after A
	echo "${rand_str#*A }"

V. Looping

	1. While Loop
	#!/bin/bash
	
	num=1
	
	while [ $num -le 10 ]; do
		echo $num
		num=$((num + 1))
	done
	
	2. Continue and Break
	#!/bin/bash
	
	num=1
	
	while [ $num -le 20 ]; do
	
		# Don't print evens
		if (( ((num % 2)) == 0 )); then
 			num=$((num + 1))
 			continue
 		fi
 		
 		# Jump out of the loop with break
 		if ((num >= 15)); then
 			break
 		fi
 		
		echo $num
		num=$((num + 1))
	done
	
	3. Until loops until the loop is true
	#!/bin/bash
	
	num=1
	
	until [ $num -gt 10 ]; do
		echo $num
		num=$((num + 1))
	done
	
	4. Use read and a loop to output file info
	#!/bin/bash
  	while read avg rbis hrs; do
  	
  		# printf allows you to use \n
  		printf "Avg: ${avg}\nRBIs: ${rbis}\nHRs: ${hrs}\n"
  		
  	# Pipe data into the while loop
  	done < barry_bonds.txt
  	
  	5. There are many for loop options. Here is the C form.
  	#!/bin/bash
  	for (( i=0; i <= 10; i=i+1 )); do
  		echo $i
  	done
  	
  	6. We can cycle through ranges
  	#!/bin/bash
  	for i in {A..Z}; do
  		echo $i
  	done
  	
  	7.
  	
VI. Arrays

	1. Bash arrays can only have one dimension and indexes start at 0
	
	2. Messing with arrays
	#!/bin/bash
	
	# Create an array
	fav_nums=(3.14 2.718 .57721 4.6692)
	
	echo "Pi : ${fav_nums[0]}"
	
	# Add value to array
	fav_nums[4]=1.618
	
	echo "GR : ${fav_nums[4]}"
	
	# Add group of values to array
	fav_nums+=(1 7)
	
	# Output all array values
	for i in ${fav_nums[*]}; do
		echo $i;
	done
	
	# Output indexes
	for i in ${!fav_nums[@]}; do
		echo $i;
	done
	
	# Get number of items in array
	echo "Array Length : ${#fav_nums[@]}"
	
	# Get length of array element
	echo "Index 3 length : ${#fav_nums[3]}"
	
	# Sort an array
	sorted_nums=($(for i in "${fav_nums[@]}"; do
		echo $i;
	done | sort))
	
	for i in ${sorted_nums[*]}; do
		echo $i;
	done
	
	# Delete array element
	unset 'sorted_nums[1]'
	
	# Delete Array
	unset sorted_nums

	
VII. Positional Parameters

	1. Positional parameters are variables that can store data on the command line in variable names 0 - 9
	
		a. $0 always contains the path to the executed script
		
		b. You can access names past 9 by using parameter expansion like this ${10}
		
	2. Add all numbers on the command line
	#!/bin/bash
	
	# Print the first argument
	echo "1st Argument : $1"
	
	sum=0
	
	# $# tells you the number of arguments
	while [[ $# -gt 0 ]]; do
	
		# Get the first argument
		num=$1
		sum=$((sum + num))
		
		# shift moves the value of $2 into $1 until none are left
		# The value of $# decrements as well
		shift
	done
	
	echo "Sum : $sum"
