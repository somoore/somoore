<p align="center">
  <img src="assets/banner.svg" alt="Scott Moore, AI security engineer" width="100%"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/YOUR_HANDLE/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:scott@moore.cloud"><img src="https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white" alt="Email"/></a>
  <img src="https://img.shields.io/badge/Austin%2C%20TX-30363d?style=flat" alt="Austin, TX"/>
</p>

## The problem I keep working on

**Agents are getting real permissions. Security tooling hasn't caught up.**
A sandbox sees a process make a network call. It can't see that the agent just read `.env`, or that an MCP tool told it to "forward these for analytics." I build the tools that add that missing context, and the audits for the data layers agents sit on.

## Projects

| | |
|---|---|
| 🛡️ [**sir**](https://github.com/somoore/sir) | **Sandbox in Reverse.** Information-flow control for AI coding agents (Claude Code, Gemini CLI, Codex). Read a secret, and the next exit is blocked, with a causal explanation and a hash-chained audit ledger. Go + Rust. |
| 🔍 [**turbopuffer security suite**](https://github.com/somoore/powerpipe-turbopuffer-security-benchmark) | Vector databases leave row-level access control to the application, and nothing audits it. A [Steampipe plugin](https://github.com/somoore/steampipe-plugin-turbopuffer), a 15-control [Powerpipe benchmark](https://github.com/somoore/powerpipe-turbopuffer-security-benchmark) covering cross-tenant retrieval, residency, CMEK and canary documents, and a [Terraform provider](https://github.com/somoore/terraform-provider-tpuf). |
| 💻 [**pairputer-on-aws**](https://github.com/somoore/pairputer-on-aws) | A disposable Linux MicroVM that you and an AI drive together, streamed into the chat. Freezes when idle and runs in your own AWS account. |
| 👾 [**hellbox**](https://github.com/somoore/hellbox) | DOOM in an AWS Lambda MicroVM, streamed to the browser with live suspend and resume. Built to make Firecracker feel real. |

## Toolbox

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Steampipe](https://img.shields.io/badge/Steampipe-1F6FEB?style=flat)

## Say hi

I like talking to people working on agent security, model-platform security, and anything that makes AI systems safer to deploy.
