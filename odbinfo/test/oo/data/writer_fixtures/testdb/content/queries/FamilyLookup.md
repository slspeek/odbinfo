---
columns:
- autoincrement: false
  issigned: false
  name: Name
  nullable: Nullable
  precision: 2147483647
  readonly: false
  scale: 0
  tablename: Family
  title: Family.Name
  typename: VARCHAR
  writable: true
- autoincrement: false
  issigned: true
  name: FamilyID
  nullable: No_Nulls
  precision: 10
  readonly: false
  scale: 0
  tablename: Family
  title: Family.FamilyID
  typename: INTEGER
  writable: true
command: "SELECT \"Name\",\n       \"FamilyID\"\nFROM   \"Family\""
name: FamilyLookup
table_tokens:
- column: 7
  hidden: false
  index: 18
  line: 3
  link: []
  text: '"Family"'
  type: 184
---
