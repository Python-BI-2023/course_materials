import os
import shutil
import sys
import time
from dataclasses import dataclass
from typing import Any, Generator, Iterator


class MeasureTime:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Elapsed time is: {elapsed_time}")


class TmpDir:
    def __init__(self, path: str = '.', to_delete: bool = True):
        self.path = path
        self.to_delete = to_delete
        self.unique_name = self._create_unique_name()
        self.tmp_dir_path = os.path.join(self.path, self.unique_name)

    def __enter__(self) -> str:
        os.mkdir(self.tmp_dir_path)
        print(f"Temporary directory is: {self.tmp_dir_path}")
        return self.tmp_dir_path

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self.to_delete:
            shutil.rmtree(self.tmp_dir_path)
            print(f"Temporary directory {self.tmp_dir_path} deleted")

    def _create_unique_name(self) -> str:
    # тут любой адекватный способ сделать уникальное имя
    # отдельно хороший ход - добавить проверку на всякий случай
        return f"tmp_{int(time.time())}"


class MyDict(dict):
    def __iter__(self):
        return iter(self.items())


class NotFasta(TypeError):
    pass


@dataclass
class FastaRecord:
    id: str
    description: str
    seq: str

    def __repr__(self):
        return f"FastaRecord(id={self.id}, description={self.description}, seq={self.seq})"


class OpenFasta:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.line = None
        
    def __enter__(self):
        self.file = open(self.path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def __iter__(self):
        return self
    
    def read_record(self):
        return next(self)

    def read_records(self):
        records = []
        for record in self:
            records.append(record)
        return records    

    def __next__(self):
        if self.line is None:
            self.line = self.file.readline().rstrip()
        elif self.line == '':
            raise StopIteration

        seq_id, descr = self.line.split(' ', 1)
        seq_id = seq_id.strip('>')
        seq = ''
        
        self.line = self.file.readline().strip()
        while (not (self.line.startswith('>'))) and (self.line != ''):
            seq = seq + self.line
            self.line = self.file.readline().rstrip()
        return FastaRecord(id=seq_id, description=descr, seq=seq)
