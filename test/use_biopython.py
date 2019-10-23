#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/22 18:54
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : use_biopython.py

from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read('test/1.fa', format='fasta')
result_handle = NCBIWWW.qblast("blastp", "nt", record.format("fasta"))

with open('data/my_blast.xml', 'w') as f:
    f.write(result_handle.read())
result_handle.close()
