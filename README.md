------------------ 企业级云原生 CI/CD 自动化交付与监控平台 ----------------------

本项目是一个基于开源生态搭建的全自动代码交付流水线，实现了从代码提交到生产环境**零停机发布**的全流程闭环，并集成了安全左移、K8s 配置验证及外部黑盒监控。

🌐 **在线体验地址**: [http://39.106.44.177:8000](http://39.106.44.177:8000)

------------------ 架构设计----------------


[ 开发者 Git Push ] 

       │
       
       ▼
       
[ GitHub Actions 云端流水线 ]


       ├── 1. Pytest 单元测试门禁 (质量左移)
       
       ├── 2. Trivy 镜像漏洞扫描 (安全左移)
       
       ├── 3. Docker Build & Push to 阿里云 ACR (镜像分发)
       
       ├── 4. SSH 远程部署 (蓝绿切换)
       
       └── 5. Kind 启动临时 K8s 集群 (资源清单测试)

[ 阿里云 1核1G 生产服务器 ]
       
       ├── Nginx 容器 (反向代理与流量平滑切换)
       
       ├── App 容器 (运行中)
       
       └── 内部 Docker Network (DNS 解析隔离)

[ Serverless 外部监控 ]

       └── GitHub Actions Cron 定时探测 -> 钉钉 Webhook 告警

-------------------- 核心亮点-----------------

 DevSecOps 安全与质量门禁：集成 pytest 拦截 Bug，集成 Trivy 扫描高危漏洞，确保只有健康且安全的镜像才能被部署。

 零停机蓝绿部署 (Zero-Downtime)：摒弃传统“先停后起”模式。通过 Docker 内部网络与 Nginx 动态 reload，实现新老容器平滑切换，用户端刷新 0 次 502 报错。

 K8s 资源清单自动化测试：引入 kind (Kubernetes in Docker)，在流水线中瞬间拉起临时 K8s 集群，验证 Deployment 与 Service 资源清单的正确性。

 Serverless 黑盒监控：利用 GitHub Actions Cron 触发器，不占用服务器任何资源，实现脱离宿主机的定时 HTTP 探活，异常时秒级触发钉钉告警。

 ChatOps 通知闭环：流水线关键节点自动向钉钉群推送 Markdown 格式的结构化播报。

 技术栈:

CI/CD: GitHub Actions, Shell Script

容器与云原生: Docker, Docker Compose, Kubernetes (Kind)

网络与代理: Nginx (反向代理/蓝绿部署)

安全与质量: Pytest, Trivy, GitHub Secrets

运维与监控: Python, GitHub Actions Cron, 钉钉 Webhook API

-----------------快速启动---------------

1. 环境依赖

Docker & Docker Compose

阿里云容器镜像服务 (ACR) 账号

2. 配置 Secrets

在 GitHub 仓库的 Settings -> Secrets and variables -> Actions 中配置以下变量：

ACR_REGISTRY: 阿里云镜像仓库地址

ACR_USERNAME / ACR_PASSWORD: 仓库认证信息

SERVER_IP / SERVER_SSH_KEY: 目标服务器 SSH 凭证

DINGTALK_WEBHOOK: 钉钉机器人 Webhook

3. 触发部署
修改任意代码并 Push 到 main 分支，GitHub Actions 将自动接管后续的构建与零停机部署。
