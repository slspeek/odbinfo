""" Defines the main datatypes used """
from dataclasses import dataclass


@dataclass
class Column:  # pylint: disable=too-many-instance-attributes
    """ Column properties see:
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Column.html
    """
    name: str
    default_value: str
    description: str
    help: str
    is_auto_increment: bool
    is_nullable: int
    table_name: str
    type_name: str
    precision: str
    scale: str


@dataclass
class Key:
    """ Database key properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Key.html
    """
    name: str
    columns: [str]
    referenced_table: str
    type: int
    delete_rule: int
    update_rule: int


@dataclass
class Table:
    """ Table properties
        www.openoffice.org/api/docs/common/ref/com/sun/star/sdbcx/Table.html
    """
    name: str
    description: str
    keys: [Key]
    columns: [Column]
