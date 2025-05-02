---
categories:
- Maps of Content
date: '2024-11-13'
draft: false
image: https://source.unsplash.com/random/1600x900?cachebust=89088
tags: []
title: Repositories MOC
---

# Repositories MOC

This Map of Content organizes our knowledge about the cellutions codebase, categorized by domain and purpose.

## Core Libraries & Tools

### Infrastructure Tools
- [[Rueidis Overview]] - Redis client for Go
- [[PGMQ Overview]] - PostgreSQL Message Queue implementation
- [[File Transferer]] - File transfer utility
- [[Apollo Router]] - GraphQL gateway configuration
- [[Migration Container]] - Database migration tools
- [[Schema Register]] - Schema management system

### Data Processing
- [[Flinklib Overview]] - Flink utilities and common code
- [[PG Events]] - PostgreSQL event handling
- [[Flink Connector Cassandra]] - Custom Flink connector
- [[ES Postgres Pulsar Connector]] - Data pipeline connector

### Database Clients
- [[Elasticsearch Java Client]]
- [[Cassandra Java Client]]
- [[Redis Java Client]]
- [[Flink Utils Java]]

## Platform Services

### Seenow Platform
- [[Seenow System Overview]] - Platform architecture
- [[Content Service]] - Content management
- [[Auth Service]] - Authentication and authorization
- [[Subscription Service]] - Subscription management
- [[Search Service]] - Search functionality
- [[Recommendation Service]] - Content recommendations

### Mediahub Platform
- [[Mediahub Overview]] - Platform architecture
- [[Asset Management]] - Digital asset management
- [[Post Service]] - Content posting system
- [[Auth Service]] - Authentication system

### Media Processing
- [[Transcode Service]] - Media transcoding
- [[Central Contract]] - API contracts

## DevOps & Infrastructure

### Kubernetes & ArgoCD
- [[Charts Overview]] - Helm charts
- [[ArgoCD Configuration]] - Deployment configurations
- [[Crossplane Resources]] - Infrastructure as code
- [[Cluster Components]] - Kubernetes components

### Monitoring & Observability
- [[Grafana Dashboards]] - Monitoring setup
- [[Observation Platform]] - Observability tools
- [[Client Logger API]] - Logging infrastructure

## Mobile Applications

### Apps
- [[Seenow iOS]] - iOS client application
- [[Seenow Android]] - Android client application

### SDKs
- [[Player SDK Android]] - Video player SDK
- [[Data SDK iOS]] - Data management SDK

## Key Implementation Patterns
- [[GraphQL Gateway Pattern]] - Using Apollo Router
- [[Event Sourcing Implementation]] - In content services
- [[CQRS Pattern]] - In various services
- [[Microservices Communication]] - Inter-service patterns

## Related MOCs
- [[010-Core Concepts MOC]] - Core concepts implemented in these repos
- [[020-Technologies MOC]] - Technologies used across repositories
- [[040-Projects MOC]] - Projects built using these repositories

## Documentation & Resources
- [[Architecture Decision Records]]
- [[API Documentation]]
- [[Development Guidelines]]
- [[Deployment Procedures]]
