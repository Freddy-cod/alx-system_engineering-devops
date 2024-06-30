![3-scale_up](https://github.com/Freddy-cod/alx-system_engineering-devops/assets/72683354/4a066141-8e86-4b7b-b2e9-41a7b7e5066d)

# Infrastructure Overview

This document describes an enhanced web infrastructure where all Single Points of Failure (SPOFs) have been eliminated. Each major component (web server, application server, and database servers) is hosted on separate GNU/Linux servers. SSL protection is maintained end-to-end, and each server's network is secured with a firewall and is actively monitored.

## Infrastructure Details

### Addition of Firewalls Between Each Server
Firewalls are placed between each server to protect them from unauthorized access. This ensures that each server is individually secured, providing a higher level of security compared to protecting a single server.

### SSL Protection
SSL protection is not terminated at the load balancer, ensuring that all traffic remains encrypted from the client to the server, enhancing security by preventing data interception throughout the entire communication process.

### Monitoring
Each server is equipped with monitoring tools to track performance, measure key metrics, and alert administrators to any issues. This ensures proactive management and maintenance of server health and performance.

## Issues with This Infrastructure

### High Maintenance Costs
Hosting each major component on its own server increases maintenance costs. Additional servers mean higher initial purchase costs and increased electricity consumption, raising the overall operational expenses for the company. Funds will be needed not only for purchasing the servers but also for ongoing power and maintenance costs.

---
