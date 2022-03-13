# odbinfo

## About
When I was working on a fairly complicated LibreOffice Base 
application, I wanted an overview of the components involved
in a diagram expressing their relations,
so I started writing an extension called
[DBDeps](https://github.com/slspeek/dbdeps).
Then I came across
[BaseDocumenter](https://extensions.libreoffice.org/en/extensions/show/basedocumenter-to-document-your-base-applications)
written by Jean Pierre Ledure, and I started adding 
graphviz diagram functionality to it
(unfinished project [BaseDocumenter2Dot](https://github.com/slspeek/BaseDocumenter2Dot)).
When I wanted to add more functionality, I wanted to work with my own code in my language
of choice, so two years ago I decided to write the BaseDocumenter functionality
from scratch in python.

## Audience
People making applications with LibreOffice Base using forms, reports,
mail merge documents and macros.


## What it does
It generates a html-report of your libreoffice database file and related text documents. It includes a graphviz diagram of all the components that displays
the application structure of tables, views, queries, forms, reports, modules and referring
odt and ott files. It shows dependency and parent-child relationships.

You can use this information to get an overview of your application and use 
this to your advantage working on it. It is handy when you want to rename
a component, because you can easily inspect the uses.

## Installation
Get the odbinfo.oxt from ... (Coming soon)

Install the odbinfo.oxt file in LibreOffice.

ODBInfo needs:
1. [wget](https://www.gnu.org/software/wget/)
2. [gohugo](https://gohugo.io/)
3. [graphviz](https://graphviz.org/)

If you are on debian-based linux run:
```bash
sudo apt install wget hugo graphviz
```
If you are on windows or mac, open a datebase in LibreOffice and use the "Verify installation of required components.." menu item from
the "ODBInfo" menu. It displays a dialog with links to the required software.

Press the "Run diagnostics" button to see what may be missing. If somethings missing
click on the link for the installation help on that component. Rerun after you installed a piece
of software, until all signs are green.

## Usage
If you have the required software installed, you can use the menuitem "Make database report" from the
"ODBInfo" menu. Press "Start" on the dialog the make a report.

## Configuration
Most users will not have to do configuration to use the extension.
It should run out of the box. 

Configuration is done via a [YAML](https://www.w3schools.io/file/yaml-arrays/)
file config.yaml in the .odbinfo folder in the user home directory. After the first run
a default configuration is written in this location.


The default configuration with some help comments is shown below:
```yaml
general:
  # If you want to place the report on a webserver you have 
  # please supply the url (Not needed for basic use).
  base_url: http://odbinfo.org/
  # If null the .odbinfo folder in the parent of the database
  # document is used
  output_dir: null
graph:
  # Multiple uses of the same object by one specific object are
  # merged when this option is set to true
  collapse_multiple_uses: true
  parent_edge_attrs:
    arrowhead: none
    arrowtail: diamond
    color: '#495C49'
    dir: back
    style: dashed
  relation_attr: # Omitted for brevity
  # Only shows controls with a command or an eventlistener
  # if set to true
  relevant_controls: true
  type_attrs: # Omitted for brevity
  # Types exclude from the diagram (to keep it smal)
  # you can remove items you do want see in the diagram and add items
  # you do not want to see them in the diagram
  user_excludes:
  - key
  - index
  - eventlistener
  - library
  - querycolumn
  - column
  - pythonlibrary
  - pythonmodule
  - databasedisplay
# Name of the report, defaults to the database filename without the extension.
name: ''
textdocuments:
  # database registration id in LibreOffice to search for in the text documents,
  # defaults to the database filename without the extension.
  db_registration_id: null
  # Leaving this null searches the parent directory of the database document
  # and its subdirectories for related text documents.
  # Set it to [] to skip searching for text documents or templates altogether.
  search_locations: null

```

## Known issues
May take a while to run if the database document file is in a big directory due
to the search of related text documents.  

The BASIC parsing does not recorgnize BASIC class modules and method invocations.

## Bugs
If you find a bug please submit an issue.

## Building
See [development instructions](doc/development.md)