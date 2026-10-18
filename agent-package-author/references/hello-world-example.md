# Hello World design exemplar

The illustrative Project Welcome Pack accepts a project description and `audience=user|contributor`, then writes `WELCOME.md` and `welcome.json` with repeatable bytes. The contributor output ends with a first-change path; the user output ends with a help path. A missing audience or invalid output must be diagnosed. These requirements justify more than a single generic instruction; they do not specify a required tree for other skills.

| Requirement | Illustrative resource decision and reason |
| --- | --- |
| Both audiences receive the same files and manifest fields. | Keep the common workflow in `SKILL.md` and the detailed output contract in one reference; both branches need the same rules. |
| Only one audience's closing section applies per request. | Put contributor and user profiles in separate references with explicit selection conditions; load only the selected profile. If the rules are short and complete in the entry, separate files are unnecessary. |
| Both outputs share approved introductory wording and layout. | Use one Markdown template in `assets/` when the renderer consumes it; a static file without an actual reader adds no value. |
| Repeated input must produce identical bytes. | Use a small renderer in `scripts/` for repeatable file writing and manifest generation, rather than asking the agent to reproduce byte-level behavior from prose. |
| Wrong audience, missing fields, or corrupted output must fail. | Use a separate validator that reads the result independently of the renderer; test both profiles and at least one negative case. |

This is a design decision example, not a mandatory file list. A simple skill with no distinct branch, reusable template or deterministic artifact may need only `SKILL.md`. Create each reference, script or asset only when its selected responsibility has enough substance and an actual caller; preserve the route and shared prerequisites when splitting a subworkflow. Do not copy the example's numbers of scripts, references, fixtures, or tests without an independent need. The separate tests and fixtures are development evidence, not resources that every installed skill loads.
