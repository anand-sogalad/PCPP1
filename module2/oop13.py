"""
lab1:
Scenario
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;
create an abstract class representing a scanner that enforces the following methods:
scan_document – returns a string indicating that the document has been scanned;
get_scanner_status – returns information about the scanner (max. resolution, serial number)
Create an abstract class representing a printer that enforces the following methods:
print_document – returns a string indicating that the document has been printed;
get_printer_status – returns information about the printer (max. resolution, serial number)
Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.
"""

import abc


class Scanner(abc.ABC):
    def scan_document(self):
        return "Document was scanned"

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    def print_document(self):
        return "Document was printed"

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def get_scanner_status(self):
        return "Max scan resolution is low, S/N: S001"

    def get_printer_status(self):
        return "Max print resolution is low, S/N: P001"


class MFD2(Scanner, Printer):
    def get_scanner_status(self):
        return "Max scan resolution is fine, S/N: S002"

    def get_printer_status(self):
        return "Max print resolution is fine, S/N: P002"

    def get_history(self):
        return "The history is..."


class MFD3(Scanner, Printer):
    def get_scanner_status(self):
        return "Max scan resolution is high, S/N: S003"

    def get_printer_status(self):
        return "Max print resolution is high, S/N: P003"

    def get_history(self):
        return "The history is..."

    def send_fax(self):
        print("sending fax")

    def receive_fax(self):
        print("receiving fax")


mfd1 = MFD1()
print(mfd1.print_document())
print(mfd1.get_printer_status())

mfd2 = MFD2()
print(mfd2.print_document())
print(mfd2.get_printer_status())

mfd3 = MFD3()
print(mfd3.print_document())
print(mfd3.get_printer_status())
