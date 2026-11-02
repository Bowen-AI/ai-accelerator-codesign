# RTL and physical design: a fast primer

- **Architecture:** Choose the workloads, compute arrays, memory capacity/bandwidth, interconnect, and numerical precision.
- **Microarchitecture:** Specify pipelines, clock cycles, state machines, buffers, resource scheduling, and data movement.
- **RTL (Register Transfer Level):** Encode cycle-level digital behavior in Verilog or SystemVerilog. Simulation checks behavior, not actual silicon speed.
- **Synthesis:** Convert RTL to gates/registers under a standard-cell library and timing constraints.
- **Physical design:** Place cells, build the clock tree, route wires, analyze parasitics and timing, and close power/performance/area (PPA).
- **Fabrication and validation:** Produce real silicon and measure it.

## Example

Doubling MACs may change a compute-bound model's theoretical execution time, but will do little if an LLM decoder is waiting for weights in memory. It can also increase area, routing congestion, timing and power.

## Optional activity (CPU only)

Implement an 8-bit synchronous, registered multiply-accumulate. Describe reset behavior, numerical overflow and pipeline latency. Test using Verilator or Icarus Verilog. Explain why logic simulation alone cannot establish physical timing, dynamic power or silicon yield.

For tool docs: https://verilator.org/guide/latest/ and https://openroad.readthedocs.io/.
