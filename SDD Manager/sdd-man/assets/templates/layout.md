# Project Layout

<!-- Adapt physical domains to the project. Remove instructional comments from the completed document. -->

## 1. Purpose and authority

Define this document as the canonical description of physical project ownership and distinguish it from behavioral SPEC and construction-order PLAN responsibilities.

## 2. Repository overview

```text
<project-root>/
├── <root file or directory>
└── <root file or directory>
```

Describe only important top-level locations and root-wide conventions.

## 3. Physical ownership domains

| Domain                | Canonical location | Responsibility | Detailed layout node                       |
| --------------------- | ------------------ | -------------- | ------------------------------------------ |
| Documentation         | `<path>`           | `<ownership>`  | `layout/docs.md` or this file              |
| Production source     | `<path>`           | `<ownership>`  | `layout/src.md` or this file               |
| Tests                 | `<path>`           | `<ownership>`  | `layout/tests.md` or this file             |
| Packaging and runtime | `<path>`           | `<ownership>`  | `layout/packaging-runtime.md` or this file |

Create only children justified by substantial independent physical structure.

## 4. Root files and repository-wide conventions

Define important root-level files and conventions genuinely shared across physical domains. Do not use this section as a catch-all.

## 5. Dependency and import boundaries

Define physical constraints that enforce architectural dependency direction, package ownership, visibility, or generated-code boundaries.

## 6. Test and fixture ownership

Define unit, integration, acceptance, helper, and fixture locations and how they correspond to production components.

## 7. Documentation ownership

Define locations and responsibilities of SPEC, PLAN, LAYOUT, ROADMAP, verification mapping, user documentation, and generated documentation.

## 8. Packaging, generated, installation, and runtime artifacts

Define:

- source inputs to packaging;
- build and distribution outputs;
- generated-file ownership;
- ignored disposable artifacts;
- installed package contents and behavior;
- runtime-created files and locations.

## 9. Cross-tree routing

| Architectural area | SPEC owner       | Implementation owner | Test owner    | Principal PLAN phase |
| ------------------ | ---------------- | -------------------- | ------------- | -------------------- |
| `<area>`           | `spec/<node>.md` | `<source path>`      | `<test path>` | `plan/<phase>.md`    |

Keep this table navigational; link to canonical behavior, task, and ownership detail.

## 10. Global physical invariants

Define repository-wide placement, naming, ownership, and dependency invariants.

## 11. Change and refactoring rules

Define when to split or merge layout nodes, how to move canonical ownership, how to update cross-references, and how to preserve generated and runtime artifact policies.
