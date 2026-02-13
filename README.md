# DevAutoPilot – Autonomous Multi-Agent SRE Platform

## Overview
DevAutoPilot is a production-ready Agentic DevOps platform that autonomously detects, diagnoses, and remediates CI/CD failures using a multi-agent architecture powered by the Microsoft Agent Framework and Azure OpenAI.

The system reduces Mean Time to Resolution (MTTR) by orchestrating specialized AI agents that collaborate to perform root cause analysis, generate patch pull requests, validate deployments, and enable self-healing infrastructure on Azure.

## Architecture Highlights
* **Multi-agent orchestration** utilizing the Microsoft Agent Framework.
* **RAG-based root cause analysis** for precise error diagnosis.
* **Autonomous patch generation** integrated directly with GitHub.
* **Deployment validation** with an automated self-healing rollback loop.
* **Azure-native deployment** leveraging App Service, PostgreSQL, Azure Monitor, and Azure OpenAI.

## System Components

### Monitoring Intelligence Agent
Detects anomalies and failures in real-time by ingesting logs and metrics from Azure Monitor.

### Root Cause Analysis (RCA) Agent
Analyzes failure logs against historical data and codebases using Retrieval-Augmented Generation (RAG) to pinpoint specific errors.

### Patch Generation Agent
Synthesizes code fixes based on RCA findings and automatically submits a Pull Request to the repository.

### Reliability Guard Agent
Validates the patch in a sandboxed environment (Azure Container Apps) before allowing it to merge, ensuring no regressions.

### Postmortem & Compliance Agent
Generates detailed incident reports and updates documentation to ensure compliance and future prevention.

## Azure Services Used
* **Azure App Service:** Hosting the core platform API and dashboard.
* **Azure Database for PostgreSQL:** Persistent storage for incident history and agent logs.
* **Azure OpenAI Service:** Powering the LLM reasoning for all agents.
* **Azure Monitor:** Source of observability data for the Monitoring Agent.
* **Azure Container Apps:** Sandbox environment for validation.

## Repository Structure
*(This section will be populated as development progresses)*

## Hackathon Alignment
**Built for AI Dev Days Hackathon 2026**
* **Category:** Automate and Optimize Software Delivery – Agentic DevOps
