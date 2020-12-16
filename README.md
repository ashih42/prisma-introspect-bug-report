# Prisma Bug Report Example Repo

This bug report repo uses Python/Sqlalchemy to define tables in a Sqlite database, and then runs `prisma introspect` together with an existing schema in `prisma/schema.prisma`.

The bug is that `prisma introspect` consistently retains some, but drops other, `@relation` custom names defined in the existing `prisma/schema.prisma`.

## Versions

* Node 14.2.0
* Prisma 2.13.0
* Python 3.8.0

## Instruction

Install node and python3 dependencies.

```
yarn install-dependencies
```

Create database and run `prisma introspect`.

```
yarn init-db
```

## Models and Relations

* 1 `Workspace` : many `Project`
* many `User` : many `Workspace` (in association table `WorkspaceMember`)
* many `User` : many `Project` (in association table `ProjectMember`)

## Result Analysis

Now `prisma introspect` has overwritten the old input `prisma/schema.prisma` and replaced some `@relation` names with default names.  

For convenience, `prisma/INPUT_schema.prisma` is a copy of the input `prisma/schema.prisma` where all custom names were defined.  Diffing these input and output .prisma files shows how `prisma introspect` treated these custom names:

User:
* ❌ `my_project_members`  (dropped) -> `ProjectMember` (default name)
* ✔️ `my_workspace_members`  (retained)

Workspace:
* ✔️ `these_projects`  (retained)
* ❌ `these_workspace_members`  (dropped) -> `WorkspaceMember` (default name)

WorkspaceMember:
* ❌ `the_user`  (dropped) -> `User` (defaul name)
* ❌ `the_workspace`  (dropped) -> `Workspace` (default name)

Project:
* ✔️ `parent_workspace`  (retained)
* ✔️ `these_project_members`  (retained)

ProjectMember:
* ❌ `the_project`  (dropped) -> `Project` (default name)
* ✔️ `the_user`  (retained)
