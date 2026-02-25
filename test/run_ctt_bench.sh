#!/data/data/com.termux/files/usr/bin/bash
echo "Compiling Φ-24 Topological Engine..."
clang -O3 src/ctt_engine.c -lm -o ctt_solver

echo "Running 11ns Quenching Simulation..."
./ctt_solver --mode=resonance --alpha=0.0765872
