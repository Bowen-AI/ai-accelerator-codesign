# Capstone assessment · Accelerator architecture design review

The final assessment applies workload characterization, analytical performance modeling, implementation awareness and engineering judgment to an accelerator design choice.

**Objective.** Present an evidence-based recommendation for improving one well-defined class of AI workload. The analysis must use publicly documented or synthetic inputs and explicitly state its assumptions.

## Scope

The study examines at least two operating conditions, ideally contrasting autoregressive decoding and sequence prefill. Candidate changes may include additional compute capacity, memory bandwidth, on-chip data reuse or model precision.

## Required artifacts

**Architecture memo.** A brief, structured report containing:

1. **Problem and workload.** Model/operator, GEMM dimensions, precision, batch size, estimated operation counts and data movement.
2. **Baseline.** Assumed compute capability, bandwidth, utilization, memory traffic and resulting performance bound.
3. **Alternatives.** At least four controlled configurations including increased compute, bandwidth and both combined.
4. **Results.** Comparative table or figures, interpretation, sensitivity to utilization and memory-transfer assumptions.
5. **Recommendation.** The preferred alternative for a clearly stated objective, possible counterexamples and relevant uncertainties.
6. **Validation.** A plan to test the hypothesis in higher-fidelity modeling, RTL, physical implementation or cloud hardware.

**Five-slide review.** Workload; baseline bottleneck; architectural alternatives; evidence and limitations; recommendation and validation plan.

## Assessment criteria

Technical work is judged by the correctness of assumptions and units, reproducible experiments, relevance to actual workload bottlenecks, recognition of uncertain effects and clarity of the recommendation.

## Important limitations

The included roofline simulator is a first-order analytical model. It **does not** estimate transistor area, energy, physical clock speed or route timing. Those require additional methods and evidence. Claims about fabricated silicon must not be inferred from the simple simulator.

Any public submission must exclude employer-confidential designs, internal performance measurements, vendor specifications and private data. Use only public or synthetic examples.

See the full [capstone project page](../capstone.html) and [course curriculum](../curriculum.html).
