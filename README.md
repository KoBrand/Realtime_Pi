# Real-Time_Pi

With this project I want to create an embedded Linux for the Raspberry Pi 3b and address/solve some state of the art topics such as, Real-time Computing (and its consequences), Time Sensitive Networking (TSN) and Computational Load-balancing over Ethernet.
I will write a documentation along the way, and keep my current work updated in this repository.

The motivation of this project is to stay up to date with modern industrial systems that become everly growing complex.
As the digitalization of the world is drastically growing, my experience today is, that there is a general lag of basic understanding what is to be expected and what can be realized by modern systems. As software to a layman is often abstract and it becomes difficult to argue why certain steps are required in order to do a proper system setup, whereas common knowledge would recommend to do otherwise.
Also a piece of hardware can be shown and can be emphasized by its design. Software can never really be seen, only tested by a user and either be approved or disliked.

In order to stay up to day with today's technologies, I have realized, that real-time computing is most often expected in modern application, for example regarding Internet Of Things (IOT) and autonomous driving application. However, to realize real-time applications a lot more has to be considered.
That is why I want to address some basics that need to solved first in order to realize these tasks.

To realize IOT and/or autonomous driving it can be observes that several devices need to be connected. For IOT different machines and for autonomous driving different Electronic Control Units (ECUs). Also as soon as the possibility of what these connected devices can realize are understood, the application grow rapidly.

Therefore, simple and small computing performances are not sufficient and powerful servers need to be introduced.
To realize real-time applications however, most today's systems work on "best effort" algorithms. This means that if an increase of requests are incoming, the process speed and memory will be crucial to achieve real-time.

However to solve tasks on real-time my opinion is, that not only the devices need to be real-time capable but also the network communication protocols. Also real-time is often misunderstood. The common understanding of the work real-time is "really fast". However, it means that a task can bee realized (computed) under any circumstances in a certain time frame. Moreover, the classic Ethernet network, such systems usually operate on, is not real-time capable. If too many tasks are requested from I device, either the latency will increase or the task will be dropped and data-loss can be a consequence.
To address this problem Load-balancing needs to be addresses. That means that any device must be able to compute any task, no matter where the request its originated from.

Summing up, To achieve real-time applications not only the devices need to be real-time capable. The hole system needs to be real-time capable and the system needs to smartly manage the requested tasks. 

My approach to address these problems:
1. Creating a real-time Linux system which can solve a number tasks under any circumstance
* It shall be once created with the help of the Linux from Scratch (LFS) guide to get a better understanding of how Linux works under the hub.
* Second I want to create a Yokto project which realizes the exact Linux system I have created with the Linux from scratch guide. The Goal is to keep the Linux system flexible to changes and be able to migrate the project to other platforms along the way.

2. Time Sensitive Networking (TSN): to make Ethernet Deterministic and to control the requests on a connected system
3. Load-balancing: Distribute tasks over different devices, in case that one device has critical capacity



