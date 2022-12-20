"""
    public
    protected
    private
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu_core = cpu                   # private
        self._memory = memory                   # protected
        self.hdd = hdd                          # public

    def print_computer(self):                   # public method
        print('CPU: {} MHz,\nMemory: {} Mb,\nHDD: {} Gb'.format(
            self.__cpu_core,
            self._memory,
            self.hdd
        ))

    @property
    def cpu(self):
        return self.__cpu_core

    @cpu.setter
    def cpu(self, cpu):
        if cpu < 0:
            raise ValueError(f'Incorrect value {cpu}')

        self.__cpu_core = cpu


comp = Computer(2300, 16000, 2000)

comp.print_computer()
print(dir(comp))
print(comp._Computer__cpu_core)
print(comp._memory)
print(comp.hdd)
# comp.get_cpu()
# comp.set_cpu(324532423)
print(comp.cpu)
comp.cpu = 4536453
