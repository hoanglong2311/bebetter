---
categories:
- Technologies
date: 2023-10-03
draft: false
image: https://source.unsplash.com/random/1600x900?cachebust=16390
series:
- Redis Deep Dive
tags:
- Redis
- Databases
- Caching
title: Redis Data Structures and Use Cases
---

## Introduction to Redis Data Structures

Redis is an in-memory data structure store that can be used as a database, cache, message broker, and more. Its power comes from the variety of data structures it provides and the operations available for each.

## String

The most basic Redis data type. Strings can be text, integers, or binary data up to 512MB.

### Use Cases
- Caching HTML fragments or API responses
- Counters and rate limiters
- Session storage

### Example Operations
```bash
# Set and get a simple key
SET user:1:name "John Doe"
GET user:1:name

# Increment a counter
SET pageviews 0
INCR pageviews
INCRBY pageviews 10
```

## Lists

Linked lists of string elements, sorted by insertion order. Good for fast addition/removal at both ends.

### Use Cases
- Task queues
- Recent activity feeds
- Inter-process communication

### Example Operations
```bash
# Add items to a list
LPUSH tasks "send-email:1"
RPUSH tasks "process-payment:2"

# Get list elements
LRANGE tasks 0 -1  # Get all items
LPOP tasks         # Remove and get the leftmost item
```

## Sets

Unordered collections of unique strings with O(1) add, remove, and check operations.

### Use Cases
- Unique visitor tracking
- Tagging systems
- Relationship graphs

### Example Operations
```bash
# Add members to a set
SADD tags:post:1 "redis" "database" "performance"

# Set operations
SMEMBERS tags:post:1           # Get all members
SISMEMBER tags:post:1 "redis"  # Check membership
SINTER tags:post:1 tags:post:2 # Intersection
```

## Sorted Sets

Similar to sets, but each element has an associated score for ordering.

### Use Cases
- Leaderboards and rankings
- Priority queues
- Time-series data with timestamps as scores

### Example Operations
```bash
# Add members with scores
ZADD leaderboard 100 "player:1"
ZADD leaderboard 200 "player:2"

# Get members by rank
ZRANGE leaderboard 0 -1 WITHSCORES
ZREVRANGE leaderboard 0 9  # Top 10 players
```

## Hashes

Maps of field-value pairs, perfect for representing objects.

### Use Cases
- User profiles
- Configuration settings
- Inventory items

### Example Operations
```bash
# Set multiple fields
HSET user:1 name "John" email "john@example.com" visits 10

# Get fields
HGET user:1 name
HGETALL user:1
HINCRBY user:1 visits 1
```

## Streams

Append-only log data structures introduced in Redis 5.0.

### Use Cases
- Event sourcing
- Message queues with consumer groups
- Activity feeds

### Example Operations
```bash
# Add entries to a stream
XADD events * sensor "temperature" value "22.5"

# Read from a stream
XREAD COUNT 2 STREAMS events 0
```

## HyperLogLog

Probabilistic data structure for estimating cardinality (count of unique elements).

### Use Cases
- Unique visitor counting at scale
- Metrics and analytics

### Example Operations
```bash
# Add elements
PFADD visitors "ip:192.168.1.1" "ip:192.168.1.2"

# Get estimated count of unique elements
PFCOUNT visitors
```

## Choosing the Right Data Structure

The choice of data structure significantly impacts application performance and code simplicity:

1. Need simple key-value storage? Use **Strings**
2. Need ordered elements with duplicates? Use **Lists**
3. Need unique elements without order? Use **Sets**
4. Need unique elements with ordering? Use **Sorted Sets**
5. Need to represent objects with fields? Use **Hashes**
6. Need time-ordered events with consumer groups? Use **Streams**
7. Need to count unique items efficiently at scale? Use **HyperLogLog**

## Performance Considerations

- Redis is single-threaded, so long-running commands can block other operations
- Be careful with high-cardinality keys (like user IDs) to avoid memory fragmentation
- Use pipelining and Lua scripts for atomic multi-operation transactions 