

![Uploading 0-simple_web_stack_.PNG…]()

# Infrastructure Overview

This document outlines the basic web infrastructure for hosting a website accessible at www.foobar.com. The setup described here lacks firewalls and SSL certificates for network protection, and all components (database, application server) share the server's resources (CPU, RAM, and SSD).

## Infrastructure Details

### What is a Server?
A server is a computer system, either hardware or software, that provides services to other computers, known as clients.

### Role of the Domain Name
The domain name offers a human-readable alias for an IP address. For instance, the domain name www.wikipedia.org is more recognizable and easier to remember than its IP address, 91.198.174.192. This mapping between the IP address and the domain name is managed by the Domain Name System (DNS).

### DNS Record Type for www.foobar.com
The domain www.foobar.com uses an A record, which can be verified by running `dig www.foobar.com`. Although results may vary, this design utilizes an A record.
An Address Mapping record (A Record) or DNS host record stores a hostname and its corresponding IPv4 address.

### Role of the Web Server
A web server is a software or hardware system that accepts HTTP or HTTPS requests and responds with the requested resource's content or an error message.

### Role of the Application Server
An application server installs, operates, and hosts applications and related services for end-users, IT services, and organizations, facilitating the hosting and delivery of high-end consumer or business applications.

### Role of the Database
A database maintains a collection of organized information that can be easily accessed, managed, and updated.

### Communication Between Server and Client
Communication between the client and the server occurs over the internet using the TCP/IP protocol suite.

## Issues with This Infrastructure

### Single Points of Failure (SPOF)
This infrastructure has multiple Single Points of Failure. For example, if the MySQL database server goes down, the entire site will be inaccessible.

### Downtime During Maintenance
Maintenance operations require shutting down components or the entire server. With only one server in use, the website will experience downtime during maintenance.

### Scalability Challenges
Scaling this infrastructure is difficult due to the single server housing all components. The server can quickly run out of resources or slow down under heavy traffic loads.

---

Feel free to let me know if you need any further changes or additional sections for this README.
