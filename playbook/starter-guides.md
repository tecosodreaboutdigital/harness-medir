# Starter guides template

Grounded in: [Part 2](../harness-p2.html#en-dois-controles), section 2, "There are only
two controls": guides are "the controls that anticipate," acting before execution to
raise the odds of getting it right on the first attempt. Every other template in this
playbook is a guide too, `task-contract.md` and `skill-template.md` especially, but
those are shaped by a specific task or skill. These four are not: they are defaults that
hold regardless of task, worth carrying into any new project before a single line of that
project's own work exists.

Copy the block below into your own project's `AGENTS.md` or `CLAUDE.md`. Do not copy
this repository's own `AGENTS.md` or `STANDARDS.md` wholesale: both are written for this
repository's own artefacts (a third-party skill inventory, an HTML publishing pipeline)
and will not transfer. This is the portable part.

---

```
## Default guides

1. Reuse before you build. Prefer a maintained, secure open-source library or a
   supported extension point over new code. Build from scratch only when no
   existing option can meet the requirement efficiently, and say so explicitly
   when you make that call.

2. Match the solution to the requirement, not to what looks impressive. Choose
   the simplest design that satisfies what was actually asked. No speculative
   abstraction, no configuration flag for a use case nobody raised, no
   framework where a function does the job.

3. Verify against the library or API's own current documentation before
   writing code that depends on it, and before any upgrade. Do not cite
   version behaviour from memory, and do not upgrade a pinned dependency
   unless the upgrade is the actual task.

4. A test earns its place by catching a regression that would otherwise ship.
   Write tests that provide real confidence, not padding: no duplicate
   coverage of the same path, no release gate that blocks a merge without
   preventing an actual failure.
```

## Why these four, together

Part 2's own matrix of guides and sensors already names the sensor rule 2 pairs with:
"an evaluation of whether the solution is needlessly complicated for the problem." A
guide that says "do not overengineer" and a sensor that checks for it are the same
discipline applied before and after, exactly the split section 2 argues for.

Rule 3 is the general form of a rule this repository already enforces narrowly, in its
own `AGENTS.md`: before recommending or installing a third-party skill from this
project's curation, fetch the origin and check whether it is still current. That
protocol is the worked example; this is the pattern, generalised to any dependency in
your own project, not just a curated skill. It is also the only one of the four that this
repository enforces on itself. Rules 1, 2 and 4 are not written down in any guide here, so
read them as defaults offered for adoption, not as practice this project has already shown.

## Red flags, stop if you catch yourself thinking

- "It's faster to write this myself than to evaluate three libraries." Evaluating is
  usually the smaller cost, a one-time cost against a maintenance cost that never ends.
- "Let's make this configurable in case we need it differently later." Nobody has asked
  for the other case yet. Add the flag when they do.
- "I already know how this API works." Knowledge goes stale the moment a library ships
  a new major version; the check costs one fetch.
- "More tests can't hurt." A test with no failure mode it catches is a maintenance cost
  with no return, and a slow suite trains people to stop reading it.

## Honest limits

These four guides prevent a known class of failure: over-building, over-abstracting,
working from stale knowledge, over-testing. They say nothing about correctness,
security or your project's own domain: pair them with your own project's guides, not
instead of them. Adapt the wording before you paste it; a rule copied unread is the
same failure mode `playbook/README.md` already warns about.
