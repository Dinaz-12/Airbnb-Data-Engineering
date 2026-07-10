import subprocess
import sys

scripts = [
    "src/ingest.py",
    "src/clean.py",
    "src/transform.py",
    "src/create_database.py",
    "src/build_star_schema.py",
    "src/run_queries.py",
    "src/eda.py",
    "src/statistics.py"
]

for script in scripts:
    print("\n" + "=" * 60)
    print(f"Running: {script}")
    print("=" * 60)

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"❌ Error while running {script}")
        sys.exit(result.returncode)

print("\n🎉 Data Engineering Pipeline Completed Successfully!")