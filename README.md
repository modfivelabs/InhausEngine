# InhausEngine
Material driven library that manages InHausTools

---

# File Structure

| Symbol | Description      |
|------- | -----------------|
|  +++++ | Namespace        |
|  +--   | Class            |
|  +~~   | Abstract Class   |
|  +---  | Child Class      |
|  ^     | feature/WIP      |

```
inhaus
+++++
    |
    |
    +-- config
    |   |
    |   +-- UNITS
    |   +-- FAMILY_LIST
    |   +-- CATEGORY_LIST
    |   +-- MATERIAL_PROPERTIES
    |
    |
    +-- document
    |   |
    |   +-- Units
    |   +-- Measurement
    |   +-- Author^
    |   +-- Timestamp^  
    |   |
    |   +~~ DatabaseCommon^
    |   +----- Project^
    |   +----- Warehouse^
    |
    |
    +-- material
    |   |
    |   +~~ MaterialCommon
    |   +--- Extrusion^
    |   +--- Roll^
    |   +--- Sheet
    |   +--- Shutter^
    |   +--- Strip^
    |
    |
    +-- UI : EtoForms^
    |
    |
    +-- utility
        |
        +-- dotNETBase
        +-- Debug

```
