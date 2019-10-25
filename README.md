# Udacity Full Stack Web Developer Nanodegree Project:
# Logs Analysis

This is a Logs Analysis, which is 1 of 3 projects for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).  
3 queries are performed to answer 3 questions pertaining to a news database provided:

> 1.  What are the most popular three articles of all time?
> 2.  Who are the most popular article authors of all time?
> 3.  On which days did more than 1% of requests lead to errors?

## Installation

A Linux-based virtual machine [\[VM\]](https://www.techopedia.com/definition/4805/virtual-machine-vm), which basically acts as a separate computer atop a "host" computer, is used to run a Python script which queries an SQL database to answer the above-mentioned questions. It is recommended that a Unix-style terminal be used; the regular terminal program of a Linux or Mac system will do, while for Windows, Git Bash is recommended.

### Requirements

- the regular terminal program \(for a Linux or Mac OS\)
- [Git Bash](https://git-scm.com/downloads) \(for Windows\)
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- Python version 2.7

### Virtual Machine Installation

Vagrant and VirtualBox are used to install and manage the VM. Files can be easily shared between the host computer and the VM. Be sure to use the recommended terminal based on your OS.

### VirtualBox Installation

VirtualBox is the actual software running the virtual machine & needn't be launched after installation as Vagrant will do so.  It can be downloaded [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).  Only the *platform package* is necessary.  

**Ubuntu users:** If Ubuntu 14.04 is being run, use the Ubuntu Software Center to install VirtualBox instead.  A warning has been issued of a bug of the package from the virtualbox.org site which may uninstall other necessary software.

### Vagrant Installation

Vagrant configures the VM and allows files to be shared between one's host computer and the VM.  It can be downloaded at: [www.vagrantup.com](https://www.vagrantup.com/downloads.html).  

**Windows users:** The installer might ask for network permissions to be granted or for a firewall exception to be made.  Please be sure to allow this.

Once Vagrant is successfully installed, one can run ```vagrant --version``` and see the version number in the terminal's response.

### VM Configuration

Use Github to fork and clone the repo at https://github.com/udacity/fullstack-nanodegree-vm.  

A new directory with the VM files will be installed.  `cd` into the directory on your terminal & then `cd` again into another directory called **vagrant**.

### Initializing VM

Once inside the **vagrant** directory, type in `vagrant up`. Vagrant will then download the Linux OS and install it.  This may take some time depending on one's internet connection, but when it's completed successfully, you'll see your shell prompt again.

Run `vagrant ssh` to log into the VM.

**Windows users:** You might have to enable the use of virtualization depending on your version of Windows and PC.  As this varies greatly, it is recommended to execute a web search for your particular version of Windows and PC.  

Also depending on your version of Windows and Vagrant, you might have to run `winpty vagrant ssh` instead of `vagrant ssh`.

## Download the database

The database can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). This file will have to be unzipped and then placed inside the `vagrant` subdirectory.

Load the date inside the `vagrant` directory using the command:
`psql -d news -f newsdata.sql`

## Download the Python script

The script can be forked and cloned from this Github repo:

Be sure to place it inside the same `vagrant` directory.

Run `python newsdb.py`.  You should see the above 3 questions followed by the answers to the database queries.

## Acknowledgments

* A big thank you to the Udacity team for providing the VM files & database, the training to complete this project, and the ensuing feedback.  
