# Realtime_Pi

With this Project I want to create a embedded linux for the Raspberry Pi 3b and adress/solve some state of the art Topics such as Realtime linux, Time Sensitive Networking and Computational loadbalancing over ehternet.
I will write a documentation along the way, and keep my curent work updated in this repository.

The motivation of this project is to stay uptodate with modern upcoming industiral programming tasks.
As the digitatlization if the world is drastically growing, my expreiance till today is that there is a generl lag of basic understanding what is to be expected and what can be realized. As software to a layman is often abstract, it is difficult to argue why certain steps are required in order to do propper coding, whereas common nowledge would recommand to do otherwise.
Also a Peace of hardware can be shown and can be enphesised by its design. Software can never realy be seen, only tested by a user and either be aprooved or dissliked.

In oder to stay uptoday with todays technologie, I have realized, that realtime computing is mostoften expected in modern application for exaple regarding IOT and autonomous driving. That is why I want to address some basics that need to soved first in order to realise these Tasks.

To realis IOT and/or Autonomous driving it can be observes that severl devices need to be connected. For IOT different Machines and for Autonomous driving diffent ECUs. Also as soon as the possibiliteis of what these connected devices can realise are understood, the application grow rappidlly.

Therefore simple and small computing preformances are not sufficient and Powerfull Servers need to be introduced.
To realize realtime applications however, most todays systems work on "best effort" algorthims. This means that if an encreas of requests are incomming, the process speed and Memory will be crutial to acheve realtime.

However to solfe tasks on realtime my opinon is, that not only the devices need to be realtime capable but also the network kommunication prorocols. Also realitem is often missunderstood. The common understanding of the work realitme is "realy fast". However, it means that a task can bee realized (computed) under any surcomstances in a certain time fraim. Hoever the classic Ethenet network such systems usually operate on is not realtime capable. If to many tasks are requested from I device, either the latance will increase or the task will be droped and dataloss can be a consequence.
To adress this problem Loadbalancing needs to be addresses. That means that any device must be able to comupute any task, nomatter where the request ist origined from.

Summing up, To achieve realitme applications not only the devices need to be realitme capable. The hole system needs to be realtime capable and the system needs to smartly manage the requested tasks. 

My approach to adress these problems:
1. Creating a realtime Linux system wich can solve a number tasks under any surcomsatnces
* It shall be once created with the help of the Linux from Scratch (LFS) guide to get a better understanding of how Linux works under the hub.
* Second I want to create a Yokto project which realises the exact Linux system I have created with the Linux from skratch guide. The Goal is to keep the Linux system felible to changes and be able to migrate the project to other platforms along the way.

2. Time Sensitive Networking (TSN): to make Ethernet Deterministic and to control the requests on a connected system
3. Loadbalancing: Distribute tasks over different devices, in case that one divice has ciritical capacy




