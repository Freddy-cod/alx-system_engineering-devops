![2-secured_and_monitored_web_infrastructure](https://github.com/Freddy-cod/alx-system_engineering-devops/assets/72683354/5730112c-2a34-48ac-9f92-8d65ad7fedeb)


# Infrastructure Overview

This document describes a 3-server web infrastructure designed to be secure, monitored, and capable of serving encrypted traffic.

## Infrastructure Details

### Purpose of the Firewalls
Firewalls protect the network, especially the web servers, from unauthorized and unwanted access. They act as intermediaries between the internal network and the external network, blocking incoming traffic that doesn't meet specified security criteria.

### Purpose of the SSL Certificate
An SSL certificate encrypts the traffic between the web servers and the external network, preventing man-in-the-middle (MITM) attacks and network sniffing, which could expose sensitive information. SSL certificates ensure the privacy, integrity, and authenticity of the transmitted data.

### Purpose of the Monitoring Clients
Monitoring clients track the performance and operations of the servers and the external network. They analyze server health, measure key performance metrics, and alert administrators if the servers are underperforming. These tools automatically test server accessibility, measure response times, and alert for issues such as corrupt or missing files, security vulnerabilities, and other potential problems.

## Issues with This Infrastructure

### Unencrypted Traffic Between Load Balancer and Web Servers
Terminating SSL at the load balancer level means that the traffic between the load balancer and the web servers is unencrypted, which could expose sensitive information.

### Single Point of Failure with One MySQL Server
Having only one MySQL server poses a scalability issue and acts as a single point of failure for the web infrastructure.

### Resource Contention on Servers
Hosting all components on the same servers leads to resource contention (CPU, memory, I/O, etc.), which can degrade performance and complicate troubleshooting. This setup is also not easily scalable.

--
