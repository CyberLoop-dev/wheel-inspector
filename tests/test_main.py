import tempfile
import unittest
import zipfile
from pathlib import Path
from main import inspect_wheel


class WheelInspectorTests(unittest.TestCase):
    def test_reads_metadata_and_scripts(self):
        with tempfile.TemporaryDirectory() as folder:
            wheel = Path(folder) / "demo-1.0-py3-none-any.whl"
            with zipfile.ZipFile(wheel, "w") as archive:
                archive.writestr("demo-1.0.dist-info/METADATA",
                    "Metadata-Version: 2.1\nName: demo\nVersion: 1.0\nRequires-Dist: requests>=2\n")
                archive.writestr("demo-1.0.dist-info/WHEEL", "Wheel-Version: 1.0\n")
                archive.writestr("demo-1.0.dist-info/RECORD", "")
                archive.writestr("demo-1.0.dist-info/entry_points.txt",
                    "[console_scripts]\ndemo = demo.cli:main\n")
            report = inspect_wheel(wheel)
            self.assertEqual(report["name"], "demo")
            self.assertEqual(report["requires_dist"], ["requests>=2"])
            self.assertEqual(report["console_scripts"]["demo"], "demo.cli:main")
            self.assertTrue(report["dist_info"]["record"])


if __name__ == "__main__":
    unittest.main()
