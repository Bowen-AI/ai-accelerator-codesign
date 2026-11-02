# AI Accelerator Co-Design

**An independent, open six-week course in AI accelerator architecture and hardware–software co-design.**

**[Course website](https://bowen-ai.github.io/ai-accelerator-codesign/) · [Full curriculum](https://bowen-ai.github.io/ai-accelerator-codesign/curriculum.html) · [Reading library](https://bowen-ai.github.io/ai-accelerator-codesign/readings.html) · [Capstone brief](https://bowen-ai.github.io/ai-accelerator-codesign/capstone.html)**

This course examines a central challenge in accelerator engineering: identifying which hardware changes meaningfully improve the performance of modern AI workloads. It connects Transformer operations, data movement, accelerator organization, microarchitecture and practical implementation constraints.

The course is designed for programmers and systems engineers with a working understanding of linear algebra. No prior RTL knowledge is required. The **core is CPU-only**; access to a TPU, FPGA or discrete GPU is optional.

## Course at a glance

| Duration | Workload | Required hardware | Final assessment |
|---|---|---|---|
| 6 weeks | 8–10 hours/week (48–60 total) | Python 3.10+ on a CPU computer | Workload-driven architecture design review |

| Module | Focus | Technical output |
|---|---|---|
| 01 | Workload characterization | Resource accounting and bottleneck analysis |
| 02 | Architecture and dataflow | Compute–bandwidth design comparison |
| 03 | Model-aware co-design | Precision and traffic sensitivity report |
| 04 | RTL and physical constraints | Implementation risk assessment |
| 05 | Design-space exploration | Controlled experiment and design shortlist |
| 06 | Architecture review | Capstone memo and five-slide presentation |

The complete study sequence, prerequisites and assessments are described in the [public curriculum](https://bowen-ai.github.io/ai-accelerator-codesign/curriculum.html). University references appear in the [reading library](https://bowen-ai.github.io/ai-accelerator-codesign/readings.html).

## Interactive study site

GitHub Pages serves the static website from the root HTML files and `assets/site.css`, using the [Pages deployment workflow](.github/workflows/deploy-pages.yml). The site includes an interactive **roofline trade-off explorer** that runs directly in the browser.

The browser model illustrates a simplified relationship between compute demand, external memory traffic and latency. **It is not a TPU emulator, cycle-accurate architecture simulation, power estimate or silicon benchmark.** The program explicitly states its modeling assumptions.

## Reproducible Python lab

The educational simulator requires only Python 3.10+ and the standard library:

```bash
python3 labs/roofline.py --demo
python3 labs/roofline.py --sweep --out results.csv
python3 -m unittest discover -s labs -p 'test_*.py'
```

The model evaluates illustrative GEMM workloads against hypothetical accelerator configurations. Its CPU-only scripts produce estimated time floors, not measured processor performance.

## Selected academic references

- [MIT 6.5930 — Hardware Architecture for Deep Learning](https://csg.csail.mit.edu/6.5930/syllabus.html): architecture design, workload mapping and exploration.
- [Stanford CS217 — Hardware Accelerators for Machine Learning](https://cs217.stanford.edu/): accelerator architecture, high-level synthesis and remote cloud FPGA work.
- [MIT 6.5940 — Efficient AI Computing](https://hanlab.mit.edu/course): quantization, pruning and efficient inference.
- [Stanford CS336 — Language Modeling from Scratch](https://cs336.stanford.edu/): Transformer workloads, GPU/TPU performance and inference.

The original university courses vary in publicly available lectures, exercises and computing resources. This project draws on openly accessible materials and provides **independently authored exercises**, not redistributed university courseware or solutions. Course participation and academic credit are not provided by this repository.

## Further study

The optional advanced track extends analytical models to mapping simulators such as [Timeloop/Accelergy](https://timeloop.csail.mit.edu/), RTL simulation using [Verilator](https://verilator.org/guide/latest/), physical design with [OpenROAD](https://openroad.readthedocs.io/) and independently accessible GPU/FPGA experiments.

## Publishing and contribution

The static site is deployed using GitHub Actions; technical details are documented in [PUBLISHING.md](PUBLISHING.md). Changes to public study material should preserve attribution and avoid proprietary code, non-public data, vendor IP or confidential employer designs.

Original repository content is available under the [MIT License](LICENSE). Third-party resources retain their respective rights. **This independent course is not affiliated with or endorsed by MIT, Stanford or Google.**
