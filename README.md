<div align="center">

```
 ┌─────────────────────────────────────────────────────────────┐
 │                                                             │
 │   A F T A B   B A S H I R                                   │
 │   senior .net engineer · backend · platform · kubernetes    │
 │                                                             │
 │   $ whoami                                                  │
 │   > 9 years shipping systems that other people depend on    │
 │                                                             │
 └─────────────────────────────────────────────────────────────┘
```

[![LinkedIn](https://img.shields.io/badge/linkedin-_-0A0A0A?style=flat-square&logo=linkedin&logoColor=0077B5&labelColor=0A0A0A)](https://linkedin.com/in/aftabkh4n)
[![Dev.to](https://img.shields.io/badge/dev.to-_-0A0A0A?style=flat-square&logo=devdotto&logoColor=white&labelColor=0A0A0A)](https://dev.to/aftabkh4n)
[![NuGet](https://img.shields.io/badge/nuget-_-0A0A0A?style=flat-square&logo=nuget&logoColor=004880&labelColor=0A0A0A)](https://www.nuget.org/profiles/aftabkh4n)

</div>

---

I build systems from the API down to the infrastructure. Kubernetes, Terraform, event driven pipelines, MCP servers, and CI/CD tooling that does something useful rather than something impressive.

Most of what I build ends up here as open source. Currently focused on MCP servers for AI assisted platform engineering, self healing Kubernetes automation, and event driven architecture with Kafka and Azure Service Bus.

---

## Published packages

<!-- NUGET-STATS:START -->
`total packages: —` · `total downloads: —`
<!-- NUGET-STATS:END -->

| Package | Downloads |
| --- | --- |
| `BlazorMemory` | ![](https://img.shields.io/nuget/dt/BlazorMemory?style=flat-square&label=&color=0A0A0A) |
| `IdpPlatform.GitHub` | ![](https://img.shields.io/nuget/dt/IdpPlatform.GitHub?style=flat-square&label=&color=0A0A0A) |
| `TravelAI.Core` | ![](https://img.shields.io/nuget/dt/TravelAI.Core?style=flat-square&label=&color=0A0A0A) |

Full list: [nuget.org/profiles/aftabkh4n](https://www.nuget.org/profiles/aftabkh4n)

---

## What I've built

**Platform and infrastructure**

| | | |
| --- | --- | --- |
| [**GenAI DevOps Platform**](https://github.com/aftabkh4n/genai-devops-platform) | Detects pod failures, reads the logs with an LLM, opens a PR with the fix | `.NET 10` `Kubernetes` `Claude` |
| [**IDP Platform**](https://github.com/aftabkh4n/idp-platform) | One API call provisions a repo, Dockerfile, K8s deployment, and CI pipeline | `.NET 9` `K8s` `SignalR` `Postgres` |
| [**Terraform IDP**](https://github.com/aftabkh4n/terraform-idp) | Postgres, Kubernetes, Prometheus, Grafana, and AWS EKS from one `terraform apply` | `Terraform` `EKS` `Helm` |
| [**Travel Booking Platform**](https://github.com/aftabkh4n/travel-booking-platform) | Every request goes through a YARP gateway for auth and rate limiting, with an Angular dashboard on top | `.NET 10` `YARP` `Angular` `Mongo` |

**Distributed systems**

| | | |
| --- | --- | --- |
| [**Order Pipeline**](https://github.com/aftabkh4n/order-pipeline) | Outbox pattern, `FOR UPDATE SKIP LOCKED`, backoff, dead letter path. Runs locally | `.NET 10` `Kafka` `Service Bus` |
| [**TravelAI.Core**](https://github.com/aftabkh4n/TravelAI.Core) | API answers in under 100ms, workers do the slow AI calls out of band | `.NET 10` `RabbitMQ` `OTel` |
| [**Data Platform API**](https://github.com/aftabkh4n/data-platform) | Search and analytics API. Redis took repeat queries from 500ms to under 100ms | `.NET 9` `Postgres` `Redis` |

**AI tooling**

| | | |
| --- | --- | --- |
| [**ContextOS**](https://github.com/aftabkh4n/contextos) | Persistent memory for AI coding agents. Hybrid BM25 and vector search, git aware | `.NET 10` `SQLite` `ONNX` |
| [**MCP Kubernetes Manager**](https://github.com/aftabkh4n/mcp-kubernetes-manager) | Eight tools that let an AI assistant drive a real cluster in plain language | `.NET 9` `MCP` `K8sClient` |
| [**BlazorMemory**](https://github.com/aftabkh4n/BlazorMemory) | Fact extraction, vector search, and persistent memory for Blazor and ASP.NET Core | `.NET 9` `Blazor` `OpenAI` |

---

## Stack

```
lang        C#  ·  .NET 8/9/10  ·  TypeScript  ·  SQL
web         ASP.NET Core  ·  Blazor  ·  Razor Pages  ·  Angular  ·  YARP
cloud       AWS (EKS, IAM, VPC)  ·  Azure  ·  Kubernetes  ·  Docker
iac         Terraform  ·  Helm  ·  GitHub Actions
events      Kafka  ·  RabbitMQ  ·  Azure Service Bus  ·  MassTransit
data        PostgreSQL  ·  SQL Server  ·  MongoDB  ·  Redis
o11y        OpenTelemetry  ·  Serilog  ·  Prometheus  ·  Grafana
```

---

## Writing

<!-- BLOG-POST-LIST:START -->
- [How I Built 50 Developer Tools That Run Entirely in the Browser](https://dev.to/aftabkh4n/how-i-built-50-developer-tools-that-run-entirely-in-the-browser-3a6a)
- [My tests were describing the code, not checking it](https://dev.to/aftabkh4n/my-tests-were-describing-the-code-not-checking-it-3m2p)
- [BlazorMemory 1.0 is out. Ten months, 14 packages, and what I got wrong along the way.](https://dev.to/aftabkh4n/blazormemory-10-is-out-ten-months-14-packages-and-what-i-got-wrong-along-the-way-1548)
- [BlazorMemory v0.8.0: Semantic Kernel adapter, Ollama embeddings, and memory decay](https://dev.to/aftabkh4n/blazormemory-v080-semantic-kernel-adapter-ollama-embeddings-and-memory-decay-oom)
- [Turning TravelAI.Core Into a Real Production System](https://dev.to/aftabkh4n/turning-travelaicore-into-a-real-production-system-3npm)
<!-- BLOG-POST-LIST:END -->

---

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=aftabkh4n&show_icons=true&hide_border=true&hide_title=true&theme=dark&bg_color=0A0A0A&icon_color=3498db&text_color=c9d1d9&count_private=true" height="140" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=aftabkh4n&layout=compact&hide_border=true&hide_title=true&theme=dark&bg_color=0A0A0A&text_color=c9d1d9&langs_count=6" height="140" />

</div>
