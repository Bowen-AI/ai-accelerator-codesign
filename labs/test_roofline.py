import unittest
from roofline import Accelerator, GEMM, estimate


class RooflineTests(unittest.TestCase):
    def test_gemm_ops(self):
        w = GEMM("tiny", 2, 3, 4)
        self.assertEqual(w.ops, 48)
        self.assertEqual(w.bytes_accessed, (8 + 12 + 6) * 2)

    def test_memory_bound_faster_with_more_bw(self):
        w = GEMM("batch1", 1, 4096, 4096)
        a = estimate(w, Accelerator("slow", 100, 100))
        b = estimate(w, Accelerator("fast", 100, 200))
        self.assertEqual(a["bottleneck"], "memory")
        self.assertLess(b["estimated_latency_ms"], a["estimated_latency_ms"])

    def test_compute_bound_faster_with_more_compute(self):
        w = GEMM("high_reuse", 4096, 4096, 4096)
        a = estimate(w, Accelerator("slow", 1, 1000))
        b = estimate(w, Accelerator("fast", 2, 1000))
        self.assertEqual(a["bottleneck"], "compute")
        self.assertLess(b["estimated_latency_ms"], a["estimated_latency_ms"])

    def test_bad_chip_rejected(self):
        with self.assertRaises(ValueError):
            Accelerator("bad", 0, 100)


if __name__ == "__main__":
    unittest.main()
