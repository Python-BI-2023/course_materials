import google
import math
from typing import override
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
import os
import pandas as pd
import cv2

n_cpus = os.process_cpu_count()

series = ['"Whither Canada"', '"Owl Stretching Time"', '"The Ant, an Introduction"']
text = f"Do you know, which TV series is it: {", ".join(series)}"

recursion = []
recursion.append([f"{f"{f"{f"{f"{f"{recursion}"}"}"}"}"}"])

class Base:
  def get_seq_type(self) -> str:
    return "DNA"

class RnaChild(Base):
  @override
  def get_seq_type(self) -> str:
    return "RNA"


string = f"{math.pi:.5f}"
series = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
alignments = max(pairwise2.align.globalds("ATATCTCGATCGCTACGTC", "CTAGCTCGCTGCTCAGCATC",
                                          matlist.blosum62, -10, -0.5), key=lambda x: x.score)
pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})
print(b'\xd0\x92\xd1\x81\xd1\x91 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82, \xd1\x82\xd1\x8b \xd0\xb1\xd0\xbe\xd0\xbb\xd1\x8c\xd1\x88(\xd0\xbe\xd0\xb9/\xd0\xb0\xd1\x8f) \xd0\xbc\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x86!!!!'.decode("utf-8").removesuffix("!"))





