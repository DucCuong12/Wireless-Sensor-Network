# Wireless-Sensor-Network
Addressing the challenge of maximizing the count of targets that fulfill both K-coverage and K-connectivity requirements within a wireless sensor network (WSN) while maintaining a predetermined number of sensors


# PAPER: Memetic Algorithm for maximizing K-coverage and K-connectivity in Wireless Sensors Network:  This paper is ACCEPTED in Jounal Informatica2024 ISI Q2 

This repository contains the implementation of a novel hybrid optimization approach combining Genetic Algorithm (GA), Prim's Algorithm, and a specialized local search strategy. The proposed method is designed to address the K-Coverage problem while ensuring connectivity in sensor networks. Our approach effectively balances exploration and exploitation to achieve optimal sensor deployment.

## Features
- **Chromosome Representation:** Binary vector with `n+1` elements.
- **Genetic Operators:** Heuristic Crossover & Mutation.
- **Local Search Strategy:** Fine-tuning solutions for improved performance.
- **Fitness Evaluation:** Optimized for K-Coverage and connectivity.
- **Selection & Replacement:** Advanced heuristics for evolutionary progress.

## Chromosome Representation
Each chromosome is a **binary vector** of length **n+1**, where:
- **1** → The corresponding cluster is considered for connectivity.
- **0** → The corresponding cluster is ignored.
- **Base Station** is always included.

After selecting clusters, **Prim’s Algorithm** is applied to compute the minimal sensor connections.

## Genetic Operators
### Crossover (Heuristic Crossover)
A heuristic crossover generates an offspring based on:
- If `P1[i] = P2[i]`, the child inherits `P1[i]`.
- If `P1[i] ≠ P2[i]`, the child inherits `P1[i]` with probability:
  ```math
  fitness(P1) / (fitness(P1) + fitness(P2))

  ### Mutation (Heuristic Mutation)
The mutation strategy ensures a balance between **exploration** and **constraint satisfaction**:
- **For feasible solutions (sufficient sensors for connectivity)**:
  - Iterate through positions with `0` values.
  - Flip `0 → 1` with a probability `pro`.
  - Reduce `pro` by `1 / (2n)` after each mutation to prevent excessive changes.
  
- **For infeasible solutions (insufficient sensors for connectivity)**:
  - Iterate through positions with `1` values.
  - Flip `1 → 0` using the same probability `pro`.
  - This helps move infeasible solutions toward feasibility without excessive modifications.

### Local Search Strategy
To enhance the best individual (`Best_indi`):
1. Iterate through all positions where `Best_indi[i] = 0`.
2. Flip `0 → 1` one at a time and evaluate the new solution.
3. If the new solution satisfies the constraints and improves fitness, it replaces `Best_indi`.

This method ensures gradual improvement without drastic modifications.

### Fitness Evaluation
The fitness function evaluates solutions based on **K-Coverage** and **K-Connectivity** constraints:
- **Feasible individuals (sufficient sensors)**:
  - Fitness is computed as the total number of targets satisfying **K-Coverage** and **K-Connectivity**.

- **Infeasible individuals (insufficient sensors)**:
  - Fitness is calculated as:
    ```math
    fitness = \frac{1}{\text{number of missing sensors}}
    ```
  - This ensures that infeasible solutions with fewer missing sensors have a higher fitness value.
  - Retaining infeasible individuals helps preserve genetic diversity for future generations.

An individual **X** is considered better than **Y** if:
```math
fitness(X) > fitness(Y)
