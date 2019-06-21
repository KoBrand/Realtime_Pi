# Linux from Scratsh (LFS) for Raspberry PI 3b+

1. Creating a realtime Linux system which can solve a number tasks under any circumstance,
* It shall be once created with the help of the Linux from Scratch (LFS) guide to get a better understanding of how Linux works.


## Installation of the neccessary tools to do the LFS build
1. I was using Ubuntu mint on the Rasperry PI.
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

2. Create new Patrition.
Here I used the tool Gparted to devide my SD card into two seperate partitions. One contianing ubuntu mint and on the other I will create my LSF. As file system I set ext4 size was about 7 GB.
I could not do this on the running raspberry because it was required to umnount the Divice. This is not possible becuase Ubunut mint was running, so I used my laptop insted.

Then I mounted the new partition on `/mnt/lfs` as the guide requests.
I also editted `sudo nano etc/fstab` and added this line:
```
...

/dev/mmcblk0p3     /mnt/lfs        ext4   defaults          1  1

```
This way the driver will be mounted on every reboot and I dont have to do everything manually.

3. Download every pycket you need on to the Partition.
Somehow there is jetzt a list of things, not really shur why I need them what they are for and if I need every single one of then. Maybe less cann be used?

Also according to this guide: https://intestinate.com/pilfs/guide.html some other pakets and patches have to be installed.
Somehow I do not like the ide of just using somthing esle just because some one told me to. I might work deeper into this matter:
TODO: Compile "wrong / pure" LFS packeges on the pi and analyse the errrors.

4. I had to creat a new user with no inherited infroamion from the host system.

Then I needed to chostimize the Profile by 

```
cat > ~/.bash_profile << "EOF"
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
EOF
```
```
cat > ~/.bashrc << "EOF"
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnueabihf
PATH=/tools/bin:/bin:/usr/bin
export LFS LC_ALL LFS_TGT PATH
EOF
```

Be awere of the line `LFS_TGT=$(uname -m)-lfs-linux-gnueabihf` this is a change to the LFS guide because we are on the Raspberry 




## General infomation in Need to keep track of when I reboot the system

1. This needs to be run on start to make things easyer:
This setst a  variable that can be called with "$LFS" and returns the path "/mnt/lfs" where the partition is mounted
```
export LFS=/mnt/lfs
```
also check `echo $LFS` to be shur everything ernt correctly.

I created a Linux from Scratch user: lfs. I access the user with 
``` su -lfs ``` enter koni