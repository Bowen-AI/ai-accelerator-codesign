# AI Accelerator Co-Design: 6-Week Intensive

**Goal:** Develop the ability to identify bottlenecks in AI workloads and make a defensible accelerator architecture recommendation, using a CPU-only laptop.

**Who it is for:** Software / systems engineers working near TPU, GPU, chip or AI accelerator design. Assumes Python and basic linear algebra; no previous RTL or VLSI experience needed.

**Effort:** 6 weeks, **8–10 hours/week** (48–60 hours). For a four-week sprint, combine Weeks 1+2 and Weeks 3+4 and reduce the final project. For deeper mastery, add the optional RTL, FPGA and advanced-mapping exercises (another 4–6 weeks).

**Public study site:** Open [`index.html`](./index.html) in a browser. It works fully offline (external course links require internet). For GitHub Pages, see [Publishing](#publishing-to-github-pages).

**Run the labs:** Python 3.10+; **no Python packages needed**.

```bash
python3 labs/roofline.py --demo
python3 labs/roofline.py --sweep --out results.csv
python3 -m unittest discover -s labs -p 'test_*.py'
```

## Hardware requirements and what the official courses actually use

- **MIT 6.5930 (Spring 2026)**: hands-on labs in DNN workload analysis, mapping, sparsity and compute-in-memory; the publicly described work centers on architecture modeling and open-ended design, including AccelForge. You do not need to own an accelerator. Some classroom lab materials may require course access. **MIT explicitly said it would not record the 2026 lectures**, though notes/slides were linked publicly.
- **Stanford CS217 (Winter 2026)**: includes **real cloud FPGA evaluation** of C++/SystemC high-level synthesis designs. It does not require owning an FPGA, but reproducing the full enrolled-class flow may need provisioned cloud resources and course tooling. The public syllabus is not a guarantee of open lab access.
- **Stanford CS336 (Spring 2026)**: public videos and assignments; the full model-training and GPU-kernel assignments require GPU compute, which self-study students may rent remotely. Our selected analytical workload exercises don't.
- **MIT 6.5940 (Fall 2026)**: public videos and slides where posted; labs include GPU basics and on-laptop LLM deployment. Some original exercises may require a GPU; our replacements do not.

Core labs here are **original, CPU-friendly educational exercises**. They are not official course assignments. Results are analytical models, **not physical-chip benchmarks** or measured power, and should not be presented as real TPU performance.

For lecture-by-lecture pointers and what to read each week, see the **[curated course materials and reading path](docs/course-materials.md)**.

## Syllabus: exact topics, materials, exercises, deliverables

| Week | Topics (8–10 hours) | Study materials | Hands-on deliverable |
|---|---|---|---|
| **1: Workloads & bottlenecks** | Transformer inference prefill vs decode; GEMM dimensions; FLOPs/MACs; parameters, activation and KV cache traffic; arithmetic intensity and roofline | [Stanford CS336](https://cs336.stanford.edu/) intro + systems lectures; [MIT 6.5930 syllabus](https://csg.csail.mit.edu/6.5930/syllabus.html) overview and Einsums/Transformers; [MIT 6.5940](https://hanlab.mit.edu/course) intro | Run `roofline.py --demo`. Create a table of GEMM vs memory-bound cases and a one-page bottleneck diagnosis. |
| **2: Accelerator architecture** | PEs/MAC arrays, systolic dataflow, hierarchy SRAM/HBM, reuse, tiling, mapping and bandwidth ceilings; latency versus throughput | [Stanford CS217](https://cs217.stanford.edu/) course overview; [MIT 6.5930](https://csg.csail.mit.edu/6.5930/syllabus.html) Mapping/Dataflow notes; [Timeloop/Accelergy](https://timeloop.csail.mit.edu/) | Sweep compute and bandwidth. Build a 2×2 design tradeoff matrix: compute × bandwidth. |
| **3: AI algorithm–hardware co-design** | Attention and KV-cache decoding; batch size, prompt length, precision and quantization; sparsity and pruning; when theoretical FLOP reduction helps or hurts | [MIT 6.5940](https://hanlab.mit.edu/course) pruning/quantization videos; [Stanford CS336](https://cs336.stanford.edu/) systems/performance topics; [MIT 6.5930](https://csg.csail.mit.edu/6.5930/syllabus.html) sparsity/precision notes | Analyze FP16 vs INT8 assumed traffic and compute. Compare prefill with decode; note modeling assumptions. |
| **4: RTL, synthesis, physical constraints** | Architecture vs microarchitecture vs RTL; registers, clocking, pipelines, synthesis, critical paths, power–performance–area (PPA); placement, routing and timing | [Stanford CS217](https://cs217.stanford.edu/) C++/SystemC HLS description; [Verilator](https://verilator.org/guide/latest/); [OpenROAD](https://openroad.readthedocs.io/) | Write a block-level accelerator diagram and an original timing/area constraint worksheet. Optional: implement small MAC pipeline in Verilog and simulate locally. |
| **5: Design-space exploration** | Area / throughput / energy proxies; bottleneck shifts; workload mixes, mapping and fusion; Pareto frontiers, sensitivity analysis and model uncertainty | [MIT 6.5930](https://csg.csail.mit.edu/6.5930/info.html) mapping/fusion labs; [AccelForge docs](https://accelergy-project.github.io/accelforge/guide/modeling.html); [Timeloop](https://timeloop.csail.mit.edu/) | Run the automated sweep and select two non-dominated designs. Draft architecture recommendation (with caveats). |
| **6: Capstone & communication** | End-to-end AI accelerator co-design; selecting an objective, checking assumptions, arguing design choices; optional real GPU/FPGA validation | Revisit [MIT 6.5930](https://csg.csail.mit.edu/6.5930/) capstone outline and [Stanford CS217](https://cs217.stanford.edu/) HLS/FPGA scope | Complete `docs/capstone-template.md`: executive summary, workloads, baseline, scenarios, Pareto chart, sensitivity, risks and recommended next experiments. |

### Weekly cadence

- **~2 hours**: lecture videos, slides or public notes.
- **~2 hours**: reproduce formulas by hand and make design assumptions explicit.
- **~3–4 hours**: coding/measurement in the provided CPU-only simulator.
- **~1–2 hours**: short memo and review; make one decision-oriented claim backed by numbers.

### Checkpoints

- Week 1: identify a compute-bound and memory-bound workload with quantitative justification.
- Week 2: explain the bottleneck after doubling MAC throughput or memory bandwidth.
- Week 3: compare at least two precision or caching assumptions.
- Week 4: identify the RTL/microarchitecture/physical-design boundaries in a proposed change.
- Week 5: produce a design-space sweep and point out model uncertainty.
- Week 6: present one actionable hardware recommendation with evidence and validation plan.

## Optional advanced track (after six weeks)

1. Replace the roofline proxy with **AccelForge** or **Timeloop/Accelergy** for realistic mapping and energy proxies, following the official tool documentation. No fabricated chip required, but setup is more involved.
2. Add a cycle-approximate RTL design using Verilator; optionally run OpenROAD (toolchain and PDK constraints apply).
3. If you have independent access to a cloud FPGA or GPU, validate selected kernels remotely. This is a **remote real-hardware** experiment, not emulation; budgets and tool availability vary.

## Resources and attribution

**Curated links, not copied university courseware:**
- MIT 6.5930: <https://csg.csail.mit.edu/6.5930/> (public notes and syllabus; 2026 lectures not recorded).
- Stanford CS217: <https://cs217.stanford.edu/> (cloud FPGA/HLS work described on official course page).
- MIT 6.5940: <https://hanlab.mit.edu/course> (videos/slides where posted).
- Stanford CS336: <https://cs336.stanford.edu/> (recordings, assignments, GPU requirements).
- MIT CSAIL Timeloop/Accelergy: <https://timeloop.csail.mit.edu/>.
- AccelForge: <https://accelergy-project.github.io/accelforge/guide/modeling.html>.
- Verilator: <https://verilator.org/guide/latest/>; OpenROAD: <https://openroad.readthedocs.io/>.

The files, notes, worksheets and original simulator in this study project are original educational content. Follow upstream licenses and course policies before redistributing their material. **Avoid posting employer-confidential designs, TPU performance figures or internal Google specifications** into a public repository.

## Publishing on Bowen-AI GitHub Pages

The source repository is [Bowen-AI/ai-accelerator-codesign](https://github.com/Bowen-AI/ai-accelerator-codesign). After GitHub Pages is enabled, the expected website is [bowen-ai.github.io/ai-accelerator-codesign](https://bowen-ai.github.io/ai-accelerator-codesign/). This URL is not confirmed live until a successful Pages deployment.

In GitHub: **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save**. See [PUBLISHING.md](PUBLISHING.md). All materials on this public site are public or original; do not upload employer-confidential content.

## License

Original study artifacts and example code in this project: MIT License (see [`LICENSE`](./LICENSE)). University links/content retain their own rights.