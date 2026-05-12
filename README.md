# Task Type 2 — MapReduce on Integers (Min, Max, Sum)
# Complete Code + Commands

---

## Key Concept

- Every Mapper emits the SAME constant key ("max", "min", "sum")
- This forces ALL values to go to ONE Reducer
- Reducer computes the single global answer


---

## Commands to Run Any of These

```bash
# Compile (example for Max)
javac -classpath $(hadoop classpath) -source 8 -target 8 -d . MaxMapReduce.java

# Package
jar -cvf max.jar *.class

# Create input directory and upload
hdfs dfs -mkdir -p /input
hdfs dfs -put numbers.txt /input/

# Run
hadoop jar max.jar MaxMapReduce /input/numbers.txt /output

# Read output
hdfs dfs -cat /output/part-r-00000

# Expected output for Max:
# max    91

# Re-run cleanup
hdfs dfs -rm -r /output
```

---

## Common Exam Mistake

Using 0 as starting value for max or min:
- int maxSoFar = 0  → WRONG if all numbers are negative
- int minSoFar = 0  → WRONG if all numbers are positive
Always use Integer.MIN_VALUE / Integer.MAX_VALUE
