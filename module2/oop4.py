"""
Scenario
Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
The methods are delivered by the following classes:
scan(), delivered by the Scanner class;
print(), delivered by the Printer class;
send() and print(), delivered by the Fax class.
Each method should print a message indicating its purpose and origin, like:
'print() method from Printer class'
'send() method from Fax class'
create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
on each object call the methods: scan(), print(), send();
observe the output differences. Was the Printer class utilized each time?
"""


class Scanner(object):
    def scan(self):
        print("Scanner: scanning...")


class Printer(object):
    def print(self):
        print("Printer: Printing...")


class Fax(object):
    def send(self):
        print("Fax: sending...")

    def print(self):
        print("Fax: printing...")


class MultiFunctionalDeviceSPF(Scanner, Printer, Fax): ...


class MultiFunctionalDeviceSFP(Scanner, Fax, Printer): ...


def main():
    spf = MultiFunctionalDeviceSPF()
    sfp = MultiFunctionalDeviceSFP()

    spf.scan()
    spf.print()  # from Printer
    spf.send()

    sfp.scan()
    sfp.print()  # from Scanner
    sfp.send()


if __name__ == "__main__":
    main()
