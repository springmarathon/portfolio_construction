# Portfolio Construction

A rigorous, ground-up demos in quantitative portfolio construction. Each notebook derives the theory from first principles, then implements it in Python — with the practitioner's perspective on where the math breaks down and what to do about it.

---

## Philosophy

Most portfolio construction courses teach tools. This one teaches the **dependency chain**: why each technique exists, what failure mode it is responding to, and how it connects to the next.

---

## Index

### Module 1 — Markowitz Optimization

The classical mean-variance framework, derived from scratch.

| Notebook | Topic |
|---|---|
| `1.1_efficient_frontier.ipynb` | Lagrangian derivation of the closed-form minimum-variance weights; plotting the efficient frontier; the two-fund theorem |
| `1.2_tangency_portfolio.ipynb` | Adding the risk-free asset; Sharpe-ratio maximization; the Capital Market Line |
| `1.3_mean_variance.ipynb` | Long-only constraints; loss of closed form; CVXPY implementations |
| `1.4_conic_programming.ipynb` | The SOCP/SDP hierarchy; why convexity matters for solvers |

**Key insight:** `w* ∝ Σ⁻¹μ` — the optimizer inverts the covariance matrix to find weights. Small errors in μ and Σ get amplified catastrophically. Everything in modules 2–3 is a response to this.

---

### Module 2 — Advanced Optimization

What to do when classical Markowitz fails or is too restrictive.

| Notebook | Topic |
|---|---|
| `2.1_robust_optimization.ipynb` | Ellipsoidal uncertainty sets; the min-max formulation; SOCP reformulation |
| `2.2_michaud_resampling.ipynb` | Monte Carlo resampling as an empirical alternative to robust optimization |
| `2.3_particle_swarm.ipynb` | Metaheuristic methods for non-convex problems (cardinality constraints, integer lot sizes, non-smooth objectives) |

---

### Module 3 — Estimation Error

The covariance matrix Σ is just as dangerous as μ when estimated from finite data.

| Notebook | Topic |
|---|---|
| `3.1_black_litterman.ipynb` | Bayesian prior from reverse optimization (CAPM equilibrium); blending views with the prior; the conjugate posterior |
| `3.2_ledoit_wolf.ipynb` | Why sample covariance fails (rank deficiency, eigenvalue dispersion, instability); shrinkage toward structured targets |
| `3.3_marchenko_pastur.ipynb` | Random Matrix Theory; the Marchenko-Pastur distribution as a null model; separating signal eigenvalues from noise |

**Key insight:** The aspect ratio q = N/T controls how badly the sample covariance fails. When q → 1, most eigenvalues are statistically indistinguishable from noise. Ledoit-Wolf shrinkage and RMT denoising are the main remedies.

---

### Module 5 — Factor Models

Decomposing risk and return into systematic and idiosyncratic components.

| Notebook | Topic |
|---|---|
| `5.1_statistical_model.ipynb` | Statistical Factor Models; Principal Component Analysis (PCA); Eigen-decomposition of the covariance matrix; Risk decomposition |

**Key insight:** PCA reduces the $O(N^2)$ problem of estimating a covariance matrix to $O(N \times K)$ by identifying the $K$ orthogonal vectors that explain the most variance. This provides a "parsimonious" representation of risk.

---


### Module 6 - Risk Budgeting

| Notebook | Topic |
|---|---|
| `6.1_risk_parity.ipynb` | Euler decomposition of portfolio risk; log-barrier convex formulation; equal risk contribution |

---

## Setup

```bash
# Clone the repo
git clone https://github.com/your-username/portfolio_construction.git
cd portfolio_construction

# Install dependencies
pip install -e .

# Launch Jupyter
jupyter notebook
```

**Dependencies:** `numpy`, `scipy`, `cvxpy`, `matplotlib`, `yfinance`

---

## References

- Markowitz (1952), *Portfolio Selection*, Journal of Finance
- Black & Litterman (1992), *Global Portfolio Optimization*, Financial Analysts Journal
- Ledoit & Wolf (2004), *Honey, I Shrunk the Sample Covariance Matrix*, Journal of Portfolio Management
- Marchenko & Pastur (1967), *Distribution of eigenvalues for some sets of random matrices*
- Michaud (1989), *The Markowitz Optimization Enigma: Is 'Optimized' Optimal?*, Financial Analysts Journal
- López de Prado (2016), *Building Diversified Portfolios that Outperform Out of Sample*, Journal of Portfolio Management
- MOSEK Portfolio Cookbook: https://docs.mosek.com/portfolio-cookbook/index.html