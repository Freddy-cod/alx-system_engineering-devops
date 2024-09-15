Postmortem: Outage on JobEase AI – Automated Job Application System
Issue Summary
Duration: 6 hours, from 10:00 AM to 4:00 PM GMT on 14th September 2024.
Impact: During this period, 70% of users were unable to submit job applications through the platform. Users experienced delays, error messages during submission, and overall sluggish performance of the service.
Root Cause: A memory leak in the application server caused the system to crash intermittently and handle requests slowly. This was due to a misconfigured caching layer that caused excessive memory consumption.

Timeline
10:00 AM – Issue detected by monitoring alert indicating high memory usage on the application server.
10:05 AM – First investigation begins, assuming a spike in traffic caused the high resource usage.
10:15 AM – Engineers scaled up additional servers to handle what was believed to be increased traffic.
10:30 AM – Users reported continued issues with job submissions, indicating the issue was not resolved.
11:00 AM – Escalation to the senior DevOps team as traffic scaling didn’t resolve the root cause.
11:30 AM – Further investigations into the caching layer and database queries revealed slow response times from the server.
12:00 PM – Misleading path: team assumed a database bottleneck and started optimizing queries.
1:00 PM – Investigations revealed that the root cause was a memory leak in the cache configuration.
1:30 PM – Engineers deployed a temporary fix to clear memory usage and restarted the server.
2:00 PM – Full investigation into the cache revealed a missing parameter in the caching strategy.
2:30 PM – Memory limits on the cache were adjusted and patches were applied.
3:30 PM – Systems were tested and monitored to ensure stability.
4:00 PM – The system was fully operational, and user traffic resumed to normal levels.
Root Cause and Resolution
Root Cause:
The root cause of the outage was a memory leak due to improper cache configuration. The cache, which was intended to speed up the retrieval of job listings, did not have a memory limit set. As job applications increased, the cache consumed excessive memory, leading to system slowdowns and eventual crashes.

Resolution:
After identifying that the caching layer was causing the memory leak, the immediate step taken was to clear out the cache and restart the application server. The DevOps team then applied a configuration patch to set memory limits on the cache and configured the cache to expire stale data more efficiently. This resolved the memory consumption issue, allowing the application server to handle requests normally.

Corrective and Preventative Measures
Improvements:

Implement better monitoring for memory usage in the cache and server to detect spikes early.
Review and optimize the caching strategy to ensure it scales efficiently with increasing traffic.
Improve the alert system to catch configuration issues before they impact service performance.
Tasks:

Patch Cache System: Ensure proper memory limits and expiration policies are applied to the cache configuration.
Add Memory Monitoring: Implement specific memory monitoring tools that trigger alerts before resources are exhausted.
Stress Testing: Regularly stress-test the system to ensure it can handle increased traffic without degrading performance.
Update Documentation: Ensure the cache configuration and system architecture are thoroughly documented to avoid similar issues in the future.
Database Query Optimization: Revisit database query strategies to ensure they don’t become bottlenecks during high traffic periods.
Auto-scaling Adjustment: Adjust auto-scaling strategies to trigger only when genuine traffic spikes occur, rather than as a response to internal system issues like memory leaks.
This postmortem aims to provide an understanding of the outage, root cause, and steps to prevent a recurrence. Through improved monitoring, patching, and configuration practices, we will ensure better system resilience in the future.






