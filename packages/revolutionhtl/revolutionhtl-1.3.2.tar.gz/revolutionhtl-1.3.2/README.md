![REvolutionH-tl logo.](https://gitlab.com/jarr.tecn/revolutionh-tl/-/raw/master/docs/images/Logo_horizontal.png)

REvolutionH-tl is a powerful Python tool designed for evolutionary analysis tasks. It provides a comprehensive set of features for orthogroup analysis, gene tree reconstruction, species tree reconstruction, and reconciliation of gene and species trees.

---

José Antonio Ramírez-Rafael •  Annachiara Korchmaros • Katia Aviña-Padilla • Alitzel López Sánchez • Andrea Arlette España • Marc Hellmuth • Peter F. Stadler • Maribel Hernandez-Rosales

---

This guide will walk you through the installation, usage, and key functionalities of REvolutionH-tl.

<img src="https://gitlab.com/jarr.tecn/revolutionh-tl/-/raw/master/docs/images/revolution_diagram.png" alt="pipeline" style="zoom:25%;" />



# Installation

To get started with REvolutionH-tl, you can easily install it using [pip](https://pip.pypa.io/en/stable/installation/):

```bash
pip install revolutionhtl
```

**Requirements**

Make sure you have the following prerequisites installed:

[Python >=3.7 ](https://www.python.org/)

To perform sequence alignments, you'll also need to install Diamond or BLAST. You can download the Diamond executable from [here](https://github.com/bbuchfink/diamond) or using command line as follows:

```bash
wget http://github.com/bbuchfink/diamond/releases/download/v2.1.8/diamond-linux64.tar.gz
tar xzf diamond-linux64.tar.gz
```

To install BLAST follow these instructions: [Unix](https://www.metagenomics.wiki/tools/blast/install) / [Windows](https://www.ncbi.nlm.nih.gov/books/NBK52637/). Or use the command line:

```bash
sudo apt-get install ncbi-blast+
```

# Synopsis

REvolutionH-tl is a command-line tool, and it can be used with the following syntax:

```bash
python -m revolutionhtl <arguments>
```

In addition, use the commands for visualization of results:

```bash
python -m revolutionhtl.plot_summary <arguments>
python -m revolutionhtl.plot_reconciliation <arguments>
```



Let's delve into the steps of the program, the required arguments, and output files:

## General overview

REvolutionH-tl methodology is divided in 5 steps. You can run all of them in a row by providing a directory containing fasta files (use argument `-F <directory>`). Furthermore, if you want to run a specific step using precomputed files, you can use the argument `-steps <step list>` together with the arguments required for such a step.

REvolutionH-tl assumes you have a fasta file for each species in your analysis. Such a file contains the list of genes or proteins present in the organism. By default, REvolutionH-tl expects peptide sequences (proteins) and aligns them using Diamond. In the next sections, we present a detailed description of the input/output files of each step, parameters, and examples.

### Steps

1. **Alignment Hits Computation.** First, REvolutionH-tl runs a sequence aligner to obtain alignment hits and statistics like bit-score and e-value.

   Required argument: `-F <directory containing fasta files>`

   Output: directory `_alignment_all_vs_all/`

2. **Best Hit & Orthogroup Selection.** Best hits are the putative closest evolutionary-related genes across species, and orthogroups are a collection of genes sharing a common ancestor.

   Input argument: `-alignment_h <directory containig aligment hit files>`.

   Output files: `.best_hits.tsv`, `.orthogroups.tsv`, and optionally `.singletones.tsv` (using `-singletones` flag). A singleton is a gene lacking homologous.

3. **Gene Tree Reconstruction, Best Matches, and Orthology Assignment.** Gene trees are reconstructed from the hits. Best matches are the closest evolutionary-related genes across species based on gene tree topology. Two genes are orthologous if they were conserved after a speciation process.

   Required argument: `-best_h <.tsv file containing best hits>`.

   Output files: `.gene_trees.tsv`, `.orthologs.tsv`, `.best_matches.tsv`.

4. **Species tree reconstruction.** Species trees are obtained as a consensus of the speciation events in the gene trees.

   Required argument: `-T <.tsv file containig gene trees>`

   Output file: `.species_tree.tsv`

5. **Tree reconciliation.** Tree reconciliation depicts the evolution of genes across existing and ancestral species, it is represented as a gene tree embedded into a species tree.

   Required arguments:

   `-T <.tsv file containig gene trees>`

   `-S <single-line file containing species tree>`

   Output files: `.reconciliation.tsv`, `.corrected_trees.tsv`, `.labeled_species_tree.nhxx`

### Arguments

<details>
  <summary> <b>Input data</b> (Click to expand)  </summary> 
  <b>-h </b> Show the full help message and exit. <br/> <br/>
  <b>-steps</b> List of steps to run (default: 1 2 3 4 5).  <br/> <br/>
  <b>-F </b> [str | Input for step 1] Directory containing fasta files.  <br/> <br/>
  <b>-alignment_h</b> [str | Input for step 2] Directory containing alignment hits. <br/> <br/>
  <b>-best_h</b> [str | Input for step 3] .tsv file containing best hits. <br/> <br/>
  <b>-T</b> [str | Input for steps 4 and 5] .tsv file containing gene trees in nhxx format. <br/> <br/>
  <b>-S</b> [str | Input for step 5] .nhxx file containing a species tree.<br/> <br/>
</details>
<details>
  <summary> <b>File names</b> (Click to expand)  </summary> 
  <b>-o</b> [str | Default: tl_project] Prefix for output files.<br/><br/>
  <b>-fext</b> [str | Default: .fa] Extesion for fasta files.<br/><br/>
  <b>-singletones</b> [flag | Prameter for step 2] Use to print singletons, i.e. genes that weren't assigned to an orthogroup. <br/><br/>
  <b>-og</b> [str | Default: OG] Column specifying orthogroup ID in input and output .tsv files.<br/><br/>
  <b>-Nm</b> [int | Default: 2000] Maximum number of genes in a orthogroup, bigger orthogroups are splitted. If 0, no orthogroup is splitted. <br/><br/>
  <b>-k</b> [int | Default: 100] Range in the numer of genes of orthogroups procesed in batch: first those with less than k genes, then less that 2k. then  less than 3k, and so on. <br/><br/>
  <b>-S_attr</b> [str | Default: ;] Attribute delimiter in the input .nhxx file (Input of step 5). <br/><br/>
</details>
<details>
  <summary> <b>Algorithm parameters</b> (Click to expand)  </summary> 
  <b>-aligner</b> [str | Parameter for step 1 | Default: diamond] Command or path to the program for computation of aligment hits. Supported: diamond, blastn, blastp. <br/><br/>
  <b>-v</b> [flag | Parameter for step 1 ] Use to display diamond messages. <br/><br/>
  <b>-e</b> [float | Parameter for step 1 | Default: 1e-05] Maximum evalue required to consider significant an aligment hit. <br/><br/>
  <b>-m_command</b> [str | Parameter for step 1 | Default: makeblastdb] BLAST command or path to the BLAST program for database creation. <br/><br/>
  <b>-id</b> [float | Parameter for step 1 | Default: 25] Minimum percentage of identity required to report an alignment hit. <br/><br/>
  <b>-cov</b> [float | Parameter for step 1 | Default: 50] Minimum percentage of query coverture required to report an alignment hit. <br/><br/>
  <b>-k_hits</b> [int | Parameter for step 1 | Default: 100] Maximum number of alignment hits per gene againist a fixed species. <br/><br/>
  <b>-bh_heuristic</b> [str | Parameter for step 2 | Default: target] Indicates how to normalize bit-score. Normalize by sequence lenght: query, target, alignment, smallest. No normalization: row. <br/><br/>
  <b>-f</b> [float | Parameter for step 2 | Defualt: 0.95] Number between 0 and 1. Defines the adaptative threshhold for best-hit selection as: f*max_bit_score. <br/><br/>
  <b>-bmg_h</b> [str | Parameter for step 3 | Defult: Louvain] Comunity detection method for MaxConsistentTriples heuristic. Options: Mincut, BPMF, Karger, Greedy, Gradient_Walk, Louvain, Louvain_Obj. <br/><br/>
  <b>-no_binary_R</b> [flag | Parameter for step 3 ] Use to avoid the usage of binary triples from best-hit graph. <br/><br/>
  <b>-f_bT</b> [flag | Parameter for step 3 ] Use to force gene trees to be binary. <br/><br/>
  <b>-T_no_db</b> [flag | Parameter for step 3 ] Use to avoid running build twice in the MaxConsistentTriples heuristic. <br/><br/>
  <b>-stree_h</b> [str | Parameter for step 4 | Default: louvain_weight] Comunity detection method for MaxConsistentTriples heuristic. Options: naive, louvain, mincut, louvain_weight. <br/><br/>
  <b>-streeh_repeats</b> [int | Parameter for step 4 | Default: 4] Specifies how many times run the MaxConsistentTriples heuristic. <br/><br/>
  <b>-streeh_b</b> [flag | Parameter for step 4] Use to force specis tree to be binary. <br/><br/>
  <b>-streeh_ndb</b> [flag | Parameter for step 4] Use to avoid running build twice in the MaxConsistentTriples heuristic. <br/><br/>
  <b>-n_edit_T</b> [flag | Prameter for step 5] Use to avoid editing of inconsistent gene trees. <br/><br/>
</details>



### Additional Resources

For an **example with data and practical usage examples**, click [here](https://gitlab.com/jarr.tecn/revolutionh-tl/-/blob/master/docs/example.md). For a detailed description of the theoretical background of this tool see reference [1].

By following these steps and using REvolutionH-tl, you can conduct comprehensive evolutionary analysis tasks, including orthogroup selection, gene tree reconstruction, species tree reconstruction, and reconciliation, all in one powerful Python tool. Go to the section "Biological Relevance" for applications.

# Visualization

After running an analysis using the command bellow, you can generate visualizations of the results using the commands `python -m revolutionhtl.plot_summary <arguments>` and `python -m revolutionhtl.plot_reconciliation <arguments>`. An example:

```bash
python -m revolutionhtl -F fastas/ # Run an standar analysis of revolutionhtl
python -m revolutionhtl.plot_summary # Summarize inferred evolutionary histories
python -m revolutionhtl.plot_reconciliation <orthogroup IDs> # Visualize the reconciliation of an orthogroup.

```

# File format overview

### Forbidden characters

 Please avoid the usage of the following characters in the name of the species, genes, or other parameters of the tool: ';', '/'.

### NHX format for trees

[NHX format](http://www.phylosoft.org/NHX/) is a generalization of the Newick format. The box below contains a species tree with four species as leafs.

```bash
((Corynebacterium_felinum,Citricoccus_zhacaiensis),(Bacillus_thuringiensis,Sutcliffiella_horikoshii));
```

**Log file** Every time you run REvolutionH-tl, the program writes in the file `tl_project_log.txt` the parameters used to run the program, as well as the time and progress.

**Fastas directory** Fasta files are required for step 1. Additionally, fasta files are also required when you set the flag `-singletons`. Specify the fastas directory using the attribute `-F <directory>`.

You must have a fasta file for each species in your analysis (At least 2 species).

The name of each file has to follow the format `<species name>.fa`. Please avoid the usage of forbidden characters in the name of the species. By default, REvolutionH-tl searches for files with the extension ".fa", but you can change the extension using the attribute `-fext <extension>`.

NOTE: each gene in your analysis must have a unique identifier. Duplicated identifiers will raise a problematic behavior of REvolutionH-tl even if those genes belong to different species. Remember to avoid forbbiden characters in your identifiers.

**Alignment hits directory** This directory is the output of step 1, it has the suffix `_alignment_all_vs_all/`.

The alignment hits directory is required for step 2. Specify it using the attribute `-alignment_h <directory>`.

For each pair of fastas, you must have two files of alignment hits; from species one to species two and from species two to species one. The name of each file has to follow the format `<species_one>.vs.<species_two>.alignment_hits`.

REvolutionH-tl requires the alignment hits in tabular form with no headers. Each row of this table describes an alignment hit throughout seven columns. Below we describe those columns in the same way as Diamond and BLAST:

- qseqid: identifier of the query sequence
- sseqid: identifier of the target sequence
- qlen: length of the query sequence
- slen: length of the target sequence
- length: length of the alignment of the query sequence against the target sequence.
- bitscore: alignment statistic reflecting the degree of similarity of the target to the query sequence.
- evalue: alignment statistic reflecting significance. It is the number of subject sequences that can be expected to be retrieved from the database that have a bit score equal to or greater than the one calculated from the alignment of the query and subject sequence

**Orthogroups file** This file is an output of step 2, it has the suffix `.orthogroups.tsv`.

Orthogroups are stored in a tabular format (.tsv file). Each row in this file represents one orthogroup. The first column assigns a unique identifier for each orthogroup. The number in the second column indicates the number of genes, and the third column shows the number of species represented in the orthogroup. The rest of the columns correspond to the species in your analysis, each of those columns contains the genes present in the orthogroup. If there is more than one gene per species, they are separated using a comma (',').

**Best hits file** This file is an output of step 2, it has the suffix `.best_hits.tsv`.

Best hits are required as input for step 3. You can provide them using the argument `-best_h <.tsv file>`.

Best hits should be provided in a tabular form (.tsv file). Each row in this file describes a best hit. The headers of this file are:

- OG: identifier of the orthogroup containing the genes of the hit.
- Query_species: species of the query gene.
- Target_species: species of the target gene
- Query_accession: identifier of the query gene.
- Target_accession: identifier of the target gene.
- Normalized_bit_score: normalized bit-score of the corresponding alignment hit.

**Singleton file** This file is an output of step 2, it has the suffix `.singletons.tsv`.

Singletons are stored in a two-column .tsv file. The first column contains gene identifiers, while the second indicates the fasta file containing the singleton gene.

**Gene trees file** This file is an output of step 3, it has the suffix `.gene_trees.tsv`.

Gene trees are the input of steps 4 and 5. You can provide them using the argument `-T <.tsv file>`.

This file is a table where each row contains the information for one gene tree. The first column specifies the orthogroup associated with the genes in the leaves of the gene tree, while the second column contains the gene tree in nhxx format.

The leaves of the gene tree are gene identifiers and have the attribute "species". The species of the genes must be consistent with the species tree. The inner nodes of the gene tree are associated with evolutionary events: the letter "S" indicates a speciation event, while "D" stands for gene duplication.

**Orthologs file** This file is an output of step 3, it has the suffix `.orthologs.tsv`.

Orthology is stored in a tabular form. Each row of this table contains an orthology relation, i.e. the information of a pair of orthologous genes, described in 6 columns:

- a, b: pair of orthologous genes
- species_a, species_b: species corresponding to the orthologous genes.
- OG: identifier of the orthogroup containing the orthologous genes.
- Normalized_bit_score: normalized bit-score associated with the best hits between genes a and b. If there is not a best hit, we place the symbol "*".

**Best matches file**

This file is an output of step 3, it has the suffix `.best_matches.tsv`.

Best matches are stored in a tabular form. Each row of this table contains the information of a best-match throughout 5 columns:

- OG: identifier of the orthogroup containing the best match.
- Query_accession: query gene.
- Query_species: species of the query gene.
- Target_accession: a best match of the query gene in the target species.
- Target_species: species of the target gene.

**Species tree file** This file is an output of step 4, it has the suffix `.species_tree.tsv`.

The species tree is required for step 5. You can provide it using the argument `-S <.nhxx file>`.

The species tree has species as leaves. The name of the species must be consistent with the species of the genes in the gene trees.

**Corrected tree file** This file is a result of step 5, it has the suffix `.corrected_trees.tsv`.

Some gene trees in the gene tree file are not consistent with the species tree, and then it is impossible to find a reconciliation. To solve this problem the trees are edited by pruning leaves.

This file is a table where each row contains the information for one gene tree. The first column specifies the orthogroup associated with the genes in the leaves of the gene tree, the second column contains the corrected gene tree in nhxx format, and the last column shows the size of the inconsistency measured in "color triples" (see reference [1]). If this number is zero, then the corrected tree was not edited.

**Labeled species tree file** This file is an output of step 5, it has the suffix `.labeled_species_tree.nhxx`.

This tree is the same as the one in the "Species tree file", but it includes the extra attribute "node_id", which specifies a unique identifier for each node of the tree.

**Reconciliation file** This file is an output of step 5, it has the suffix `.reconciliation.tsv`.

Reconciliation of gene trees against the species tree is output in tabular format. Each row of the table contains the reconciliation of one gene tree. The reconciliation is described using 5 columns:

- OG: orthogroup associated with the genes in the leaves of the gene tree.
- tree: reconciled gene tree.
- reconciliation_map: a relation of the nodes of the gene tree with the nodes in the species tree.

The trees in this file are similar to those in the "gene trees file", with three additional characteristics: first, they may be more resolved than the original trees, second, they have the attribute "node_id" which specifies a unique identifier for each node of the tree, and third, some leaves of the tree have the label "X", representing a gene loss event.

To represent a reconciliation map REvolutionH-tl uses a comma-separated list, where each element takes the form x:y. Here x is a node ID in the gene tree, and y is a node ID in the species tree. 

# Detailed pipeline description

## Step 1 | Alignment hits

We perform sequence alignment for homology detection. Additionally, we use alignment statistics for approximation of evolutionary relatedness. To perform alignments we use Diamond and BLAST. Se references [2,3]

## Step 2 | Best hit & orthogroup selection

### Best hits

For every gene in the analysis, step 1 aims to recover all the most similar genes based on sequence similarity. This procedure uses the normalized bit-score of the alignment hits and an adaptive threshold to create a subselection of alignment hits. We call *best hits* to this subselection. See section 3.1.2 of reference [1] for a deeper explanation of this analysis.

A best hit (x-->y) is a directed relationship from one gene x to gene y, where the former is called *query* and the latter is called *target*.

### Orthogroups

An orthogroup is a collection of homologous genes, which means that they appear as leaves of the same gene tree. We say that two genes are in the same orthogroup if we can construct a path of best hits connecting them.

## Step 3 | Gene tree reconstruction & orthology

### Gene trees

The inner nodes of the gene tree are labeled as speciation events with the letter "S", or as duplication events with the letter "D". The leaves of the gene tree represent the genes of the orthogroup.

The gene trees output here are the least resolved trees that can be reconstructed from the best hits. If you want fully resolved trees, look at the output of step 5.

### Orthology

Two genes are orthologous if they diverge at a speciation event.

Orthology is a undirected relation, so saying that "x gene is orthologous of y gene" is the same as saying that "gene y is orthologous of gene x".

### Best matches

For each gene in the gene trees, we return the best matches, i.e. the most evolutionarily related genes in other species. Best matches are defined concerning a gene tree. See section 3.1.1 [1] for a deeper explanation.

A best match (x-->y) is a directed relationship from gene "x" to gene "y". The main difference with "best hits" in the previous step is that a best match is consistent with a gene tree, while a best hit is based on the bit-score of sequence alignments.

### Step 3 | Species tree reconstruction

We reconstruct a species tree as a consensus of all the gene trees obtained in step 2, the procedure is detailed in section 3.1.4 of [1].

### Step 4 | Tree reconciliation

The reconciliation shows how genes evolved across species and time. This can be represented as a map of the nodes in the gene tree to nodes and edges of the species tree. The figure below shows a reconciliation. On the left side, the nodes of a gene tree are mapped to the species tree using arrows. On the right side, the reconciliation is shown explicitly by drawing the gene tree inside of the species tree. Red circles correspond to speciation events, while blue squares correspond to gene duplication. Note that duplication nodes in the gene tree are mapped to edges of the species tree, on the other hand, speciation nodes of the gene tree are mapped to nodes of the species tree.

![Reconciliation](https://gitlab.com/jarr.tecn/revolutionh-tl/-/raw/master/docs/images/recon_example.png?ref_type=heads)

To represent a reconciliation map REvolutionH-tl uses a comma-separated list, where each element takes the form `x:y`, where `x` is a node ID in the gene tree, and `y` is a node ID in the species tree. In the example of the figure above we have the reconciliation map `0:0,1:1,2:1`. As in the example of the figure, the reconciled gene tree can include extra speciation events and gene loss. In section 3.1.5 of [1], the procedure to compute this map is detailed.

# Biological Relevance

RevolutionH-tl is a versatile tool that facilitates various aspects of evolutionary and comparative genomics research. Its outputs are useful for advancing our understanding of the evolution and functional roles of genes across different species. It has several biological applications:

1. **Phylogenetics**: RevolutionH-tl aids in constructing accurate gene and species trees, allowing researchers to infer the evolutionary history of genes and species. This information is fundamental for understanding the relationships among different organisms.
2. **Functional Genomics**: By identifying orthogroups and best hits, RevolutionH-tl helps researchers discover homologous genes with similar functions. This can be invaluable for functional annotation and comparative genomics studies.
3. **Evolutionary Genomics**: Researchers can use RevolutionH-tl to explore gene duplication and speciation events. This information sheds light on the evolutionary processes that have shaped gene families and species.
4. **Biological Databases**: The output files from RevolutionH-tl can be integrated into biological databases to enhance the annotation of genes and improve our understanding of gene and species relationships.
5. **Phylogenomic Analyses**: RevolutionH-tl's ability to reconcile gene trees with species trees provides insights into the complex interplay between gene duplication, loss, and speciation. It is invaluable for conducting phylogenomic analyses.
6. **Comparative Genomics**: Researchers can compare the output from RevolutionH-tl across different species to identify conserved genes and understand how specific genes have evolved in different lineages.
7. **Functional Inference**: The orthologous relationships identified by RevolutionH-tl can be used to infer gene function by transferring functional annotations from well-characterized genes to orthologs.

# References

[1] José Antonio Ramírez-Rafael, Annachiara Korchmaros, Katia Aviña-Padilla, Maribel Hernandez-Rosales (2023) *REvolutionH-tl : a graph-based tool to estimate gene family evolutionary scenarios* [in progress].

[2] Ramirez-Rafael J. A. (2023). *REvolutionH-tl: a tool for the fast reconstruction of evolutionary histories using graph theory* [Master dissertation, Cinvestav Irapuato]. Avaliable at https://drive.google.com/file/d/1NckRmpvxeOdoJG3ugbZSKsHyYEua4eYG/view?usp=sharing.

[3] Buchfink B, Reuter K, Drost HG, "Sensitive protein alignments at tree-of-life scale using DIAMOND", *Nature Methods* **18**, 366–368 (2021). [doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x)

[4] Fassler J, Cooper P. BLAST Glossary. 2011 Jul 14. In: BLAST® Help [Internet].  Bethesda (MD): National Center for Biotechnology Information (US);  2008-.  Available from: https://www.ncbi.nlm.nih.gov/books/NBK62051/
