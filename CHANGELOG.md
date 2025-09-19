# Changelog

## [v2.0.0] - 2024-09-19

### 🚀 Major Release - MCP Diagram Generator

#### ✨ New Features
- **MCP Architecture Model** - Complete Model Context Protocol for AWS architectures
- **Transversal Core Modules** - Reusable parser, generator, and engine
- **Multiple Use Cases** - BMC specific, Generic AWS, and Refined professional diagrams
- **Unified CLI** - Single entry point with multiple execution modes
- **Professional Diagrams** - PNG + Draw.io with AWS official icons

#### 🏗️ Architecture
- `core/` - Transversal modules (mcp_parser, diagram_generator, mcp_engine)
- `cases/` - Functional use cases (bmc_case, generic_aws_case, refined_bmc_case)
- `docs/` - MCP models and technical documentation
- `output/` - Generated diagrams (PNG + Draw.io)
- `scripts/` - Utility scripts and runners

#### 📊 Diagram Types Generated
- **Main Architecture** - Complete AWS infrastructure view
- **Microservices Detail** - ECS Fargate with auto-scaling
- **Network Architecture** - VPC, subnets, routing, Multi-AZ
- **Security Architecture** - Security layers and compliance
- **Data Flow** - Complete data processing pipeline

#### 🎯 BMC Specific Features
- **60M Products** - PostgreSQL with Redis cache
- **OCR >95% Accuracy** - Amazon Textract integration
- **10K Invoices/Hour** - High throughput processing
- **Multi-AZ Deployment** - 99.9% availability SLA
- **Auto-scaling** - 2-15 instances per service

#### 🔧 Technical Improvements
- **PNG + Draw.io Parity** - 1:1 correspondence between formats
- **MCP as Source of Truth** - Configuration-driven architecture
- **Professional Styling** - AWS official colors and icons
- **Detailed Labels** - Performance metrics and KPIs
- **Editable Diagrams** - Draw.io compatible with app.diagrams.net

#### 📋 Usage
```bash
# BMC specific case
./run.sh --case bmc

# Generic AWS case  
./run.sh --case generic

# Refined professional diagrams
./run.sh --case refined

# Custom MCP file
./run.sh --file docs/mcp-aws-model.md --name MyProject
```

#### 🎨 Generated Files
- **PNG Files** - For presentations and documentation
- **Draw.io Files** - For collaborative editing
- **10 Diagram Types** - Complete architecture coverage

#### 🧹 Repository Cleanup
- **Archived Obsolete Files** - 30+ old files moved to archive/
- **Organized Structure** - Clear separation of concerns
- **Unified Generators** - Single Draw.io per project
- **Automated Sync** - PNG to Draw.io synchronization

### 🔄 Migration from v1.0.0
- Old Mermaid diagrams → Professional PNG + Draw.io
- Manual generation → Automated MCP-driven
- Single use case → Multiple reusable cases
- Basic diagrams → Professional AWS architecture

### 📈 Performance
- **Generation Time** - <30 seconds for complete set
- **File Sizes** - Optimized PNG (200-400KB) + Draw.io (4-8KB)
- **Scalability** - Unlimited use cases and configurations

### 🎉 Ready for Production
- Complete documentation
- Professional diagrams
- Automated generation
- Extensible architecture
- GitHub releases ready

---

## [v1.0.0] - 2024-09-18

### Initial Release
- Basic Mermaid diagrams
- BMC architecture proposal
- Manual diagram generation
- Initial documentation
