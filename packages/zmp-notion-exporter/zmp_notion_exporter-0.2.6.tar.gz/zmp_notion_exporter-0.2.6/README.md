# zmp-notion-exporter

![Platform Badge](https://img.shields.io/badge/platform-zmp-red)
![Component Badge](https://img.shields.io/badge/component-exporter-red)
![CI Badge](https://img.shields.io/badge/ci-github_action-green)
![License Badge](https://img.shields.io/badge/license-MIT-green)
![PyPI - Version](https://img.shields.io/pypi/v/zmp-notion-exporter)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/zmp-notion-exporter)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zmp-notion-exporter)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/zmp-notion-exporter)

<!-- ![Language Badge](https://img.shields.io/badge/language-python-blue)
![Version Badge](https://img.shields.io/badge/version-^3.12-blue) -->

The zmp-notion-expoter is the utility library to export the Mardown, HTML and PDF files from the notion pages.

# Goals
This is the utility project for the Cloud Z MP manual system

# Examples
## Export to markdown
include all sub pages of the root notion page
```python
import logging
import os
import time

from dotenv import load_dotenv

from zmp_notion_exporter import NotionPageExporter, extract_notion_page_id

load_dotenv()

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logging.getLogger("zmp_notion_exporter.page_exporter").setLevel(logging.INFO)
logging.getLogger("httpcore").setLevel(logging.INFO)


notion_token = os.environ.get("NOTION_TOKEN", "")

if not notion_token:
    raise ValueError("NOTION_TOKEN is not set")


root_page_zcp_url = (
    "https://www.notion.so/cloudzcp/Cloud-Z-CP-19ab7135d33b803b8ea7ff3e366f707d?pvs=4"
)]

output_dir = "/Users/kks/IdeaProjects/aiops/zmp-doccuments-ui"

exporter = NotionPageExporter(
    notion_token=notion_token,
    root_page_id=extract_notion_page_id(root_page_zcp_url),
    root_output_dir=output_dir,
)

start_time = time.time()

path = exporter.markdownx(include_subpages=True)

print(path)

docs_node, static_image_node = exporter.get_output_nodes()
docs_node.print_pretty(include_leaf_node=True)
static_image_node.print_pretty(include_leaf_node=False)


end_time = time.time()

print("-" * 100)
print(f"Export took {end_time - start_time:.2f} seconds")
print("-" * 100)


# Output sample
.output
.output/
└── docs/
    └── cloud-z-cp/
        └── introduction/
            └── product-overview
            └── glossary
            └── release-notes
            └── application-modernization
            └── cloud-application-architecture
        └── introduction-2/
            └── release-notes-2
            └── release-notes-1
.output/
└── static/
    └── img/
        └── cloud-z-cp/
            └── introduction/
            └── introduction-2/
----------------------------------------------------------------------------------------------------
Export took 27.57 seconds
----------------------------------------------------------------------------------------------------

# double check using the os command
$ tree .output
├── docs
│   └── cloud-z-cp
│       ├── _category_.json
│       ├── introduction
│       │   ├── _category_.json
│       │   ├── application-modernization.mdx
│       │   ├── cloud-application-architecture.mdx
│       │   ├── glossary.mdx
│       │   ├── product-overview.mdx
│       │   └── release-notes.mdx
│       └── introduction-2
│           ├── _category_.json
│           ├── release-notes-1.mdx
│           └── release-notes-2.mdx
└── static
    └── img
        └── cloud-z-cp
            ├── introduction
            │   ├── 19fb7135-d33b-800a-8e85-f4be38bdeb0d.png
            │   ├── 19fb7135-d33b-8010-b82a-c1a9e182a45d.png
            │   ├── 19fb7135-d33b-8029-9cb0-e38b61df0c4b.png
            │   ├── 19fb7135-d33b-8044-b4b0-dd8150f553d0.png
            │   ├── 19fb7135-d33b-8092-893e-e2e92070f50b.png
            │   ├── 19fb7135-d33b-80a2-960b-e6d91fb708ba.png
            │   └── 19fb7135-d33b-80dc-97ed-c9960713e0c3.png
            └── introduction-2

9 directories, 17 files
```

## Export to markdown files of the specific page
```python
import logging
import os
import time

from dotenv import load_dotenv

from zmp_notion_exporter import NotionPageExporter, extract_notion_page_id

load_dotenv()

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logging.getLogger("zmp_notion_exporter.page_exporter").setLevel(logging.INFO)
logging.getLogger("httpcore").setLevel(logging.INFO)


notion_token = os.environ.get("NOTION_TOKEN", "")

if not notion_token:
    raise ValueError("NOTION_TOKEN is not set")


root_page_zcp_url = (
    "https://www.notion.so/cloudzcp/Cloud-Z-CP-19ab7135d33b803b8ea7ff3e366f707d?pvs=4"
)

target_page_urls = [
    "https://www.notion.so/cloudzcp/Getting-Started-Sample-Page-193b7135d33b80e0954fc9e52d94291a?pvs=4",  # Getting Started Sample Page
]

output_dir = ".output"

exporter = NotionPageExporter(
    notion_token=notion_token,
    root_page_id=extract_notion_page_id(root_page_zcp_url),
    root_output_dir=output_dir,
)

start_time = time.time()
path = exporter.markdownx(
    page_id=extract_notion_page_id(target_page_urls[-1]), include_subpages=True
)

# Output sample
.output/docs/cloud-z-cp/introduction/release-notes
.output/
└── docs/
    └── cloud-z-cp/
        └── introduction/
            └── product-overview
            └── glossary
            └── release-notes
            └── application-modernization
            └── cloud-application-architecture
        └── introduction-2/
            └── release-notes-2
            └── release-notes-1
.output/
└── static/
    └── img/
        └── cloud-z-cp/
            └── introduction/
            └── introduction-2/
----------------------------------------------------------------------------------------------------
Export took 10.21 seconds
----------------------------------------------------------------------------------------------------

# double check using the os command
$ tree .output
.output
├── docs
│   └── cloud-z-cp
│       ├── introduction
│       │   └── release-notes.mdx
│       └── introduction-2
└── static
    └── img
        └── cloud-z-cp
            ├── introduction
            └── introduction-2

9 directories, 1 file
```
