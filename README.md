<h1 align="center"> 🟣 LineAI</h1>
<p align="center">
  <strong>Evidence-Based Research Synthesis Engine</strong><br>
  Real-time claim verification grounded in academic metadata.
</p>

<p align="center">
  <a href="https://lineai-search.com"><strong>Explore Live Demo »</strong></a>
</p>

<hr />

<h3>Core Concept</h3>
<p>
  LineAI solves the "LLM Hallucination" problem by forcing generative models to reference 
  verified academic metadata before synthesizing answers. It uses a <strong>Hexagonal Architecture</strong> 
  (Ports & Adapters) to decouple core research logic from volatile external APIs.
</p>



<h3>The Knowledge Grid</h3>
<table width="100%">
  <tr>
    <td width="30%"><strong>Engine</strong></td>
    <td width="40%"><strong>Role</strong></td>
    <td><strong>Source</strong></td>
  </tr>
  <tr>
    <td>Gemini 3 Flash</td>
    <td>Contextual Synthesis</td>
    <td><a href="https://ai.google.dev/">Google AI</a></td>
  </tr>
  <tr>
    <td>CrossRef</td>
    <td>Metadata Retrieval</td>
    <td><a href="https://api.crossref.org">CrossRef REST</a></td>
  </tr>
  <tr>
    <td>OpenAlex</td>
    <td>Global Citation Graph</td>
    <td><a href="https://openalex.org/">OpenAlex API</a></td>
  </tr>
</table>

<h3>System Architecture</h3>
<ul>
  <li><strong>Domain Layer:</strong> Pure business logic and entity models.</li>
  <li><strong>Application Layer:</strong> Research orchestration and synthesis pipelines.</li>
  <li><strong>Infrastructure Layer:</strong> Decoupled adapters for Gemini, CrossRef, and OpenAlex.</li>
</ul>



<h3>Visual Preview</h3>
<p align="center">
  <img src="https://github.com/vassishap/lineai/raw/main/docs/screenshot.png" alt="LineAI Interface" width="800">
</p>

<hr />

<p align="center">
  Built with <strong>FastAPI</strong>, <strong>React</strong>, and <strong>Google Cloud Run</strong>.
</p>
