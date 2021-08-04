from multiprocessing import Process, Manager

''' Custom Module Imports '''
from calculator.add import addition
from calculator.subtract import subtraction
from calculator.multiply import multiplication
from calculator.divide import division


class Main:
    def __init__(self) -> None:
        pass

    def calculatorFunction(self):
        ls = [[1,2],[3,4],[5,6]]
        with Manager() as manager:
            result = manager.dict()
            for i in ls:
                obj1 = addition(i[0],i[1], result)
                obj2 = subtraction(i[0],i[1], result)
                obj3 = multiplication(i[0],i[1], result)
                obj4 = division(i[0],i[1], result)

                p1 = Process(target=obj1.add)
                p2 = Process(target=obj2.subtract)
                p3 = Process(target=obj3.multiply)
                p4 = Process(target=obj4.divide)

                p = [p1,p2,p3,p4]

                p1.start()
                p2.start()
                p3.start()
                p4.start()

                for procs in p:
                    procs.join()

                print(result)

if __name__ == '__main__':
    main = Main()
    main.calculatorFunction()