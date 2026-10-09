# Course Roadmap

## Goal
Build skills to develop, evaluate, deploy, and maintain AI-powered software. Treat durations as planning estimates, not guarantees. Study mathematics and problem-solving in parallel with programming.

## Phase 00 — Engineering Foundation
- Computer execution: CPU, memory, processes, operating systems
- Interpreters, compilers, source code, bytecode, machine code
- Python implementations and CPython
- Python installation/version management, REPL, venv, pip
- Terminal, Git/GitHub, project layout, reproducibility
**Deliverable:** reproducible environment and documented first program.

## Phase 01 — Python Fundamentals
- Syntax, names, objects, built-in types, mutability
- Operators, conditionals, loops, comprehensions
- Strings, lists, tuples, sets, dictionaries
- Functions, arguments, return values, scope
- Modules, packages, files, JSON, CSV
- Exceptions, debugging, introductory testing
**Deliverable:** tested CLI utility with input validation and file persistence.

## Phase 02 — Intermediate Python
- OOP, composition, inheritance, polymorphism, MRO
- Dunder methods, properties, dataclasses, abstract classes
- Closures, decorators, functional patterns
- Iterables, iterators, generators, lazy evaluation
- Context managers and resource management
- Standard library: collections, itertools, functools, pathlib, logging, argparse
- Type annotations, generics, protocols, static checking
**Deliverable:** modular typed package with tests and documentation.

## Phase 03 — Advanced Python
- CPython execution and bytecode
- Object references, identity, memory management, garbage collection
- Attribute lookup, descriptors, metaclasses, introspection
- Threads, processes, synchronization, race conditions, deadlocks
- AsyncIO, coroutines, tasks, cancellation, timeouts
- Profiling, benchmarking, caching, memory analysis
**Deliverable:** measured ingestion pipeline with concurrent and asynchronous implementations.

## Phase 04 — Professional Python Engineering
- Architecture, dependency injection, packaging, configuration
- Ruff, type checking, pytest, coverage, pre-commit
- Unit, integration, contract, property-based testing
- Logging, structured errors, observability
- FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Redis
- Authentication, authorization, input validation, API security
- Docker and CI automation
**Deliverable:** tested, containerized API with database integration and CI.

## Phase 05 — Data Structures & Algorithms
- Big-O; arrays, strings, hashes, stacks, queues, linked lists
- Searching, sorting, recursion, backtracking, two pointers, sliding window
- Heaps, trees, graphs, BFS/DFS, greedy methods, dynamic programming
**Target:** 100–150 well-understood problems with complexity explanations.

## Phase 06 — Mathematics for AI
- Linear algebra: vectors, matrices, norms, products, eigenvalues, SVD
- Calculus: derivatives, gradients, chain rule, Jacobians
- Probability, distributions, Bayes' theorem, statistics and inference
- Optimization, gradient descent, regularization, numerical stability
**Deliverable:** implement linear/logistic regression and gradient descent with NumPy.

## Phase 07 — Scientific Python & Data Engineering
- NumPy, Pandas, Polars, SciPy, visualization
- Vectorization, broadcasting, cleaning, missing values, outliers
- Feature engineering, validation, ETL, Parquet, Arrow, reproducibility
**Deliverable:** reproducible data ingestion, validation, transformation, and analysis pipeline.

## Phase 08 — Machine Learning Engineering
- Supervised/unsupervised learning, regression, classification, ensembles
- Clustering, dimensionality reduction, splits, leakage, cross-validation
- Feature engineering, tuning, metrics, calibration, error analysis
- Scikit-learn pipelines, experiment tracking, serialization, serving
**Deliverable:** evaluated ML model served by a documented API.

## Phase 09 — Deep Learning & PyTorch
- Tensors, autograd, neural layers, losses, optimizers, training loops
- Regularization, DataLoaders, checkpoints, GPU training
- CNNs, recurrent architectures, attention, Transformers, mixed precision
**Deliverable:** reproducible training and inference project.

## Phase 10 — Generative AI, LLMs & Agentic AI
- Tokens, embeddings, attention, Transformers, inference
- Prompt/context engineering, structured outputs, tool calling, streaming
- RAG ingestion, chunking, vector and hybrid retrieval, reranking, evaluation
- Agent workflows, tools, state, memory, approvals, failure recovery
- Fine-tuning concepts, LoRA/QLoRA, Hugging Face
- Prompt injection, data leakage, permissions, grounding, safety evaluation
**Deliverable:** secure RAG application with retrieval and grounded-answer evaluation.

## Phase 11 — MLOps, LLMOps & Production AI
- Reproducible builds, CI/CD, containers, cloud foundations
- Experiment tracking, model/data versioning, model registry
- Serving, batching, streaming, GPU memory, inference optimization
- Logs, metrics, traces, latency, throughput, cost and quality monitoring
- Drift, incidents, rollback, tenant isolation, privacy and threat modeling
**Deliverable:** deployable AI service with automated checks, evaluation, monitoring, and rollback.

## Mastery Gate
For every chapter: explain ideas without notes; solve exercises independently; test edge cases; explain relevant trade-offs; target at least 80% on assessment; document evidence and areas to revisit.

## Career Direction
The shared foundation supports AI Application Engineering, Generative AI Engineering, ML Engineering, and AI Infrastructure/Operations. Research roles generally require additional mathematical and research depth.
