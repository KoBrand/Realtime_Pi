# Realtime_Pi

With this Project I want to create a embedded linux for the Raspberry Pi 3b.
I will write a documentation along the way, and keep my curent work updated in this repository.

The motivation of this project is to stay uptodate with modern upcoming industiral programming tasks.
As the digitatlization if the world is drastically growing, my expreiance till today is that there is a lack ov basic understanding what to expect and what can realitically be realized. As software to a layman is often abstract, it is difficult to argue why surtain steps are required in order to do propper coding, whereas common nowledge would recommand to do otherwise.

In oder to stay uptoday with todays technologie, I have realized, that realtime computing is mostoften expected in modern application for exaple regarding IOT and autonomous driving. That is why I want to address some basics that need to soved first in order to realise these Tasks.

To realis IOT and/or Autonomous driving it can be observes that severl devices need to be connected. For IOT different Machines and for Autonomous driving diffent ECUs. Also as soon as the possibiliteis of what these connected devices can realise are understood, the application grow rappidlly.

Therefore simple and small computing preformances are not sufficient and Powerfull Servers need to be introduced.
To realize realtime applications however, most todays systems work on "best effort" algorthims. This means that if an encreas of requests are incomming, the process speed and Memory will be crutial to acheve realtime.

My approach to adress these problems:
* Creating a realtime Linux system wich can solve a number tasks under any surcomsatnces
1. It shall be once created with the help of the Linux from Scratch (LFS) guide to get a better understanding of how Linux works under the hub.
2. Second I want to create a Yokto project which realises the exact Linux system I have created with the Linux from skratch guide. The Goal is to keep the Linux system felible to changes and be able to migrate the project to other platforms along the way.

* Time Sensitive Networking (TSN): to make Ethernet Deterministic and to control the requests on a connected system
* Loadbalancing: Distribute tasks over different devices, in case that one divice has ciritical capacy




