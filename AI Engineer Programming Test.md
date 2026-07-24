# AI Engineer Programming Test: Agentic AI

> **Objective** — Assess the candidate's ability to design and implement a simple agentic AI system using multi-agent orchestration, incorporating **Retrieval-Augmented Generation (RAG)**.

---

## 1. Framework Options

Candidates can choose **one** of the following free and simple frameworks:

| # | Framework | Style |
|---|-----------|-------|
| 1 | **LangChain / LangGraph** | Graph-based orchestration |
| 2 | **OpenAI Agents SDK** | Lightweight agent primitives |

---

## 2. Tools & Requirements

### 2.1 Data Handling
- Standard Python libraries and a simple local file (e.g., a `.txt` file) to simulate a knowledge base.

### 2.2 LLM
- Candidates may use any LLM available in the market.
- **Alternatively**, send an email to `kanit.mekritthikrai@bangkokbank.com` to request access to the `gpt-5-mini` deployment below:

```python
endpoint        = "https://oaibblinnocandiddate01.openai.azure.com/"
model_name      = "gpt-5-mini"
deployment      = "gpt-5-mini"
subscription_key = "<contact>"
```

### 2.3 Required Skills
- Python programming
- Basic understanding of RAG
- API interaction
- Prompt design

---

## 3. Scenario

Build a system composed of **two cooperating agents**:

| Agent | Responsibility |
|-------|----------------|
| **Data Retriever** *(RAG)* | Retrieves specific information from the knowledge base. Does **not** answer questions directly — only returns relevant text snippets. |
| **Report Generator** | Receives the snippets from the Data Retriever and synthesizes them into a cohesive, non-redundant, well-formatted answer to the user's query. |

---

## 4. Task Instructions

### 4.1 Knowledge Base
Create a text file named `knowledge_base.txt` containing a few paragraphs of sample information. Examples:
- Company policies
- Product descriptions
- General facts about a topic (e.g., "cats")

### 4.2 Agent Definitions

#### 🔹 Data Retriever

- **Role / Instructions:** Expert in information retrieval. Searches `knowledge_base.txt` for *all* snippets relevant to the user's request.
- **Tool:** Implement a **custom Python function / tool** that:
  1. Reads `knowledge_base.txt`
  2. Performs a simple keyword search or basic semantic search
  3. Is registered with the agent so it can be called automatically
- **Output:** Returns raw, relevant text chunks to the Report Generator.

#### 🔹 Report Generator

- **Role / Instructions:** Expert writer and synthesizer. Uses the provided information snippets to formulate a comprehensive, high-quality answer for the end-user.
- **Tool:** *None required.*
- **Output:** The final, polished answer presented to the user.

---

## 5. Task Orchestration

- Orchestrate a **sequential workflow** in which the Data Retriever's output is passed as input to the Report Generator.
- Candidates using the **OpenAI Agents SDK** or **LangChain** should use one of the following patterns:
  - **Handoff** pattern
  - **Agent-as-tool** pattern
  - *Any other* suitable orchestration pattern

---

## 6. Execution & Evaluation

### 6.1 Execution
Run the system with a sample query, for example:

> *"What is the policy on international travel?"*

### 6.2 Submission
The candidate should submit on the GitHub repository:

1. ✅ Complete Python source code
2. ✅ `knowledge_base.txt` file
3. ✅ A screenshot of the final output for **a few different queries**

### 6.3 Evaluation Criteria

| # | Criterion | Weight Focus |
|---|-----------|--------------|
| 1 | Correct use of the chosen framework to define agents and orchestrate the workflow | Framework usage |
| 2 | Effective implementation of the RAG mechanism (the custom data retrieval tool) | RAG quality |
| 3 | Clarity and quality of the final output — non-redundant, accurate based on provided info, well-formatted | Output quality |
| 4 | Code structure, readability, and adherence to Python best practices | Engineering |

---

<div align="center">

*End of Test Specification*

</div>