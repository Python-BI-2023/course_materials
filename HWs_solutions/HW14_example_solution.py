from abc import ABC, abstractmethod

import numpy as np


# ошибки могут быть 2 любые разумные
class EquipmentNotFoundError(Exception):
    pass


class BookingError(Exception):
    pass


class User:
    def __init__(self, name):
        self.name = name


class Booking:
    def __init__(self, equipment, user, start_time, end_time):
        self.equipment = equipment
        self.user = user
        # время можно принимать временем, можно принимать строкой и переводить во время
        self.start_time = start_time
        self.end_time = end_time

    def is_intersect(self, other) -> bool:
        if self.equipment != other.equipment:
            return False

        return ((self.start_time <= other.start_time < self.end_time) or (
                other.start_time <= self.start_time < other.end_time))


class LabEquipment:
    def __init__(self, equipment):
        # Эти атрибуты можно сделать классовыми
        self.equipment = equipment
        self.booking_history = []

    def is_available(self, new_booking: Booking) -> bool:
        if new_booking.equipment not in self.equipment:
            raise EquipmentNotFoundError(f"Equipment '{new_booking.equipment}' not found.")

        for booking in self.booking_history:
            if booking.is_intersect(new_booking):
                return False
        return True

    def book(self, new_booking: Booking):
        if new_booking.equipment not in self.equipment:
            raise EquipmentNotFoundError(f"Equipment '{new_booking.equipment}' not found.")

        if not self.is_available(new_booking):
            raise BookingError(f"Time slot for '{new_booking.equipment}' is already booked.")

        self.booking_history.append(new_booking)


class GenCodeInterpreter:
    def __init__(self):
        self.memory = [0] * 5000
        self.pointer = 0
        self.output = None

    def eval(self, code):
        self.output = ''

        for command in code:
            match command:
                case 'A':
                    self.pointer += 1
                case 'T':
                    self.pointer -= 1
                case 'G':
                    self.memory[self.pointer] += 1
                case 'C':
                    self.memory[self.pointer] -= 1
                case 'N':
                    self.output += chr(self.memory[self.pointer])
                case _:
                    print('Unknown command!')
        return self.output


def meet_the_dunders():
    res = int.__int__(0)

    matrix = list.__new__(list)
    idx = int.__int__(0)
    while idx.__lt__(100):
        matrix.__iadd__([list.__call__(range(idx, idx.__add__(10)))])
        idx = idx.__add__(10)

    def func_1(x):
        return range(1, 5, 2).__contains__(x)

    def func_2(x):
        return [x.__getitem__(col) for col in selected_columns_indices]

    selected_columns_indices = list.__call__(filter(func_1, range(matrix.__len__())))
    selected_columns = map(func_2, matrix)

    arr = np.array(list(selected_columns))

    mask = arr.__getitem__((slice(None), 1)).__mod__(3).__eq__(0)
    new_arr = arr.__getitem__(mask)

    product = new_arr.__matmul__(new_arr.T)

    if product.__getitem__(0).__lt__(1000).__eq__(True).__and__(product.__getitem__(2).__gt__(1000)).__contains__(
            True).__bool__():
        res = int(product.mean().__truediv__(10).__mod__(100))
    return res


def filter_fastq(input_path,
                 gc_bounds=(0, 100),
                 length_bounds=(0, 2 ** 32),
                 quality_threshold=0,
                 output_path=None):
    ...
    #records = list(SeqIO.parse(input_path, 'fastq'))
    #...
    #with open(output_path, 'w') as file:
    #    SeqIO.write(filtered_results, file, 'fastq')

class BiologicalSequence(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def is_alphabet_correct(self):
        pass


class NucleicAcidSequence(BiologicalSequence):
    alphabet = None
    complement_dict = None

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, idx):
        return self.seq.__getitem__(idx)

    def __str__(self):
        return str(self.seq)

    def __repr__(self):
        return str(self.seq)

    def is_alphabet_correct(self):
        return set(self.seq) <= self.alphabet

    def complement(self):
        if self.complement_dict is None:
            raise ValueError

        result = type(self)(''.join([self.complement_dict[base] for base in self.sequence]))
        return result

    def count_gc_content(self):
        length = len(self.seq)
        if length == 0:
            return 0
        else:
            gc_count = len([base for base in self.seq if base.upper() in ['G', 'C']])
            return gc_count * 100 / length


class DNASequence(NucleicAcidSequence):
    alphabet = 'ATGC'
    complement_dict = {
        'a': 't', 'A': 'T',
        't': 'a', 'T': 'A',
        'g': 'c', 'G': 'C',
        'c': 'g', 'C': 'G'
    }
    transcription_dict = {
        'a': 'a', 'A': 'A',
        't': 'u', 'T': 'U',
        'g': 'g', 'G': 'G',
        'c': 'c', 'C': 'C'
    }

    def __init__(self, seq):
        super().__init__(seq)

    def transcribe(self):
        return RNASequence(''.join([self.transcription_dict[base] for base in self.seq]))


class RNASequence(NucleicAcidSequence):
    alphabet = 'AUGC'
    complement_dict = {
        'u': 'u', 'A': 'U',
        't': 'a', 'U': 'A',
        'g': 'c', 'G': 'C',
        'c': 'g', 'C': 'G'
    }

    def __init__(self, seq):
        super().__init__(seq)


class AminoAcidSequence(BiologicalSequence):
    pass  # тут что-нибудь из прошлого семестра
