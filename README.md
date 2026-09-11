# PyMOL Plugins

A collection of lightweight PyMOL plugins for structural biology workflows, with a focus on sequence analysis, AlphaFold model organization, and structural alignment.

## Plugins

| Plugin       | Description                                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **afgroups** | Automatically organize AlphaFold models belonging to the same prediction into PyMOL groups.                                        |
| **findseq**  | Search protein sequences in PyMOL objects using Python regular expressions and create selections for each match.                   |
| **malign**   | Perform structural alignment of multiple mobile objects onto a common reference object.                                            |

---

## findseq

findseq searches the sequence of a PyMOL object for a user-defined motif and creates a PyMOL selection for every match.

The motif is interpreted as a Python regular expression using the standard `re` module, allowing both exact sequence searches and more flexible pattern matching.

### Usage

```text
findseq object, motif
```

For example:

```text
findseq ferritin, SSMYA
```

or using a regular expression:

```text
findseq ferritin, SSM..
```

Each match is stored as a separate PyMOL selection:

```text
findseq_1
findseq_2
findseq_3
...
```

This makes it straightforward to visualize or further manipulate residues corresponding to sequence motifs directly in PyMOL.

To keep the creation and accumulation of selection object human friendly, running another findseq command will automatically delete all findseq object previously created.

### Regular expressions

Because motifs are interpreted using Python's `re` module, standard regular-expression syntax can be used.

For example:

```text
findseq protein, G..G
```

matches a glycine followed by any two residues and another glycine.

Character classes can also be used:

```text
findseq protein, [ST]..[KR]
```

See the [Python `re` documentation](https://docs.python.org/3/library/re.html) for the complete regular-expression syntax.

---

## afgroups

afgroups is designed to simplify the organization of AlphaFold models in PyMOL.

AlphaFold predictions are frequently represented by multiple related structures, for example models generated from the same prediction or prediction set. When many such structures are loaded into PyMOL, the object list can quickly become difficult to navigate.

afgroups automatically:

* identifies AlphaFold models belonging to the same prediction;
* groups related models into PyMOL groups;
* generates informative short names automatically;
* reduces manual object-management overhead;
* provides a more structured representation of large AlphaFold datasets.

The resulting PyMOL hierarchy makes it easier to inspect, compare, hide, show, and manipulate related AlphaFold models as a single unit.

### Usage

```text
afgroups
```

---

## malign

malign performs structural alignment of multiple PyMOL objects against a common reference structure.

The plugin takes:

1. a reference object;
2. one or more mobile objects.

Each mobile object is then structurally aligned onto the reference.  

This is particularly useful when comparing multiple predicted or experimentally determined structures against a common structural reference.

Rather than manually running an alignment operation for every object, malign provides a convenient way to perform the same structural-alignment workflow across an entire set of mobile structures.

### Usage 

**align obj2 and obj3 onto obj1 :**

```text
malign obj1, obj2 obj3
```
or 

```text
malign obj1, (obj2, obj3)
```

**align all object onto obj01 :**

```text
malign obj1
```
or

```text
malign obj1, *
```

**align all object with name starting by "obj" onto obj01 :**

```text
malign obj1, obj*
```


---

## Installation

The plugins can be installed through the **PyMOL Plugin Manager** or loaded directly from their Python source files.  
After installation, the corresponding plugin commands can be used directly from the PyMOL command line.

---

## Requirements

* [PyMOL](https://github.com/schrodinger/pymol-open-source)
* Python support as provided by the PyMOL distribution
* Python standard library

The plugins are intended to remain lightweight and rely primarily on PyMOL's native API rather than introducing large external dependencies.
Running and Testing are performed on PyMOL 3.1.0 Open-Source


