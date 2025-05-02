---
categories:
- Core Concepts
date: '2025-04-03'
draft: false
image: https://images.unsplash.com/photo-1741851374721-a546dc41561a?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tags:
- Distributed Systems
title: Consistency Models
---

# Consistency Models

Consistency models are crucial in distributed systems as they define the rules for how data is read and written across the system. Understanding these models helps in designing systems that meet specific consistency requirements.

## Types of Consistency Models

### Strong Consistency
- Guarantees that once a write completes, all subsequent reads will return the latest written value.
- Suitable for systems where accuracy is critical, such as financial systems.

### Eventual Consistency
- Ensures that if no new updates are made to a given piece of data, eventually all accesses to that data will return the last updated value.
- Commonly used in systems where availability is prioritized over immediate consistency, like DNS.

### Causal Consistency
- Ensures that operations that are causally related are seen by all processes in the same order.
- Useful in collaborative applications where the order of operations matters.

### Read-Your-Writes Consistency
- Guarantees that once a process has written a value, it will always read that value or a more recent one.
- Important for user sessions where users expect to see their updates immediately.

### Session Consistency
- Provides consistency guarantees within a session, ensuring that all operations within a session see a consistent view of the data.
- Often used in web applications to maintain a consistent user experience.

### Monotonic Reads Consistency
- Guarantees that if a process has seen a particular value for a data item, it will never see an older value in subsequent reads.
- Helps in scenarios where users expect to see progressively newer data.

### Monotonic Writes Consistency
- Ensures that write operations are applied in the order they were issued.
- Critical for maintaining the order of operations in systems like version control.

## Conclusion

Choosing the right consistency model depends on the specific requirements of the system, such as the need for availability, partition tolerance, and latency. Understanding these models allows architects to design systems that balance these trade-offs effectively.