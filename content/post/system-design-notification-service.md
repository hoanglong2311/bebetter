---
categories:
- Interview Prep
date: 2023-10-02
draft: false
image: https://source.unsplash.com/random/1600x900?cachebust=68422
series:
- System Design Interviews
tags:
- System Design
- Microservices
- Scalability
title: 'System Design Interview: Scaling a Notification Service'
---

## Problem Statement

Design a notification service that can send millions of notifications (push, SMS, email) to users daily with high reliability and low latency.

## Requirements Analysis

### Functional Requirements
- Support multiple notification types (push, SMS, email)
- Support templating for personalized messages
- Allow scheduling of notifications
- Support batch and single notifications
- Track delivery status

### Non-Functional Requirements
- High throughput (millions per day)
- Low latency for time-sensitive notifications
- High availability (99.9%+)
- Failover mechanisms for provider outages
- Message ordering when needed

## System Architecture

### High-Level Components

```
[Client Apps] → [API Gateway]
                    ↓
   [Notification Service API]
       ↓          ↓           ↓
[Push Service][SMS Service][Email Service]
       ↓          ↓           ↓
[Push Providers][SMS Providers][Email Providers]
```

### Key Components

1. **API Gateway**
   - Rate limiting, authentication, load balancing

2. **Notification Service API**
   - Request validation
   - Notification routing
   - Template rendering

3. **Channel-specific Services**
   - Provider selection and fallback
   - Delivery optimization
   - Channel-specific formatting

4. **Message Queue**
   - Kafka or RabbitMQ for guaranteed delivery
   - Separate queues per channel and priority

## Data Model

```
Notification {
  id: UUID
  user_id: UUID
  type: ENUM(PUSH, SMS, EMAIL)
  template_id: UUID
  template_data: JSON
  status: ENUM(QUEUED, SENT, DELIVERED, FAILED)
  created_at: Timestamp
  scheduled_for: Timestamp
  completed_at: Timestamp
}

Template {
  id: UUID
  name: String
  content: String
  variables: JSON
  channel: ENUM(PUSH, SMS, EMAIL)
}
```

## Scaling Considerations

### Horizontal Scaling
- Stateless services for easy scaling
- Sharding by user_id or region

### Rate Limiting
- Per-user rate limits
- Global rate limiting

### Idempotency
- Idempotency keys for safe retries

## Failure Handling

### Provider Outages
- Multiple provider support per channel
- Circuit breakers for failing providers
- Retry mechanisms with exponential backoff

### Message Persistence
- Store messages in durable storage before processing
- Dead letter queues for failed deliveries

## Monitoring and Alerting

- Track delivery rates, latency, error rates
- Alert on abnormal failure rates
- Monitor queue depths

## Cost Optimization

- Batch notifications where possible
- Intelligent provider selection based on cost
- Time-shifting non-urgent notifications 