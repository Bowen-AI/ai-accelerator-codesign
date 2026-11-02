"""Educational CPU-only accelerator roofline model.

Analytical estimate, NOT a cycle-accurate TPU emulator, silicon power estimate,
or hardware benchmark. Assumes ideal compute/memory overlap and simple DRAM traffic.
"""
import argparse
import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Accelerator:
    name: str
    compute_tops: float
    bandwidth_gbs: float
    utilization: float = 0.6

    def __post_init__(self):
        if self.compute_tops <= 0 or self.bandwidth_gbs <= 0:
            raise ValueError("Compute and bandwidth must be positive")
        if not 0 < self.utilization <= 1:
            raise ValueError("Utilization must be within (0,1]")


@dataclass(frozen=True)
class GEMM:
    name: str
    m: int
    n: int
    k: int
    bytes_per_element: int = 2
    output_bytes_per_element: int = 2
    traffic_multiplier: float = 1.0

    def __post_init__(self):
        if min(self.m, self.n, self.k, self.bytes_per_element,
               self.output_bytes_per_element) <= 0:
            raise ValueError("Dimensions and byte widths must be positive")
        if self.traffic_multiplier < 1:
            raise ValueError("Traffic multiplier must be >= 1")

    @property
    def ops(self):
        return 2 * self.m * self.n * self.k

    @property
    def bytes_accessed(self):
        # Optimistic lower bound: read each input once, write output once.
        minimum = (self.m * self.k + self.k * self.n) * self.bytes_per_element
        minimum += self.m * self.n * self.output_bytes_per_element
        return minimum * self.traffic_multiplier

    @property
    def arithmetic_intensity(self):
        return self.ops / self.bytes_accessed


def estimate(workload: GEMM, chip: Accelerator):
    compute_s = workload.ops / (chip.compute_tops * 1e12 * chip.utilization)
    memory_s = workload.bytes_accessed / (chip.bandwidth_gbs * 1e9)
    return {
        "workload": workload.name,
        "chip": chip.name,
        "m": workload.m,
        "n": workload.n,
        "k": workload.k,
        "ops": workload.ops,
        "bytes": int(workload.bytes_accessed),
        "arithmetic_intensity_ops_per_byte": round(workload.arithmetic_intensity, 3),
        "compute_floor_ms": round(compute_s * 1e3, 6),
        "memory_floor_ms": round(memory_s * 1e3, 6),
        "estimated_latency_ms": round(max(compute_s, memory_s) * 1e3, 6),
        "bottleneck": "compute" if compute_s >= memory_s else "memory",
    }


def workloads():
    # Illustrative shapes, not any production Google TPU specifications.
    return [
        GEMM("decode_batch1_projection", 1, 4096, 4096),
        GEMM("decode_batch32_projection", 32, 4096, 4096),
        GEMM("prefill_1024_projection", 1024, 4096, 4096),
        GEMM("mlp_prefill", 1024, 11008, 4096),
    ]


def chips():
    return [
        Accelerator("baseline", 100, 1000),
        Accelerator("double_compute", 200, 1000),
        Accelerator("double_bandwidth", 100, 2000),
        Accelerator("both_doubled", 200, 2000),
    ]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--demo", action="store_true")
    group.add_argument("--sweep", action="store_true")
    p.add_argument("--out", default="results.csv")
    args = p.parse_args()
    if args.demo:
        for w in workloads():
            r = estimate(w, chips()[0])
            print("{}: {} ms ({})".format(
                w.name, r["estimated_latency_ms"], r["bottleneck"]))
    else:
        rows = [estimate(w, chip) for w in workloads() for chip in chips()]
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print("Wrote {} estimated scenarios to {}".format(len(rows), args.out))
        for row in rows:
            print("{} | {} | {} ms | {}".format(
                row["workload"], row["chip"], row["estimated_latency_ms"],
                row["bottleneck"]))


if __name__ == "__main__":
    main()
