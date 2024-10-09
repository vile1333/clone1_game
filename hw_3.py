class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self,value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self,value):
        self.__memory = value

    def make_computations(self):
        return f'Арифметические вычесления: {self.__cpu * self.__memory}'

    def __str__(self):
        return f'CPU: {self.__cpu}, Memory: {self.__memory}'

    def __eq__(self,other):
        return self.__memory == other.memory

    def __ne__(self,other):
        return self.memory != other.memory

    def __lt__(self,other):
        return self.__memory < other.memory

    def __gt__(self,other):
        return self.__memory > other.memory

    def __le__(self,other):
        return self.__memory <= other.memory

    def __ge__(self,other):
        return self.__memory >= other.memory

class Phone:
    def __init__(self,sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self,value):
        self.__sim_card_list = value

    def call(self, simcard_num, call_num):
        simcard = self.sim_card_list[simcard_num - 1]
        print(f'Идет звонок на номер {call_num} c симки {simcard_num} - {simcard}')

    def __str__(self):
        return f'Phone(sim_card_list={self.__sim_card_list})'

class Smartphone(Computer, Phone):
    def __init__(self,cpu,memory,sim_card_list):
        Phone.__init__(self,sim_card_list)
        Computer.__init__(self,cpu,memory)

    def use_gps(self,location):
        print(f'Маршрут до локации: {location}')

    def __str__(self):
        return f'Smartphone(CPU: {self.cpu}, Memory: {self.memory}, Simcard list: {self.sim_card_list})'

computer = Computer(16,32)
telephone = Phone(sim_card_list = ['Beeline','O!'])
smartphone = Smartphone(8,32,sim_card_list = ['Beeline','O!'])
other_smartphone = Smartphone(8,32,sim_card_list = ['O!','Megacom'])

print(computer)
print(telephone)
print(smartphone)
print(other_smartphone)

print(computer.make_computations())
telephone.call(1, '+ 996 777 99 88 11')
telephone.call(2, '+ 996 555 00 00 00')
smartphone.use_gps('Osh')
other_smartphone.use_gps('Kara-Balta')

print(computer > smartphone)
print(other_smartphone < smartphone)
print(computer == smartphone)
print(computer >= smartphone)
print(computer <= smartphone)
print(computer != other_smartphone)