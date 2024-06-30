![1-distributed_web_infrastructure](https://github.com/Freddy-cod/alx-system_engineering-devops/assets/72683354/c72636f8-483c-4a4d-8f55-fcb0839ed3d0)

# Infrastructure Overview

This document describes a distributed web infrastructure designed to reduce traffic to the primary server by distributing some of the load to a replica server, aided by a load balancer.

## Infrastructure Details

### Load Balancer Distribution Algorithm
The HAProxy load balancer uses the Round Robin distribution algorithm. This algorithm works by rotating through each server behind the load balancer according to their weights, ensuring smooth and fair distribution of processing time. As a dynamic algorithm, Round Robin allows for on-the-go adjustment of server weights.

### Load-Balancer Setup
The HAProxy load balancer is configured in an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all nodes to prevent any single node from being overloaded, improving throughput and response times. In contrast, an Active-Passive setup involves having only one active node at a time, with the passive node on standby. If the active node becomes inactive, the passive node takes over.

### Primary-Replica (Master-Slave) Database Cluster
In a Primary-Replica setup, one server acts as the Primary server while another serves as its Replica. The Primary server handles both read and write requests, while the Replica server handles only read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

### Differences Between Primary and Replica Nodes
The Primary node manages all write operations for the site, while the Replica node processes read operations, reducing read traffic to the Primary node.

## Issues with This Infrastructure

### Single Points of Failure (SPOF)
This infrastructure has several Single Points of Failure. If the Primary MySQL database server goes down, the entire site cannot process changes (such as adding or removing users). Additionally, the server hosting the load balancer and the application server connected to the Primary database server are also SPOFs.

### Security Issues
The network data is not encrypted with an SSL certificate, leaving it vulnerable to interception by hackers. There is also no firewall installed on any server, making it impossible to block unauthorized IPs.

### Lack of Monitoring
There is no monitoring in place to track the status of each server, leaving the system without any means to detect and address issues promptly.

---
