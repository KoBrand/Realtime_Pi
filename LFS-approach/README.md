# Linux from Scratsh (LFS) for Raspberry PI 3b+

1. Creating a realtime Linux system which can solve a number tasks under any circumstance,
* It shall be once created with the help of the Linux from Scratch (LFS) guide to get a better understanding of how Linux works.


## Installation of the neccessary tools to do the LFS build
I was using Ubuntu mint on the Rasperry PI.
Here I needed to:

set bin/sh to Bash 
```
ln -sf bash /bin/sh
```

(To set it back to Dash (Default):
```
sudo ln -sf dash /bin/sh
```
)

And install the folowing Packages:
* bison
* gcc
* g++
* make
* textinfo

```sudo apt-get install bison gcc g++ make textinfo```

(I have already installed Pythons anaconda before. Could be that this is also required)

## General infomation in Need to keep track of when I reboot the system

1. This needs to be run on start to make things easyer:
This setst a  variable that can be called with "$LFS" and returns the path "/mnt/lfs" where the partition is mounted
```
export LFS=/mnt/lfs
```
also check `echo $LFS` to be shur everything ernt correctly.