<!-- ============================================================ -->
<!--                            HEADER                            -->
<!-- ============================================================ -->
<div align="center">

# Aftab Bashir

#### Senior .NET Engineer · Platform & Backend · Open Source Builder

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1200&color=3498DB&center=true&vCenter=true&width=600&height=45&lines=9+years+shipping+production+systems;Kubernetes+and+Terraform;MCP+servers+and+AI+tooling+for+.NET;Building+in+public" alt="Typing SVG" />

</div>

<!-- ============================================================ -->
<!--                       SOCIAL + METRICS                       -->
<!-- ============================================================ -->
<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/aftabkh4n)
[![Dev.to](https://img.shields.io/badge/Dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/aftabkh4n)
[![NuGet](https://img.shields.io/badge/NuGet-004880?style=for-the-badge&logo=nuget&logoColor=white)](https://www.nuget.org/profiles/aftabkh4n)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aftab966@gmail.com)

[![Followers](https://img.shields.io/github/followers/aftabkh4n?label=Followers&style=for-the-badge&color=3498db&logo=github)](https://github.com/aftabkh4n?tab=followers)
[![Stars](https://img.shields.io/github/stars/aftabkh4n?label=Stars&style=for-the-badge&color=f1c40f&logo=github)](https://github.com/aftabkh4n)

</div>

---

<table>
<tr>
<td width="60%" valign="top">

## 👋 Who I Am

I'm Aftab Bashir, a senior .NET engineer with nine years building production systems that other people depend on, across government, enterprise and commercial environments.

My day job is secure enterprise applications in a regulated environment. Everything else I build ends up here as open source: MCP servers for AI assisted platform engineering, internal developer platforms, event driven pipelines on Kafka and RabbitMQ, and infrastructure as code with Terraform.

I write about what I build on Dev.to, including the parts I got wrong, and publish the reusable pieces to NuGet.

</td>
<td width="40%" valign="top">

## ⚡ At a Glance

```yaml
name:        Aftab Bashir
role:        Senior .NET Engineer
focus:       Backend · Platform · K8s
experience:  9 yrs in production
based:       Doha, Qatar
stack:       C# · .NET 10 · Kubernetes
clouds:      AWS · Azure · GCP
packages:    published on NuGet
writing:     dev.to/aftabkh4n
learning:    AWS CDK · CodeBuild
```

</td>
</tr>
</table>

---

<!-- ============================================================ -->
<!--                  CURRENTLY BUILDING / LEARNING               -->
<!-- ============================================================ -->
## 🔭 Currently Building & Learning

<table>
<tr>
<td width="50%" valign="top">

### 🛠️ Building
- 🧠 ContextOS, persistent memory for AI coding agents
- 🤖 MCP servers for Kubernetes and platform tooling
- 🔁 Event driven pipelines with Kafka and Service Bus
- 📦 BlazorMemory, an AI memory layer for .NET

</td>
<td width="50%" valign="top">

### 🌱 Learning & Exploring
- ☁️ AWS CDK and CodeBuild, infrastructure as code beyond Terraform
- 🧩 MCP protocol internals and agent tooling
- 📊 OpenTelemetry tracing across distributed services
- 🔐 Azure DevOps practices (AZ-400)

</td>
</tr>
</table>

---

<!-- ============================================================ -->
<!--                     FEATURED PACKAGE                         -->
<!-- ============================================================ -->
<div align="center">

### ▸ BlazorMemory

**Give your .NET app a memory.**

[![NuGet](https://img.shields.io/nuget/v/BlazorMemory?style=for-the-badge&logo=nuget&logoColor=white&label=version&labelColor=0A0A0A&color=3498db)](https://www.nuget.org/packages/BlazorMemory)
[![Downloads](https://img.shields.io/nuget/dt/BlazorMemory?style=for-the-badge&label=downloads&labelColor=0A0A0A&color=2ecc71)](https://www.nuget.org/packages/BlazorMemory)
[![Stars](https://img.shields.io/github/stars/aftabkh4n/BlazorMemory?style=for-the-badge&label=stars&labelColor=0A0A0A&color=f1c40f)](https://github.com/aftabkh4n/BlazorMemory)

</div>

Most LLM apps forget everything the moment the session ends. BlazorMemory sits underneath your Blazor or ASP.NET Core app, pulls durable facts out of conversations, embeds them, and hands the relevant ones back the next time they matter. Ten months of work, shipped as a suite of NuGet packages.

```bash
dotnet add package BlazorMemory
```

```mermaid
flowchart LR
    C["conversation"] --> X["fact extraction"]
    X --> E["embeddings"]
    E --> V[("vector store")]
    V --> R["semantic recall"]
    R --> A["your app, with context"]
    A -.->|next session| C
```

<details>
<summary><b>Other published packages</b></summary>

<br/>

| Package | Downloads |
| --- | --- |
| `IdpPlatform.GitHub` | ![](https://img.shields.io/nuget/dt/IdpPlatform.GitHub?style=flat-square&label=&color=0A0A0A) |
| `TravelAI.Core` | ![](https://img.shields.io/nuget/dt/TravelAI.Core?style=flat-square&label=&color=0A0A0A) |

<!-- NUGET-STATS:START -->
`total packages: —` · `total downloads: —`
<!-- NUGET-STATS:END -->

Full list: [nuget.org/profiles/aftabkh4n](https://www.nuget.org/profiles/aftabkh4n)

</details>

---

<!-- ============================================================ -->
<!--                     ARCHITECTURE SHOWCASE                    -->
<!-- ============================================================ -->
## 🏗️ One API Call, a Whole Service

This is what my [IDP Platform](https://github.com/aftabkh4n/idp-platform) does when a developer asks for a new service. Everything after the request happens without anyone touching a console.

```mermaid
flowchart LR
    DEV["developer request"] --> API["IDP API"]
    API --> GH["GitHub repo"]
    API --> DOCK["Dockerfile"]
    API --> K8S["Kubernetes deploy"]
    API --> CI["CI pipeline"]
    CI --> AI["AI code review"]
    K8S --> OBS["Prometheus and Grafana"]
    API -.->|live status| DEV
```

Provisioning that used to take most of a day now takes one request and a few minutes.

---

<!-- ============================================================ -->
<!--                       FEATURED PROJECTS                      -->
<!-- ============================================================ -->
## 📌 Featured Projects

<div align="center">

[![ContextOS](https://github-readme-stats.vercel.app/api/pin/?username=aftabkh4n&repo=contextos&theme=react&hide_border=true&bg_color=0D1117&icon_color=3498db&title_color=58A6FF)](https://github.com/aftabkh4n/contextos)
[![BlazorMemory](https://github-readme-stats.vercel.app/api/pin/?username=aftabkh4n&repo=BlazorMemory&theme=react&hide_border=true&bg_color=0D1117&icon_color=3498db&title_color=58A6FF)](https://github.com/aftabkh4n/BlazorMemory)
[![IDP Platform](https://github-readme-stats.vercel.app/api/pin/?username=aftabkh4n&repo=idp-platform&theme=react&hide_border=true&bg_color=0D1117&icon_color=3498db&title_color=58A6FF)](https://github.com/aftabkh4n/idp-platform)
[![MCP Kubernetes Manager](https://github-readme-stats.vercel.app/api/pin/?username=aftabkh4n&repo=mcp-kubernetes-manager&theme=react&hide_border=true&bg_color=0D1117&icon_color=3498db&title_color=58A6FF)](https://github.com/aftabkh4n/mcp-kubernetes-manager)
[![Order Pipeline](https://github-readme-stats.vercel.app/api/pin/?username=aftabkh4n&repo=order-pipeline&theme=react&hide_border=true&bg_color=0D1117&icon_color=3498db&title_color=58A6FF)](https://github.com/aftabkh4n/order-pipeline)
[![Terraform IDP](https://github-readme-stats.vercel.app/api/pin/?username=aftabkh4n&repo=terraform-idp&theme=react&hide_border=true&bg_color=0D1117&icon_color=3498db&title_color=58A6FF)](https://github.com/aftabkh4n/terraform-idp)

</div>

<details>
<summary><b>Everything else I've built</b></summary>

<br/>

**Platform and infrastructure**

| | | |
| --- | --- | --- |
| [**GenAI DevOps Platform**](https://github.com/aftabkh4n/genai-devops-platform) | Detects pod failures, reads the logs with an LLM, opens a PR with the fix | `.NET 10` `Kubernetes` `Claude` |
| [**Travel Booking Platform**](https://github.com/aftabkh4n/travel-booking-platform) | Every request goes through a YARP gateway for auth and rate limiting, with an Angular dashboard on top | `.NET 10` `YARP` `Angular` `Mongo` |

**Distributed systems**

| | | |
| --- | --- | --- |
| [**TravelAI.Core**](https://github.com/aftabkh4n/TravelAI.Core) | API answers in under 100ms, workers do the slow AI calls out of band | `.NET 10` `RabbitMQ` `OTel` |
| [**Data Platform API**](https://github.com/aftabkh4n/data-platform) | Search and analytics API. Redis took repeat queries from 500ms to under 100ms | `.NET 9` `Postgres` `Redis` |

</details>

---

<!-- ============================================================ -->
<!--                          TECH STACK                          -->
<!-- ============================================================ -->
## 🧰 Tech Stack

<div align="center">
  <img src="https://techstack-generator.vercel.app/csharp-icon.svg" alt="csharp" width="58" height="58" />
  &nbsp;&nbsp;
  <img src="https://techstack-generator.vercel.app/kubernetes-icon.svg" alt="kubernetes" width="58" height="58" />
  &nbsp;&nbsp;
  <img src="https://techstack-generator.vercel.app/docker-icon.svg" alt="docker" width="58" height="58" />
  &nbsp;&nbsp;
  <img src="https://techstack-generator.vercel.app/aws-icon.svg" alt="aws" width="58" height="58" />
</div>

<br/>

<table align="center">
<tr>
<td align="right" width="190"><b>💻 Languages & Core</b></td>
<td>
  <img src="https://go-skill-icons.vercel.app/api/icons?i=cs&theme=dark&animate=true" width="48" height="48" alt="csharp" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=dotnet&theme=dark&animate=true" width="48" height="48" alt="dotnet" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=ts&theme=dark&animate=true" width="48" height="48" alt="typescript" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=js&theme=dark&animate=true" width="48" height="48" alt="javascript" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=php&theme=dark&animate=true" width="48" height="48" alt="php" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=git&theme=dark&animate=true" width="48" height="48" alt="git" />
</td>
</tr>
<tr>
<td align="right"><b>🌐 Web & Frameworks</b></td>
<td>
  <img src="https://go-skill-icons.vercel.app/api/icons?i=blazor&theme=dark&animate=true" width="48" height="48" alt="blazor" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=angular&theme=dark&animate=true" width="48" height="48" alt="angular" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=html&theme=dark&animate=true" width="48" height="48" alt="html" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=css&theme=dark&animate=true" width="48" height="48" alt="css" />
</td>
</tr>
<tr>
<td align="right"><b>☁️ Cloud · DevOps</b></td>
<td>
  <img src="https://go-skill-icons.vercel.app/api/icons?i=aws&theme=dark&animate=true" width="48" height="48" alt="aws" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=azure&theme=dark&animate=true" width="48" height="48" alt="azure" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=gcp&theme=dark&animate=true" width="48" height="48" alt="gcp" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=kubernetes&theme=dark&animate=true" width="48" height="48" alt="kubernetes" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=docker&theme=dark&animate=true" width="48" height="48" alt="docker" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=terraform&theme=dark&animate=true" width="48" height="48" alt="terraform" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=githubactions&theme=dark&animate=true" width="48" height="48" alt="actions" />
</td>
</tr>
<tr>
<td align="right"><b>🗄️ Data · Messaging</b></td>
<td>
  <img src="https://go-skill-icons.vercel.app/api/icons?i=postgres&theme=dark&animate=true" width="48" height="48" alt="postgres" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=mysql&theme=dark&animate=true" width="48" height="48" alt="mysql" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=mongodb&theme=dark&animate=true" width="48" height="48" alt="mongodb" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=redis&theme=dark&animate=true" width="48" height="48" alt="redis" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=kafka&theme=dark&animate=true" width="48" height="48" alt="kafka" />
  <img src="https://go-skill-icons.vercel.app/api/icons?i=rabbitmq&theme=dark&animate=true" width="48" height="48" alt="rabbitmq" />
</td>
</tr>
</table>

<div align="center">

**🔭 Observability · AI Tooling**

![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-1A1A2E?style=flat-square&logo=opentelemetry&logoColor=white)
![Serilog](https://img.shields.io/badge/Serilog-1A1A2E?style=flat-square&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-1A1A2E?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-1A1A2E?style=flat-square&logo=grafana&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-1A1A2E?style=flat-square&logoColor=white)
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-1A1A2E?style=flat-square&logo=microsoftazure&logoColor=white)
![MassTransit](https://img.shields.io/badge/MassTransit-1A1A2E?style=flat-square&logoColor=white)
![YARP](https://img.shields.io/badge/YARP-1A1A2E?style=flat-square&logoColor=white)

</div>

---

<!-- ============================================================ -->
<!--                           WRITING                            -->
<!-- ============================================================ -->
## ✍️ Writing

<!-- BLOG-POST-LIST:START -->
- [What spanner for an M12 bolt? An agent that knows DIN and ISO disagree](https://dev.to/aftabkh4n/what-spanner-for-an-m12-bolt-an-agent-that-knows-din-and-iso-disagree-32km)
- [I got tired of re-explaining my codebase to Claude every morning, so I built this](https://dev.to/aftabkh4n/i-got-tired-of-re-explaining-my-codebase-to-claude-every-morning-so-i-built-this-5eo5)
- [How I Built 50 Developer Tools That Run Entirely in the Browser](https://dev.to/aftabkh4n/how-i-built-50-developer-tools-that-run-entirely-in-the-browser-3a6a)
- [My tests were describing the code, not checking it](https://dev.to/aftabkh4n/my-tests-were-describing-the-code-not-checking-it-3m2p)
- [BlazorMemory 1.0 is out. Ten months, 14 packages, and what I got wrong along the way.](https://dev.to/aftabkh4n/blazormemory-10-is-out-ten-months-14-packages-and-what-i-got-wrong-along-the-way-1548)
<!-- BLOG-POST-LIST:END -->

---

<!-- ============================================================ -->
<!--                     CONTRIBUTION SNAKE                       -->
<!-- ============================================================ -->
### 🐍 Watch My Contributions Get Eaten

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/aftabkh4n/aftabkh4n/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/aftabkh4n/aftabkh4n/output/snake.svg" />
  <img alt="github contribution snake animation" src="https://raw.githubusercontent.com/aftabkh4n/aftabkh4n/output/snake.svg" />
</picture>

</div>

---

<!-- ============================================================ -->
<!--                           FOOTER                             -->
<!-- ============================================================ -->
<div align="center">

<sub>Based in Doha · building in public · <a href="https://github.com/aftabkh4n?tab=repositories">all repositories →</a></sub>

</div>
