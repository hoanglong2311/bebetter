---
categories:
- Core Concepts
date: 2023-10-01
draft: false
image: https://source.unsplash.com/random/1600x900?cachebust=52648
series:
- Distributed Systems Fundamentals
tags:
- Distributed Systems
- System Design
- Consistency
title: CAP Theorem in Distributed Systems
---

## What is the CAP Theorem?

The CAP theorem, formulated by Eric Brewer in 2000, states that a distributed system cannot simultaneously provide more than two out of the following three guarantees:

- **Consistency**: Every read receives the most recent write or an error
- **Availability**: Every request receives a non-error response
- **Partition tolerance**: The system continues to operate despite network partitions

## Why is it Important?

In distributed systems, network partitions are a given - they will happen. So in reality, we're choosing between consistency and availability when a partition occurs.

## CAP in Practice

### CP Systems (Consistent + Partition Tolerant)
- Examples: Apache HBase, MongoDB (with strong consistency settings)
- These systems will return an error or timeout if a partition occurs rather than returning potentially stale data

### AP Systems (Available + Partition Tolerant)
- Examples: Cassandra, Amazon DynamoDB
- These systems will return the most recent available data, which might not be the most recent write

### CA Systems (Consistent + Available)
- Traditional relational databases like PostgreSQL in a single-node configuration
- These systems aren't partition tolerant and thus aren't truly distributed systems

## Making the Right Choice

The selection between consistency and availability is application-specific:

- Banking systems typically choose consistency over availability
- Content delivery networks usually prefer availability over consistency
- Many systems use a combination approach, with different consistency levels for different operations

## Beyond CAP: PACELC

The PACELC theorem extends CAP by stating that in case of network partitioning (P), a distributed system must choose between availability (A) and consistency (C), but else (E), when the system is running normally, it can choose between latency (L) and consistency (C). 