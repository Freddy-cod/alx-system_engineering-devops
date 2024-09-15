
# Postmortem: JobEase AI Outage - “When Your Cache Decides to Go on Vacation”

![Outage Diagram](https://via.placeholder.com/600x300)  
*Figure: A visual representation of the cascading cache meltdown.*

---

## Issue Summary

**Duration**: 6 hours, from 10:00 AM to 4:00 PM GMT on 14th September 2024.  
**Impact**: During the outage, 70% of our users were stuck watching the “Please Wait” spinner for longer than anyone should have to. Job applications couldn’t be submitted, and users started experiencing error messages at random. Only 30% of users were spared from this nightmare.  
**Root Cause**: A memory leak in the caching system. In simple terms: the cache got lazy and ate up all the memory, leaving the application starved.

---

## Timeline  
- **10:00 AM** – Monitoring alerts start screaming about high memory usage on our server.
- **10:05 AM** – First responders assume the site is being stormed by a surge of eager job seekers.
- **10:15 AM** – More servers are added to keep up with the “load” (Spoiler: it wasn’t the load).
- **10:30 AM** – User complaints roll in about submissions going missing like socks in a washing machine.
- **11:00 AM** – The senior DevOps team is summoned (think bat signal in the sky).
- **11:30 AM** – They begin investigating slow database queries—spoiler again: not the real issue.
- **12:00 PM** – The wild goose chase continues, focusing on database optimisation.
- **1:00 PM** – Finally, the cache’s memory leak is identified as the main suspect.  
- **1:30 PM** – Cache cleared, server restarted. There was a brief sigh of relief.
- **2:00 PM** – The missing memory limits on the cache configuration were discovered.  
- **2:30 PM** – Cache patched, and limits set.
- **4:00 PM** – All systems go, and normal service resumes.

---

## Root Cause and Resolution  
### Root Cause  
The cache, usually the team player speeding things up, went rogue. It wasn’t set up with a memory limit, so it grew and grew, eventually consuming all the system resources. JobEase’s app servers couldn’t keep up and started failing to handle job applications.

### Resolution  
Once the rogue cache was identified, it was swiftly cleared, and limits were set on its memory consumption. This kept it from hogging all the resources, ensuring it could do its job without taking down the whole application. Proper cache expiration settings were also applied to avoid overgrowth in the future.

---

## Corrective and Preventative Measures  
### Improvements  
- Set up **better monitoring** for cache and memory usage. We don't want the cache getting lazy again.
- Regular stress tests to **simulate high traffic** and make sure everything behaves (no more excuses for downtime).

### TODO List  
1. **Patch Cache Configuration**: Implement proper memory limits.
2. **Add Memory Alerts**: So we know if something’s getting greedy.
3. **Stress Testing**: Ensure the app doesn’t collapse when things get tough.
4. **Update Documentation**: Make sure the next person knows what happened and how to avoid it.

---

Let’s keep our cache in check, so next time it doesn’t go on an unscheduled vacation! 🏖️

---
