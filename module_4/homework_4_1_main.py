from homework_4_1_module import print_3
import homework_4_1_module as module
import  sys

print(dir(module))

module.print_1()
module.print_2()
print_3()

for path in sys.path:
    print(path)

print(sys)