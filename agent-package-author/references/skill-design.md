# Skill design

Define one coherent capability and its activation phrases. Put orchestration, conditions, and completion gates in a compact `SKILL.md`; move focused reusable knowledge to references, repeated deterministic operations to scripts, and reusable input material to assets. A simple skill can consist of `SKILL.md` alone.

Load only task-relevant references; when two branches require different knowledge, make the branch observable in an output or decision. Avoid redundant prose and deep reference chains. Scripts declare runtime dependencies and errors. If a script generates artifacts that can be checked independently, define an independent validator rather than trusting the producer.

Design representative success, branch, and negative acceptance cases based on actual behavior. Use the smallest structure that explains and validates the requested workflow. Describe execution requirements separately from structural format conformance.
