# Course reference guide

The reading sequence supports the [six-week curriculum](../curriculum.html). Links point to the relevant course providers; availability of recordings, slides and student-only environments varies by term. This is an independent study program rather than an MIT or Stanford offering.

## Module 1 · AI workloads and roofline analysis

**Primary material:** [Stanford CS336](https://cs336.stanford.edu/) on model resource accounting, Transformer architecture and inference; [MIT 6.5930](https://csg.csail.mit.edu/6.5930/syllabus.html) on DNN workloads, Einsums and Transformer operators.

**Engineering exercise:** A two-workload roofline comparison including GEMM FLOPs, minimal off-chip transfers, arithmetic intensity and assumptions about reuse.

## Module 2 · Accelerator architecture and dataflow

**Primary material:** [MIT 6.5930](https://csg.csail.mit.edu/6.5930/syllabus.html) on mapping and dataflow; [Stanford CS217](https://cs217.stanford.edu/) on accelerator architecture and hardware implementation; [Timeloop/Accelergy](https://timeloop.csail.mit.edu/) for an introduction to mapping tools.

**Engineering exercise:** A small sweep comparing additional arithmetic throughput with additional memory bandwidth, accompanied by a proposed tiling strategy.

## Module 3 · Model-aware hardware optimization

**Primary material:** [MIT 6.5940](https://hanlab.mit.edu/course) on quantization, sparsity and efficient inference; [Stanford CS336](https://cs336.stanford.edu/) on GPU/TPU performance, attention and inference.

**Engineering exercise:** An FP16/INT8 footprint comparison distinguishing the reduction in transferred bytes from actual execution speed and energy.

## Module 4 · RTL and physical constraints

**Primary material:** [Stanford CS217](https://cs217.stanford.edu/) on high-level synthesis and FPGA work; [Verilator](https://verilator.org/guide/latest/) documentation; [OpenROAD](https://openroad.readthedocs.io/) documentation.

**Engineering exercise:** A register-to-register datapath diagram and assessment of synthesis and timing risks. Optional extension: RTL simulation for a small synchronous MAC.

## Module 5 · Architecture design-space exploration

**Primary material:** [MIT 6.5930](https://csg.csail.mit.edu/6.5930/syllabus.html) on mapping, fusion and system design; [Timeloop/Accelergy](https://timeloop.csail.mit.edu/) for additional modeling methods.

**Engineering exercise:** A design-space sweep showing how architecture recommendations change with assumed utilization and memory traffic.

## Module 6 · Technical architecture review

**Primary material:** Revisit design-project topics from [MIT 6.5930](https://csg.csail.mit.edu/6.5930/) and implementation perspectives from [Stanford CS217](https://cs217.stanford.edu/).

**Assessment:** The [capstone brief](../capstone.html) specifies an evidence-based architecture recommendation, reproducible comparison and validation plan.

## Access and scope

MIT 6.5930's Spring 2026 site indicates that its lectures were not recorded, although notes and other resources are available. Stanford CS217 describes hardware experiments on cloud-accessed FPGAs but does not guarantee public lab access. Stanford CS336 provides public course material, with some original assignments needing GPU compute. MIT 6.5940 has publicly posted materials, depending on session.

The provided core exercises in this repository run on a CPU-only machine and are not official assignments from those universities.
