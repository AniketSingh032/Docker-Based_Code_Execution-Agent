# Docker-Based Code Execution Agent

### Overview

This project implements an intelligent **Docker-Based Code Execution Agent** using LangGraph and LangChain components for secure, isolated Python code generation, testing, and execution. The system combines advanced AI-powered code generation with containerized execution environments to deliver safe, scalable, and comprehensive programming solutions.

The agent intelligently generates Python code with comprehensive test cases, executes them in isolated Docker containers, and provides iterative debugging capabilities through real-time web search integration for enhanced problem-solving.

## Demo Video

Watch a demo:

[Demo Video](https://drive.google.com/file/d/1GoxvKiD-ahP2c_nDTha_-Cvr8qDV2BM_/view?usp=sharing)

---

### Architecture

The system uses a **multi-tool agent architecture** powered by LangGraph with the following key components:

* **Code Generation Engine:** Advanced LLM-based code generation with internal logic and test case separation
* **Docker Container Management:** Isolated execution environments for secure code testing
* **Dynamic Dependency Installation:** Automated package management within containers  
* **Real-time Search Integration:** Web search capabilities for error debugging and context enhancement
* **Iterative Debugging System:** Self-healing code execution with automatic error resolution

**Workflow Process:**
1. User submits coding request to the agent
2. Agent generates separate logic and test code blocks internally
3. Dependencies identified and installed in Docker container
4. Combined code script executed in isolated environment
5. If errors occur, agent searches for solutions and iteratively debugs
6. Returns final working code with comprehensive test coverage

### Key Features

#### Intelligent Code Generation
- **Dual-Block Architecture:** Internal separation of logic and test code for better organization
- **Comprehensive Test Coverage:** Automatic generation of normal, edge, invalid input, and stress test cases
- **Python Best Practices:** Follows PEP 8 standards with proper type hints and modular design
- **Advanced Use Cases:** Supports ML/AI, APIs, multiprocessing, async operations, and data pipelines
- **Error Handling:** Built-in try/catch mechanisms and input validation

#### Secure Container Execution
- **Isolated Environments:** User-specific Docker containers prevent cross-contamination
- **Resource Management:** Memory-limited containers (512MB) for optimal resource usage
- **Automated Cleanup:** Container lifecycle management with creation and removal utilities
- **File System Operations:** Secure file handling with temporary archives and workspace management
- **Python 3.9 Runtime:** Standardized execution environment with slim base images

#### Enhanced Debugging Capabilities
- **Real-time Web Search:** Tavily API integration for finding solutions to unknown errors
- **Context-Aware Research:** Searches for framework documentation and implementation examples
- **Iterative Problem Solving:** Automatic retry mechanisms with enhanced context
- **Error Message Analysis:** Intelligent parsing and resolution of execution failures

#### Technical Stack
- **LangGraph:** Agent workflow orchestration and tool management
- **LangChain:** AI agent framework and tool integration
- **ChatGroq:** High-performance LLM provider with deterministic outputs
- **Docker:** Containerized execution environment for secure code isolation
- **Tavily API:** Real-time web search for debugging and context enhancement
- **Python 3.9+:** Core runtime environment within containers

## Getting Started

### Prerequisites

* **Docker:** Ensure Docker is installed and running on your system
* **Python:** Requires Python version **3.9** or higher
* **API Keys:** Valid Groq API key and Tavily API key

### Installing

* Clone the repository:
```bash
git clone https://github.com/AniketSingh032/Code-Agent.git
cd docker-code-execution-agent
```

* Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

* Install required dependencies:
```bash
pip install poetry
poetry install
```

* Set up environment variables by creating a `.env` file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### Running

* **Start the LangGraph development server:**
```bash
langgraph dev
```

* **Verify Docker is Running:**
  - Before starting the application, ensure Docker is installed and running
  - Test Docker availability: `docker info`
  - The system will automatically create user-specific containers when needed

## Technical Details

### Container Management

* **Isolation:** Each user gets a dedicated Python 3.9 container
* **Resource Limits:** 512MB memory limit per container
* **Workspace:** Mounted `/tmp` directory for file operations
* **Lifecycle:** Automatic creation, execution, and cleanup processes

### Code Generation Process

1. **Request Analysis:** Parse user requirements and identify code structure
2. **Internal Generation:** Create separate logic and test blocks
3. **Dependency Resolution:** Identify and install required packages
4. **Code Combination:** Merge logic and tests into executable script
5. **Container Execution:** Run code in isolated environment
6. **Error Handling:** Debug and fix issues iteratively
7. **Result Delivery:** Return working code with explanations

### Search Integration

The system uses Tavily API for:
- **Error Resolution:** Finding solutions to unexpected errors
- **Documentation Lookup:** Accessing latest API documentation
- **Best Practices:** Discovering implementation patterns
- **Context Enhancement:** Gathering additional technical context

## Limitations

### Known Limitations

1. **Container Resource Constraints:** Limited to 512MB memory per container, which may restrict large-scale computations or memory-intensive operations.

2. **Docker Dependency:** Requires Docker installation and proper configuration, which may not be available in all environments (e.g., some cloud platforms or restricted systems).

3. **API Dependencies:** Relies on external APIs (Groq, Tavily) which may have rate limits, availability issues, or require paid subscriptions for extensive usage.

4. **Security Considerations:** While containerized, the system executes user-provided code which could potentially:
   - Consume excessive resources if not properly monitored
   - Attempt network operations that may need additional security controls
   - Generate large files that could fill available disk space

5. **Code Generation Accuracy:** The LLM-based code generation may occasionally:
   - Generate syntactically correct but logically flawed code
   - Miss edge cases in complex algorithms
   - Produce inefficient solutions for performance-critical tasks

6. **Error Recovery Limitations:** The iterative debugging process may not resolve all types of errors, particularly:
   - Environment-specific issues
   - Hardware-dependent operations
   - Complex dependency conflicts

### Future Improvements 🚀

**Enhanced features and production-ready optimizations coming in future updates!** Planned improvements include:

- **Advanced Security:** Enhanced container sandboxing and security policies
- **Performance Optimization:** Improved resource management and execution speed
- **Scalability Features:** Multi-container orchestration and load distribution
- **Enhanced Monitoring:** Comprehensive logging, metrics, and debugging tools
- **Extended Language Support:** Multi-language code execution capabilities
- **Production Deployment:** Kubernetes integration and cloud-native architecture
- **Advanced Testing:** Automated performance testing and code quality analysis
- **User Interface:** Web-based frontend for easier interaction and visualization

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests to help improve this educational project.

## License

This project is provided for educational and development purposes. Please review and modify security settings before any production use.