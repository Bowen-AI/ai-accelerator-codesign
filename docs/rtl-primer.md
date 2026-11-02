# RTL and physical design: a concise technical overview

AI accelerator development spans architecture, microarchitecture, digital design and physical implementation. Each discipline addresses a different level of the hardware system.

| Stage | Key question | Typical work |
|---|---|---|
| Architecture | Which computational and memory resources should exist? | Arrays, hierarchy, bandwidth, interconnect, precision |
| Microarchitecture | How is the architecture realized over clock cycles? | Buffers, pipelines, state machines, scheduling |
| RTL | What is the cycle-level behavior of the digital design? | Verilog/SystemVerilog, registers, combinational logic, verification |
| Logic synthesis | How can RTL be mapped to a technology library? | Gates, sequential cells, timing constraints |
| Physical design | Can the netlist meet timing, power and area constraints? | Placement, clock-tree synthesis, routing, parasitic analysis |
| Silicon validation | Does manufactured hardware meet specifications? | Timing, power, functional and reliability measurements |

## Applied example

Increasing the arithmetic capacity of a matrix-multiplication array can reduce the theoretical execution time of compute-limited operators. The benefit may disappear for memory-limited decoding, while larger logic structures may increase routing distance, area, power and timing complexity.

## Optional RTL laboratory

A small synchronous multiply-accumulate unit provides a compact setting for reasoning about registered inputs, latency, pipeline stages, overflow and reset. Simulation through [Verilator](https://verilator.org/guide/latest/) evaluates functional behavior; it does not independently establish silicon timing or physical power consumption. [OpenROAD](https://openroad.readthedocs.io/) provides an introduction to physical design workflows and implementation constraints.
