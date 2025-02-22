# randsample

## Overview
The `randsample` command is part of the MACS3 suite of tools and is
used to randomly sample a certain number or percentage of tags from
alignment files. This can be useful in ChIP-Seq analysis when a
subset of the data is required for downstream analysis. 

## Detailed Description

The `randsample` command takes in one or multiple input alignment
files and produces an output file with the randomly sampled tags. It
will randomly sample the tags, according to setting for percentage or
for total number of tags to be kept. 

When `-p 100` is used, which means we want to keep all reads, the
`randsample` command can be used to convert any format MACS3 supported
to BED (or BEDPE if the input is BAMPE format) format. It can generate
the same result as `filterdup --keep-dup all` to convert other formats
into BED/BEDPE format.

Please note that, when writing BED format output for single-end
dataset, MACS3 assume all the reads having the same length either from
`-s` setting or from auto-detection.

## Command Line Options

Here is a brief overview of the `randsample` options:

- `-i` or `--ifile`: Alignment file. If multiple files are given as
  '-t A B C', then they will all be read and combined. REQUIRED. 
- `-p` or `--percentage`: Percentage of tags you want to keep. Input
  80.0 for 80%. This option can't be used at the same time with
  -n/--num. If the setting is 100, it will keep all the reads and
  convert any format that MACS3 supports into BED or BEDPE (if input
  is BAMPE) format. REQUIRED 
- `-n` or `--number`: Number of tags you want to keep. Input 8000000
  or 8e+6 for 8 million. This option can't be used at the same time
  with -p/--percent. Note that the number of tags in the output is
  approximate as the number specified here. REQUIRED 
- `--seed`: Set the random seed while downsampling data. Must be a
  non-negative integer in order to be effective. If you want more
  reproducible results, please specify a random seed and record
  it. DEFAULT: not set
- `-o` or `--ofile`: Output BED file name. If not specified, will
  write to standard output. Note, if the input format is BAMPE or
  BEDPE, the output will be in BEDPE format. DEFAULT: stdout 
- `--outdir`: If specified, all output files will be written to that
  directory. Default: the current working directory 
- `-s` or `--tsize`: Tag size. This will override the auto-detected
  tag size. DEFAULT: Not set 
- `-f` or `--format`: Format of the tag file. 
  - `AUTO`: MACS3 will pick a format from "AUTO", "BED", "ELAND",
    "ELANDMULTI", "ELANDEXPORT", "SAM", "BAM", "BOWTIE", "BAMPE", and
    "BEDPE". Please check the definition in the README file if you
    choose ELAND/ELANDMULTI/ELANDEXPORT/SAM/BAM/BOWTIE or
    BAMPE/BEDPE. DEFAULT: "AUTO" 
- `--buffer-size`: Buffer size for incrementally increasing the
  internal array size to store read alignment information. In most
  cases, you don't have to change this parameter. However, if there
  are a large number of chromosomes/contigs/scaffolds in your
  alignment, it's recommended to specify a smaller buffer size in
  order to decrease memory usage (but it will take longer time to read
  alignment files). Minimum memory requested for reading an alignment
  file is about # of CHROMOSOME * BUFFER_SIZE * 8 Bytes. DEFAULT:
  100000 
- `--verbose`: Set the verbose level. 0: only show critical messages,
  1: show additional warning messages, 2: show process information, 3:
  show debug messages. If you want to know where the duplicate reads
  are, use 3. DEFAULT: 2 


## Example Usage

Here is an example of how to use the `randsample` command: 

```bash
macs3 randsample -i treatment.bam -o sampled.bed -f BAM -p 10
```

In this example, the program will randomly sample 10 percent of total
tags from the `treatment.bam` file and write the result to
`sampled.bed`. 

