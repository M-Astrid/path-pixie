## :fairy::sparkles: Cute tool for building content trees

Pre-commit hook example

```yaml
-   repo: https://github.com/M-Astrid/path-pixie
    rev: latest
    hooks:
      - id: path-pixie
        name: path-pixie
        args: [--output, readme.md, --depth, "5", --prefix_type, "emoji"]
```

### Result example

#### 1. Emoji mode
----
*Conjured by [path-pixie](https://github.com/path-pixie)*  
- :file_folder: [knowledge_base](./knowledge_base)  
  - :file_folder: [architecture_design](./knowledge_base/architecture_design)  
    - :file_folder: [gof_patterns](./knowledge_base/architecture_design/gof_patterns)  
      - :page_facing_up: [behavioral](./knowledge_base/architecture_design/gof_patterns/behavioral.md)  
      - :page_facing_up: [creational](./knowledge_base/architecture_design/gof_patterns/creational.md)  
      - :page_facing_up: [structural](./knowledge_base/architecture_design/gof_patterns/structural.md)  
  - :file_folder: [brokers](./knowledge_base/brokers)  
    - :page_facing_up: [rabbitmq](./knowledge_base/brokers/rabbitmq.md)  
  - :file_folder: [devops](./knowledge_base/devops)  
  - :file_folder: [go](./knowledge_base/go)  
    - :page_facing_up: [dependencies](./knowledge_base/go/dependencies.md)  
    - :page_facing_up: [round](./knowledge_base/go/round.md)  
  - :file_folder: [python](./knowledge_base/python)  
    - :file_folder: [async](./knowledge_base/python/async)  
----

#### 2. Bullet mode

----
*Conjured by [path-pixie](https://github.com/path-pixie)*  
- [knowledge_base](./knowledge_base)  
  - [architecture_design](./knowledge_base/architecture_design)  
    - [gof_patterns](./knowledge_base/architecture_design/gof_patterns)  
      - [behavioral](./knowledge_base/architecture_design/gof_patterns/behavioral.md)  
      - [creational](./knowledge_base/architecture_design/gof_patterns/creational.md)  
      - [structural](./knowledge_base/architecture_design/gof_patterns/structural.md)  
  - [brokers](./knowledge_base/brokers)  
    - [rabbitmq](./knowledge_base/brokers/rabbitmq.md)  
  - [devops](./knowledge_base/devops)  
  - [go](./knowledge_base/go)  
    - [dependencies](./knowledge_base/go/dependencies.md)  
    - [round](./knowledge_base/go/round.md)  
  - [python](./knowledge_base/python)  
    - [async](./knowledge_base/python/async)  
----
#### 2. Numbers mode

----
*Conjured by [path-pixie](https://github.com/path-pixie)*  
1. [knowledge_base](./knowledge_base)  
  1. [architecture_design](./knowledge_base/architecture_design)  
    1. [gof_patterns](./knowledge_base/architecture_design/gof_patterns)  
      1. [behavioral](./knowledge_base/architecture_design/gof_patterns/behavioral.md)  
      1. [creational](./knowledge_base/architecture_design/gof_patterns/creational.md)  
      1. [structural](./knowledge_base/architecture_design/gof_patterns/structural.md)  
  1. [brokers](./knowledge_base/brokers)  
    1. [rabbitmq](./knowledge_base/brokers/rabbitmq.md)  
  1. [devops](./knowledge_base/devops)  
  1. [go](./knowledge_base/go)  
    1. [dependencies](./knowledge_base/go/dependencies.md)  
    1. [round](./knowledge_base/go/round.md)  
  1. [python](./knowledge_base/python)  
    1. [async](./knowledge_base/python/async)  
----
