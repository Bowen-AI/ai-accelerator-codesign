# Official materials and a six-week reading path

This is an independent, original study guide, **not** an official Stanford or MIT course, and not a mirror of university lecture slides, videos or assignment solutions. Links go to the university-maintained originals. Some course-lab environments need enrollment or cloud compute.

## Week 1 — Workload anatomy and the roofline model
**Stanford CS336 (Spring 2026):**
- [Course schedule with recordings and materials](https://cs336.stanford.edu/).
- Lecture 2: resource accounting (FLOPs, bytes and arithmetic intensity).
- Lecture 3: Transformer architectures.
- Lecture 10: inference and how batch/prefill/decode change bottlenecks.
**MIT 6.5930:** [syllabus](https://csg.csail.mit.edu/6.5930/syllabus.html), especially Einsums + Transformers.

Task: list FLOPs and minimal modelled DRAM bytes for two GEMMs; run the CPU-only roofline demo. Explain what the simplified model leaves out.

## Week 2 — Accelerator architecture and dataflow
**MIT 6.5930:** [official course schedule](https://csg.csail.mit.edu/6.5930/syllabus.html), lectures on Mapping: Dataflow & Partitioning and Fusion.
**Stanford CS217:** [official accelerator design/HLS/FPGA course page](https://cs217.stanford.edu/).
**Optional open-source tooling:** [Timeloop / Accelergy project](https://timeloop.csail.mit.edu/).

Task: compare doubled compute against doubled bandwidth at several batch sizes, then describe a plausible on-chip SRAM tiling strategy.

## Week 3 — Algorithm/hardware co-design
**MIT 6.5940 (Fall 2026):** [official schedule and posted slides/videos](https://hanlab.mit.edu/course). Prioritize pruning/sparsity, quantization, Transformers/LLMs, and LLM quantization.
**Stanford CS336:** lectures 4 (attention alternatives), 5 (GPUs/TPUs), and 10 (inference).

Task: compare approximate INT8 and FP16 weight traffic and state the extra assumptions needed to claim throughput or energy improvements.

## Week 4 — RTL and physical design
**Stanford CS217:** official project overview (C++/SystemC, high-level synthesis, cloud FPGA evaluation).
**Tools:** [Verilator](https://verilator.org/guide/latest/) for RTL simulation; [OpenROAD](https://openroad.readthedocs.io/) for open-source physical design.

Task: prepare a block diagram tracing datapath → state/registers → synthesized cells → placed/routed physical chip. Optional: simulate a synchronous MAC. No physical board required.

## Week 5 — Architecture design-space exploration
**MIT 6.5930:** mapping, parallelism, fusion, sparsity and compute-in-memory course topics.
**Optional simulation upgrade:** [AccelForge](https://accelergy-project.github.io/accelforge/guide/modeling.html) or [Timeloop/Accelergy](https://timeloop.csail.mit.edu/).

Task: run the 16-case design sweep. Identify Pareto-relevant tradeoffs and test whether conclusions reverse when utilization is lower or external traffic increases.

## Week 6 — Capstone and design review
Revisit the official design-project descriptions for MIT 6.5930 and the practical architecture questions in Stanford CS217.

Task: fill in [capstone-template.md](capstone-template.md) with a numerical recommendation, a sensitivity analysis, a review-ready five-slide outline, and a plan for validating the proposal with higher-fidelity models.

## Important course availability details
- MIT 6.5930 Spring 2026 explicitly states its lectures **were not recorded**; public lecture notes and some PDFs are posted.
- Stanford CS217 Winter 2026 includes **remote real FPGAs** but does not guarantee non-student access to FPGA labs or recordings.
- Stanford CS336 Spring 2026 links public recordings, assignments, and GPU-intensive systems coursework.
- MIT 6.5940 Fall 2026 posts many slides/videos, but availability depends on the specific class meeting.
- This study path runs on a CPU-only laptop; the university classes' original assignments may require cloud hardware or course access.
