# Project Agent Instructions

## Git & Worktree Policy

- `main` is stable; `integration` accumulates verified changes.
- All agent worktrees live in `.worktrees/<task-name>` on `agent/<task-name>` branches.
- Start from the latest appropriate **local** branch (`main`, `integration`, or a dependent task branch). Preserve uncommitted changes.
- One writing agent per worktree; isolate parallel tasks.
- Serialize merges into `integration`; resolve conflicts and revalidate before merging.
- Promote `integration` to `main` only after required tests and review pass.
- Automatically clean up merged branches/worktrees; preserve dirty, unfinished, or failed work for recovery.
- Never discard changes, force-push, bypass checks, or overwrite another agent's work.
- Manage Git lifecycle autonomously without user intervention.
