# Selfish Mining as a Signaling Game

Python simulation engine accompanying the thesis *"Game-Theoretic Approach to
Selfish Mining in Blockchain Networks."* Implements the signaling-game model
from Chapter 4, validated against Gambit's equilibrium solver in Chapter 6.

## Structure
- `config.py` — model parameters (R, α, c, κ, γ, q, ε, TAU_W)
- `models/` — Blockchain ledger and Block objects
- `agents/` — SenderPool and NetworkReceiver
- `game/signalling.py` — payoff functions and Bayesian belief updating
- `simulation/engine.py` — main round-based execution loop

## Known limitations
See §7.5 of the thesis — in particular, `resolve_fork()` in `models/chain.py`
has a documented limitation affecting the Selfish Pool Revenue Share and Main
Chain Canonical Blocks statistics; Mean Sender Utility and Detection Accuracy
are unaffected.

## Run
python main.py
