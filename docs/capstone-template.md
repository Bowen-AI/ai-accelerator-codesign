# Capstone: Workload-driven accelerator recommendation

**Topic:** One specific architecture improvement for a publicly described or illustrative AI workload. **Never include Google-internal information.**

## 1. Executive summary (maximum 200 words)
Recommend a change and quantify the expected improvement *under an explicit set of assumptions*.

## 2. Workload model
Create a table with layer/operator, M/N/K dimensions, batch, precision, estimated FLOPs, modelled bytes, and reason for selecting it. Cover at least two workloads, preferably decode and prefill.

## 3. Proposed architecture
State baseline TOPS, memory bandwidth, utilization, assumed mapping/reuse and bottlenecks. List limitations, including cache capacity, interconnect, contention, clock frequency and power.

## 4. Controlled experiments
Run the sweep in labs/roofline.py. Compare baseline, twice compute, twice memory bandwidth, twice both. Vary utilization and traffic multiplier to check whether the conclusion changes.

## 5. Design comparison
Show results with estimated latency, throughput assumptions and (if independently justified) an area/energy proxy. **The provided toy model does not output real area or energy.**

## 6. Decision
Which investment gives the strongest workload improvement for an assumed resource budget? Show the sensitivity of the answer and what additional evidence would change your conclusion.

## 7. Validation plan
Name an appropriate next tool: Timeloop/Accelergy for mapping/activity estimates; RTL simulation for correctness; OpenROAD for implementation constraints; cloud FPGA/GPU for measured kernels.

## Five-slide review
1. Workload and problem
2. Bottleneck and baseline
3. Architecture alternatives
4. Evidence, sensitivity, limitations
5. Recommendation and next experiment

## Completion rubric
- Numerical assumptions are clearly documented.
- Each claim is supported by a calculation or experiment.
- Trade-offs and counterexamples are included.
- Physical-design limitations are not misrepresented as measured.
- No confidential employer designs or performance data.
